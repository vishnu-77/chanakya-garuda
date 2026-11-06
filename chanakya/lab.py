"""Fixed Docker runner. Only accessible from explicit operator CLI."""
import json
import subprocess
from datetime import datetime, timezone
from .policy import ROOT, DATA, EVIDENCE, AUDIT, require_lab_approval

COMPOSE = ROOT / "lab" / "compose.yaml"
SCAN = ["docker", "compose", "-f", str(COMPOSE), "run", "--rm",
        "--no-deps", "scanner", "-sT", "-Pn", "-p", "80", "target"]

def audit(**fields):
    DATA.mkdir(exist_ok=True)
    with AUDIT.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"time": datetime.now(timezone.utc).isoformat(), **fields}) + "\n")

def scan(approved: bool = False):
    try:
        require_lab_approval("lab.scan", approved)
    except PermissionError:
        audit(tool="lab.scan", decision="deny")
        raise
    audit(tool="lab.scan", decision="allow", target="target:80")
    result = subprocess.run(SCAN, cwd=ROOT, text=True, capture_output=True,
                            timeout=180, check=False)
    evidence = {"target": "docker-internal:target:80", "returncode": result.returncode,
                "stdout": result.stdout[-20000:], "stderr": result.stderr[-4000:]}
    DATA.mkdir(exist_ok=True)
    EVIDENCE.write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    audit(tool="lab.scan", decision="completed", returncode=result.returncode)
    return evidence
