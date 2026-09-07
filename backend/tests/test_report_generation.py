from pathlib import Path

from backend.agents.report_generation import (
    ReportGenerationAgent,
)


def test_report_generation(tmp_path):
    output_path = tmp_path / "business_report.pdf"

    insights = [
        "South generated the highest profit with a value of 3981.50.",
        "North generated the lowest profit with a value of 2450.75.",
    ]

    recommendations = [
        "Consider increasing investment in the highest-performing area.",
        "Investigate the lowest-performing area and consider corrective actions.",
    ]

    agent = ReportGenerationAgent()

    result = agent.generate_report(
        title="Regional Profit Analysis",
        insights=insights,
        recommendations=recommendations,
        output_path=str(output_path),
    )

    assert result == str(output_path)
    assert Path(result).exists()
    assert Path(result).stat().st_size > 0