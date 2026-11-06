import pytest
from chanakya.policy import Denied, get_tool, require_lab_approval, tools
from chanakya.lab import SCAN

def test_unique_ids():
    assert len(tools()) == len({t["id"] for t in tools()})

def test_unknown_tool_rejected():
    with pytest.raises(Denied):
        get_tool("host.shell")

def test_approval_required():
    with pytest.raises(Denied):
        require_lab_approval("lab.scan", False)

def test_readonly_cannot_be_invoked_as_active():
    with pytest.raises(Denied):
        require_lab_approval("registry.list", True)

def test_fixed_scan_target_and_port():
    assert SCAN[-1] == "target"
    assert SCAN[-2] == "80"
