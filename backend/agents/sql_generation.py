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

        question = intent.original_query.lower()

        if "highest profit" in question or "highest-profit" in question:
            query = """
            SELECT
                o.region,
                SUM(oi.profit) AS total_profit
            FROM order_items oi
            JOIN orders o
                ON oi.order_id = o.order_id
            GROUP BY o.region
            ORDER BY total_profit DESC
            """.strip()

            explanation = (
                "Finds the region with the highest total profit."
            )

        elif "lowest profit" in question or "lowest-profit" in question:
            query = """
            SELECT
                o.region,
                SUM(oi.profit) AS total_profit
            FROM order_items oi
            JOIN orders o
                ON oi.order_id = o.order_id
            GROUP BY o.region
            ORDER BY total_profit ASC
            """.strip()

            explanation = (
                "Finds the region with the lowest total profit."
            )

        else:
            query = """
            SELECT
                o.region,
                SUM(oi.profit) AS total_profit
            FROM order_items oi
            JOIN orders o
                ON oi.order_id = o.order_id
            GROUP BY o.region
            ORDER BY total_profit DESC;
            """.strip()

            explanation = (
                "Calculates total profit by region."
            )

        return SQLQuery(
            query=query,
            explanation=explanation,
        )