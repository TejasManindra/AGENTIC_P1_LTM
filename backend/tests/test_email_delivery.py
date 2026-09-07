from backend.agents.email_delivery import (
    EmailDeliveryAgent,
)


def test_email_delivery():
    agent = EmailDeliveryAgent()

    result = agent.prepare_email(
        recipient="manager@example.com",
        subject="Business Intelligence Report",
        body="Please find the latest business analysis report attached.",
        attachment_path="reports/business_report.pdf",
    )

    assert result.recipient == "manager@example.com"
    assert result.subject == "Business Intelligence Report"
    assert result.attachment_path == (
        "reports/business_report.pdf"
    )