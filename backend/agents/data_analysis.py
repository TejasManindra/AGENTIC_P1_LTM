from dataclasses import dataclass

import pandas as pd


@dataclass
class AnalysisResult:
    summary: str
    metrics: dict
    observations: list[str]


class DataAnalysisAgent:
    def analyze(self, data: pd.DataFrame) -> AnalysisResult:
        if data.empty:
            raise ValueError("Analysis data cannot be empty.")

        metrics = {}

        numeric_columns = data.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:
            metrics[column] = {
                "total": float(data[column].sum()),
                "average": float(data[column].mean()),
                "minimum": float(data[column].min()),
                "maximum": float(data[column].max()),
            }

        observations = []

        for column in numeric_columns:
            observations.append(
                f"{column} has a maximum value of "
                f"{data[column].max():.2f}."
            )

        summary = (
            f"Analyzed {len(data)} records and "
            f"{len(numeric_columns)} numeric metrics."
        )

        return AnalysisResult(
            summary=summary,
            metrics=metrics,
            observations=observations,
        )