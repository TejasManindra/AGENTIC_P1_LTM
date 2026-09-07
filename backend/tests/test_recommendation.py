from backend.agents.recommendation import (
    RecommendationAgent,
)


def test_recommendation():
    insights = [
        "South generated the highest profit with a value of 3981.50.",
        "North generated the lowest profit with a value of 2450.75.",
    ]

    agent = RecommendationAgent()

    result = agent.recommend(insights)

    assert len(result.recommendations) == 2

    assert (
        "increasing investment"
        in result.recommendations[0].lower()
    )

    assert (
        "corrective actions"
        in result.recommendations[1].lower()
    )