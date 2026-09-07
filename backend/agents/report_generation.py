from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class ReportGenerationAgent:
    def generate_report(
        self,
        title: str,
        insights: list[str],
        recommendations: list[str],
        output_path: str,
    ) -> str:
        if not title.strip():
            raise ValueError("Report title cannot be empty.")

        if not insights:
            raise ValueError("Insights cannot be empty.")

        if not recommendations:
            raise ValueError("Recommendations cannot be empty.")

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        pdf = canvas.Canvas(str(path), pagesize=A4)

        width, height = A4
        y_position = height - 60

        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(50, y_position, title)

        y_position -= 40

        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(50, y_position, "Business Insights")

        y_position -= 25

        pdf.setFont("Helvetica", 10)

        for insight in insights:
            pdf.drawString(
                60,
                y_position,
                f"- {insight}",
            )
            y_position -= 20

        y_position -= 15

        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(
            50,
            y_position,
            "Strategic Recommendations",
        )

        y_position -= 25

        pdf.setFont("Helvetica", 10)

        for recommendation in recommendations:
            pdf.drawString(
                60,
                y_position,
                f"- {recommendation}",
            )
            y_position -= 20

        pdf.save()

        return str(path)