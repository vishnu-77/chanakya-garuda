"""Optional read-only stdio MCP façade; not connected to the agent in Phase 0."""
from mcp.server.fastmcp import FastMCP
from .tools import list_tools, read_lab_evidence

server = FastMCP("chanakya-read-only")
server.tool()(list_tools)
server.tool()(read_lab_evidence)

if __name__ == "__main__":
    server.run(transport="stdio")
