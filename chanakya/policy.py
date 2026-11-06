"""Deterministic policy; no model-controlled permission updates."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "tools.json"
DATA = ROOT / "data"
EVIDENCE = DATA / "lab_scan.json"
AUDIT = DATA / "audit.jsonl"

class Denied(PermissionError):
    pass

def tools():
    entries = json.loads(REGISTRY.read_text(encoding="utf-8"))
    ids = [entry["id"] for entry in entries]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate tool IDs")
    return entries

def get_tool(tool_id: str):
    tool = next((entry for entry in tools() if entry["id"] == tool_id), None)
    if tool is None:
        raise Denied("Unknown tool")
    return tool

def require_lab_approval(tool_id: str, approved: bool):
    tool = get_tool(tool_id)
    if tool["risk"] != "active" or tool["scope"] != "lab-only":
        raise Denied("Not an active lab tool")
    if not approved:
        raise Denied("Explicit operator approval required")
