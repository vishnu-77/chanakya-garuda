"""Single-user local CLI; no remotely exposed endpoints."""
import argparse
import asyncio
import json
import subprocess
from dotenv import load_dotenv
from .policy import ROOT, tools
from .lab import COMPOSE, audit, scan

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(prog="chanakya")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("tools")
    ask = commands.add_parser("ask")
    ask.add_argument("question")
    commands.add_parser("lab-up")
    commands.add_parser("lab-down")
    commands.add_parser("lab-scan")
    voice = commands.add_parser("voice")
    voice.add_argument("audio_file")
    args = parser.parse_args()
    if args.command == "tools":
        print(json.dumps(tools(), indent=2))
    elif args.command in {"lab-up", "lab-down"}:
        cmd = ["docker", "compose", "-f", str(COMPOSE)]
        if args.command == "lab-up":
            cmd += ["up", "-d", "target"]
        else:
            cmd += ["down"]
        subprocess.run(cmd, cwd=ROOT, check=True)
    elif args.command == "lab-scan":
        approved = input("Approve fixed Docker-internal target:80 scan? Type APPROVE LAB SCAN: ") == "APPROVE LAB SCAN"
        if not approved:
            audit(tool="lab.scan", decision="deny", reason="operator rejected")
            raise SystemExit("Denied")
        print(json.dumps(scan(approved=True), indent=2))
    elif args.command in {"ask", "voice"}:
        from .agent import answer
        question = args.question if args.command == "ask" else _voice(args.audio_file)
        print(asyncio.run(answer(question)))

def _voice(audio_file):
    from .voice import transcribe
    result = transcribe(audio_file)
    print("Local transcript:", result)
    return result

if __name__ == "__main__":
    main()
