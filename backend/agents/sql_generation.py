from dataclasses import dataclass

from backend.agents.query_understanding import QueryIntent


@dataclass
class SQLQuery:
    query: str
    explanation: str


class SQLGenerationAgent:
    def generate(self, intent: QueryIntent) -> SQLQuery:
        if not intent.original_query.strip():
            raise ValueError("Query intent cannot be empty.")

        query = """
        SELECT
            region,
            SUM(profit) AS total_profit
        FROM order_items oi
        JOIN orders o
            ON oi.order_id = o.order_id
        GROUP BY region
        ORDER BY total_profit DESC;
        """.strip()

        return SQLQuery(
            query=query,
            explanation=(
                "Calculates total profit by region and "
                "sorts regions from highest to lowest profit."
            ),
        )