# health_check.py
import requests
import socket
import subprocess
import logging

logger = logging.getLogger(__name__)

def check_url_health(url):
    try:
        response = requests.get(url, timeout=5)
        result = f"{url} - Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        result = f"{url} - Error: {e}"
    logger.info(result)
    return result

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            result = f"{host}:{port} is reachable"
    except Exception as e:
        result = f"{host}:{port} is NOT reachable - {e}"
    logger.info(result)
    return result

def check_service_status(service_name):
    try:
        result = subprocess.run(['systemctl', 'is-active', service_name], stdout=subprocess.PIPE)
        status = f"{service_name}: {result.stdout.decode().strip()}"
    except Exception as e:
        status = f"{service_name} check failed - {e}"
    logger.info(status)
    return status
