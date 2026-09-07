from backend.agents.query_understanding import (
    QueryIntent,
)
from backend.agents.sql_generation import (
    SQLGenerationAgent,
)


def test_sql_generation():
    intent = QueryIntent(
        original_query="Which region generated the highest profit?",
        metric="profit",
        dimensions=["region"],
        comparison="highest",
    )

    agent = SQLGenerationAgent()

    result = agent.generate(intent)

    assert "SELECT" in result.query
    assert "SUM(profit)" in result.query
    assert "GROUP BY region" in result.query
    assert "ORDER BY total_profit DESC" in result.query