"""Model-facing tools: no shell, external network scan or writable filesystem."""
import json
from .policy import EVIDENCE, get_tool, tools

def list_tools() -> str:
    """List available registered tools; discovery is not permission to execute."""
    get_tool("registry.list")
    return json.dumps(tools(), indent=2)

def read_lab_evidence() -> str:
    """Read existing lab evidence, never execute scans."""
    get_tool("lab.evidence")
    if not EVIDENCE.exists():
        return "No scan evidence exists. Use the separate approved lab-scan CLI."
    return EVIDENCE.read_text(encoding="utf-8")[:25000]
