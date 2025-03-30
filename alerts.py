# alerts.py
import smtplib
from slack_sdk.webhook import WebhookClient
import logging

logger = logging.getLogger(__name__)

def send_email_alert(subject, body, to_email, from_email, smtp_server):
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP(smtp_server) as server:
        server.sendmail(from_email, to_email, message)
    logger.info(f"Email sent to {to_email}")

def send_slack_alert(webhook_url, message):
    webhook = WebhookClient(webhook_url)
    webhook.send(text=message)
    logger.info("Slack alert sent")
