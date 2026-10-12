"""MCP server for Cloud Token & GPU FinOps Unit Economics Calculator."""
import sys
import json
from client import AgentFinOpsUnitCalculator

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "calculate_agent_unit_economics",
                "description": "Calculates cost per task and prompt cache savings for agent workloads",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "tasks_completed": {"type": "integer"},
                        "input_tokens": {"type": "integer"},
                        "cached_tokens": {"type": "integer"},
                        "output_tokens": {"type": "integer"}
                    },
                    "required": ["tasks_completed", "input_tokens", "cached_tokens", "output_tokens"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "calculate_agent_unit_economics":
            args = params.get("arguments", {})
            res = AgentFinOpsUnitCalculator.calculate_unit_economics(
                int(args.get("tasks_completed", 1)),
                int(args.get("input_tokens", 0)),
                int(args.get("cached_tokens", 0)),
                int(args.get("output_tokens", 0))
            )
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
