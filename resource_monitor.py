# resource_monitor.py
import shutil
import psutil
import logging

logger = logging.getLogger(__name__)

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    result = f"Disk Usage for {path} - Total: {total//(2**30)}GB, Used: {used//(2**30)}GB, Free: {free//(2**30)}GB"
    logger.info(result)
    return result

def check_memory():
    mem = psutil.virtual_memory()
    result = f"Memory - Total: {mem.total//(2**20)}MB, Available: {mem.available//(2**20)}MB, Used: {mem.percent}%"
    logger.info(result)
    return result

# aws_logs.py
import boto3
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

def fetch_cloudwatch_logs(log_group, stream_name):
    client = boto3.client('logs')
    end_time = int(datetime.now().timestamp() * 1000)
    start_time = int((datetime.now() - timedelta(minutes=5)).timestamp() * 1000)

    response = client.get_log_events(
        logGroupName=log_group,
        logStreamName=stream_name,
        startTime=start_time,
        endTime=end_time,
        limit=20
    )
    messages = [event['message'] for event in response['events']]
    logger.info(f"Fetched logs: {messages}")
    return messages
