# restart_service.py
import subprocess
import logging

logger = logging.getLogger(__name__)

def restart_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "restart", service_name], check=True)
        result = f"{service_name} restarted successfully"
    except subprocess.CalledProcessError as e:
        result = f"Failed to restart {service_name} - {e}"
    logger.info(result)
    return result
