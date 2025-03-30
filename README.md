"""
# SRE / L2 Application Support Automation Toolkit

A Python-based toolkit designed for SRE and L2 support engineers working with distributed legacy and cloud applications.
Includes health checks, AWS log retrieval, disk/memory monitoring, and auto-remediation.

## Features
- HTTP health checks
- Port reachability test
- Linux service status and restart
- Disk & memory usage monitor
- AWS CloudWatch log fetcher
- S3 file listing and download
- Logging with timestamps
- Email and Slack alerts
- Web dashboard (Flask)

## Setup
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Dashboard
```bash
python dashboard.py
```

## AWS Configuration
Ensure AWS credentials are set in your environment or `~/.aws/credentials`.

## Extend & Schedule
- Use `cron`, `systemd`, or Jenkins for scheduled automation.
- Deploy to AWS Lambda for serverless execution.

"""
