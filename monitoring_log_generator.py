import json
from datetime import datetime

# Available events
PHONE_DETECTED = "phone_detected"
FACE_MISSING = "face_missing"
MULTIPLE_PERSONS = "multiple_persons"

# Change this value to test different detections
detected_event = PHONE_DETECTED

log = {
    "event": detected_event,
    "timestamp": datetime.now().isoformat(timespec="seconds")
}

# Automatically save to JSON file
with open("monitoring_logs.json", "a") as file:
    json.dump(log, file, indent=2)

# Display output
print(json.dumps(log, indent=2))