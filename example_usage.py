"""Example usage for Cloud Token & GPU FinOps Unit Economics Calculator."""
from client import AgentFinOpsUnitCalculator

if __name__ == "__main__":
    res = AgentFinOpsUnitCalculator.calculate_unit_economics(100, 2_000_000, 1_500_000, 500_000)
    print("Cost per Task ($):", res["cost_per_task_usd"], "Cache Savings ($):", res["cache_savings_usd"])
