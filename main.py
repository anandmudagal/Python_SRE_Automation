# main.py
import logging
from health_check import check_url_health, check_port, check_service_status
from resource_monitor import check_disk_usage, check_memory
from restart_service import restart_service
from alerts import send_email_alert, send_slack_alert

logging.basicConfig(
    filename='automation.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

print(check_url_health("https://yourapp.com/health"))
print(check_port("yourhost.com", 443))
print(check_service_status("nginx"))
print(check_disk_usage("/"))
print(check_memory())
print(restart_service("your-app-service"))

# Send alerts as example
# send_email_alert("Health Check Alert", "Service X failed", "to@example.com", "from@example.com", "smtp.example.com")
# send_slack_alert("https://hooks.slack.com/services/XXX/YYY/ZZZ", "Service X is down")
