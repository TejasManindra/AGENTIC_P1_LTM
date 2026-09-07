from dataclasses import dataclass


@dataclass
class InsightResult:
    insights: list[str]


class InsightGenerationAgent:
    def generate(
        self,
        data: list[dict],
        dimension: str,
        metric: str,
    ) -> InsightResult:
        if not data:
            raise ValueError("Insight data cannot be empty.")

        if dimension not in data[0]:
            raise ValueError(
                f"Dimension '{dimension}' not found."
            )

        if metric not in data[0]:
            raise ValueError(
                f"Metric '{metric}' not found."
            )

        highest = max(
            data,
            key=lambda row: row[metric],
        )

        lowest = min(
            data,
            key=lambda row: row[metric],
        )

        insights = [
            (
                f"{highest[dimension]} generated the highest "
                f"{metric} with a value of "
                f"{highest[metric]:.2f}."
            ),
            (
                f"{lowest[dimension]} generated the lowest "
                f"{metric} with a value of "
                f"{lowest[metric]:.2f}."
            ),
        ]

        return InsightResult(
            insights=insights,
        )