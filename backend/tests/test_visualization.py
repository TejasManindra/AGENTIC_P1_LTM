import pandas as pd

from backend.agents.visualization import (
    VisualizationAgent,
)


def test_visualization():
    data = pd.DataFrame(
        {
            "region": ["South", "North", "West"],
            "profit": [3981.50, 2450.75, 3120.25],
        }
    )

    agent = VisualizationAgent()

    figure = agent.create_bar_chart(
        data=data,
        x_column="region",
        y_column="profit",
        title="Profit by Region",
    )

    assert figure is not None
    assert figure.layout.title.text == "Profit by Region"
    assert len(figure.data) == 1