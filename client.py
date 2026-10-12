"""Cloud Token & GPU FinOps Unit Economics Calculator.
100% Python Standard Library.
"""

class AgentFinOpsUnitCalculator:
    """Computes cost-per-resolved-task, margin health, and caching savings across LLM and GPU inference workloads."""

    @staticmethod
    def calculate_unit_economics(tasks_completed: int, input_tokens: int, cached_tokens: int, output_tokens: int, price_per_1m_in: float = 2.5, price_per_1m_out: float = 10.0) -> dict:
        uncached_in = max(0, input_tokens - cached_tokens)
        cost_uncached = (uncached_in / 1_000_000.0) * price_per_1m_in
        cost_cached = (cached_tokens / 1_000_000.0) * (price_per_1m_in * 0.25)
        cost_out = (output_tokens / 1_000_000.0) * price_per_1m_out

        total_cost = cost_uncached + cost_cached + cost_out
        baseline_cost = (input_tokens / 1_000_000.0) * price_per_1m_in + cost_out
        savings_usd = max(0.0, baseline_cost - total_cost)
        cost_per_task = total_cost / max(1, tasks_completed)

        return {
            "tasks_completed": tasks_completed,
            "total_cost_usd": round(total_cost, 4),
            "cache_savings_usd": round(savings_usd, 4),
            "cost_per_task_usd": round(cost_per_task, 5)
        }
