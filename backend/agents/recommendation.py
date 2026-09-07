from dataclasses import dataclass


@dataclass
class RecommendationResult:
    recommendations: list[str]


class RecommendationAgent:
    def recommend(
        self,
        insights: list[str],
    ) -> RecommendationResult:
        if not insights:
            raise ValueError("Insights cannot be empty.")

        recommendations = []

        for insight in insights:
            insight_lower = insight.lower()

            if "highest" in insight_lower:
                recommendations.append(
                    "Consider increasing investment in the "
                    "highest-performing area to sustain growth."
                )

            elif "lowest" in insight_lower:
                recommendations.append(
                    "Investigate the lowest-performing area and "
                    "consider targeted corrective actions."
                )

            else:
                recommendations.append(
                    "Review the underlying business drivers "
                    "and identify opportunities for improvement."
                )

        return RecommendationResult(
            recommendations=recommendations,
        )