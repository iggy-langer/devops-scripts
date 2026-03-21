import os
import json
import logging
import requests

from datetime import datetime, timedelta

def get_config(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Config file '{filename}' not found.")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Failed to parse config file '{filename}'.")
        return {}

def send_slack_notification(url, message):
    try:
        response = requests.post(url, json={'text': message})
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Failed to send Slack notification: {e}")

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')

def get_previous_date(days):
    return (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')

def get_dir_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size