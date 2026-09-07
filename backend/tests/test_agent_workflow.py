import pandas as pd

from backend.services.agent_workflow import AgentWorkflow


def test_agent_workflow():
    data = pd.DataFrame(
        {
            "region": ["South", "North", "West"],
            "profit": [3981.50, 2450.75, 3120.25],
        }
    )

    workflow = AgentWorkflow()

    result = workflow.run(
        business_query="Which region generated the highest profit?",
        data=data,
    )

    assert result["query"] == (
        "Which region generated the highest profit?"
    )

    assert result["sql"].query

    assert result["analysis"].summary == (
        "Analyzed 3 records and 1 numeric metrics."
    )

    assert result["figure"] is not None

    assert len(result["insights"].insights) == 2

    assert len(
        result["recommendations"].recommendations
    ) == 2