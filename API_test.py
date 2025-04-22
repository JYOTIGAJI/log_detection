import requests
import json
import uuid
from datetime import datetime

import uuid
# The URL of your REST API endpoint
url = "http://10.229.40.118:5000/api/siem_events_data"
# Get the current date and time
now = datetime.now()

# Sample JSON payload
log_data = {
    "HEADER": {
        "sourceId": 1,
        "destId": 2,
        "msgId": 100
    },
    "MESSAGE": {
        'event_id': uuid.uuid4().hex[:32],
        'date': now.day,
        'month': now.month,
        'year': now.year,
        'hour': now.hour,
        'minute': now.minute,
        'second': now.second,  
        "event_type": 2,
        "event_subtype": 10,
        "attacker_info": "10.10.299.31",
        "component": 2,
        "resource_info": "nginx.conf",
        "severity": 4,
        "event_reason": "Multiple failed login attempts",
        "pid": 1234,
        "device_type": 1,
        "device_mac": "aa:bb:cc:dd:ee:ff",
        "device_ip": "192.168.1.1",
        "src_id": 23,
        "log_text": "Potential brute-force attack detected"
    }
}

# Send POST request
response = requests.post(url, json=log_data)

# Print response from the API
print("Status Code:", response.status_code)
print("Response:", response.text)
