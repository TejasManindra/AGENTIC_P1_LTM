from backend.agents.query_understanding import (
    QueryUnderstandingAgent,
)


def test_query_understanding():
    agent = QueryUnderstandingAgent()

    result = agent.understand(
        "Which region generated the highest profit?"
    )

    assert result.original_query == (
        "Which region generated the highest profit?"
    )