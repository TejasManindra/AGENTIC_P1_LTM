from dataclasses import dataclass


@dataclass
class EmailMessage:
    recipient: str
    subject: str
    body: str
    attachment_path: str


class EmailDeliveryAgent:
    def prepare_email(
        self,
        recipient: str,
        subject: str,
        body: str,
        attachment_path: str,
    ) -> EmailMessage:
        if not recipient.strip():
            raise ValueError("Recipient email cannot be empty.")

        if not subject.strip():
            raise ValueError("Email subject cannot be empty.")

        if not attachment_path.strip():
            raise ValueError("Attachment path cannot be empty.")

        return EmailMessage(
            recipient=recipient,
            subject=subject,
            body=body,
            attachment_path=attachment_path,
        )