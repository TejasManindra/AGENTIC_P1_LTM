import pandas as pd

from backend.agents.data_analysis import (
    DataAnalysisAgent,
)


def test_data_analysis():
    data = pd.DataFrame(
        {
            "region": ["South", "North", "South"],
            "profit": [1250.50, 980.25, 1750.75],
            "sales": [5000.00, 4200.00, 6100.00],
        }
    )

    agent = DataAnalysisAgent()

    result = agent.analyze(data)

    assert result.summary == (
        "Analyzed 3 records and 2 numeric metrics."
    )

    assert result.metrics["profit"]["total"] == 3981.50
    assert result.metrics["sales"]["maximum"] == 6100.00

    assert len(result.observations) == 2