from dataclasses import dataclass
from typing import List


@dataclass
class QueryIntent:
    """Structured representation of a business query."""

    original_query: str
    metric: str | None = None
    dimensions: List[str] | None = None
    time_period: str | None = None
    comparison: str | None = None


class QueryUnderstandingAgent:
    """
    Understands a natural-language business question
    and converts it into a structured query intent.
    """

    def understand(self, query: str) -> QueryIntent:
        """
        Analyze the user's business question.

        AI/LLM-based understanding will be added later.
        """

        if not query or not query.strip():
            raise ValueError("Business query cannot be empty.")

        return QueryIntent(
            original_query=query.strip(),
            metric=None,
            dimensions=[],
            time_period=None,
            comparison=None,
        )