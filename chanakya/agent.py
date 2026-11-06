"""AgentScope/OpenRouter adapter. Requires live integration verification."""
import os
from agentscope.agent import Agent
from agentscope.credential import OpenAICredential
from agentscope.message import UserMsg
from agentscope.model import OpenAIChatModel
from agentscope.permission import PermissionBehavior, PermissionDecision
from agentscope.tool import FunctionTool, Toolkit
from .tools import list_tools, read_lab_evidence

SYSTEM = """You are Chanakya Garuda, an evidence-led engineering assistant.
Only trust registered tool execution results as observations. A scan result is not
proof of a vulnerability. Do not invent authorisation, results or citations.
No active scan tool is exposed to you; use the separately approved local CLI.
Distinguish evidence, inference and uncertainty. Use British English."""

def make_agent():
    key = os.getenv("OPENROUTER_API_KEY", "")
    if not key or key == "replace-me":
        raise RuntimeError("Set OPENROUTER_API_KEY (with a provider-side spend cap)")
    model = OpenAIChatModel(
        credential=OpenAICredential(
            api_key=key,
            base_url="https://openrouter.ai/api/v1",
        ),
        model=os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
        stream=False,
    )
    permission = PermissionDecision(
        behavior=PermissionBehavior.ALLOW,
        message="Allowlisted read-only local tool",
    )
    toolkit = Toolkit(tools=[
        FunctionTool(list_tools, is_read_only=True, permission=permission),
        FunctionTool(read_lab_evidence, is_read_only=True, permission=permission),
    ])
    return Agent(name="Chanakya", system_prompt=SYSTEM, model=model, toolkit=toolkit)

async def answer(question: str) -> str:
    limit = int(os.getenv("JARVIS_MAX_INPUT_CHARS", "12000"))
    if not 0 < len(question) <= limit:
        raise ValueError("Input length outside configured limit")
    reply = await make_agent().reply(UserMsg(name="user", content=question))
    content = getattr(reply, "content", [])
    if isinstance(content, str):
        return content
    return "\n".join(
        block.get("text", "") if isinstance(block, dict) else getattr(block, "text", "")
        for block in content
    ).strip() or str(reply)
