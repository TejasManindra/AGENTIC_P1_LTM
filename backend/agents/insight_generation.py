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

        # -------------------------------------------------
        # Extract valid numeric values
        # -------------------------------------------------

        valid_data = [
            row for row in data
            if row.get(metric) is not None
        ]

        if not valid_data:
            raise ValueError(
                f"No valid values found for metric '{metric}'."
            )

        # -------------------------------------------------
        # Find highest and lowest performers
        # -------------------------------------------------

        highest = max(
            valid_data,
            key=lambda row: float(row[metric])
        )

        lowest = min(
            valid_data,
            key=lambda row: float(row[metric])
        )

        # -------------------------------------------------
        # Calculate total and contribution
        # -------------------------------------------------

        total_value = sum(
            float(row[metric])
            for row in valid_data
        )

        highest_value = float(highest[metric])
        lowest_value = float(lowest[metric])

        highest_share = (
            (highest_value / total_value) * 100
            if total_value != 0
            else 0
        )

        performance_gap = (
            highest_value - lowest_value
        )

        # -------------------------------------------------
        # Generate explainable insights
        # -------------------------------------------------

        highest_name = highest[dimension]
        lowest_name = lowest[dimension]

        insight_1 = (
            f"{highest_name} is the top {dimension} for "
            f"{metric}, generating "
            f"₹{highest_value:,.2f}. "
            f"It contributes approximately "
            f"{highest_share:.1f}% of the total "
            f"{metric} across the analyzed {dimension}s."
        )

        insight_2 = (
            f"{lowest_name} is the lowest-performing "
            f"{dimension}, generating "
            f"₹{lowest_value:,.2f}. "
            f"The performance gap between the strongest "
            f"and weakest {dimension} is "
            f"₹{performance_gap:,.2f}."
        )

        insight_3 = (
            f"The overall {metric} across all analyzed "
            f"{dimension}s is "
            f"₹{total_value:,.2f}. "
            f"The difference between the highest and "
            f"lowest performers should be investigated "
            f"to identify the business drivers behind "
            f"the variation."
        )

        return InsightResult(
            insights=[
                insight_1,
                insight_2,
                insight_3,
            ]
        )

