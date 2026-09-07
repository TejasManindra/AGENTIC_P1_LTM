from backend.agents.insight_generation import (
    InsightGenerationAgent,
)


def test_insight_generation():
    data = [
        {"region": "South", "profit": 3981.50},
        {"region": "North", "profit": 2450.75},
        {"region": "West", "profit": 3120.25},
    ]

    agent = InsightGenerationAgent()

    result = agent.generate(
        data=data,
        dimension="region",
        metric="profit",
    )

    assert len(result.insights) == 2

    assert (
        "South generated the highest profit"
        in result.insights[0]
    )

    assert (
        "North generated the lowest profit"
        in result.insights[1]
    )