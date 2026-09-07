import pandas as pd
import plotly.express as px


class VisualizationAgent:
    def create_bar_chart(
        self,
        data: pd.DataFrame,
        x_column: str,
        y_column: str,
        title: str,
    ):
        if data.empty:
            raise ValueError("Visualization data cannot be empty.")

        if x_column not in data.columns:
            raise ValueError(
                f"X-axis column '{x_column}' not found."
            )

        if y_column not in data.columns:
            raise ValueError(
                f"Y-axis column '{y_column}' not found."
            )

        figure = px.bar(
            data,
            x=x_column,
            y=y_column,
            title=title,
        )

        return figure