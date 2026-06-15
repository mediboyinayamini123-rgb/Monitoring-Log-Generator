# Monitoring Log Generator

## Overview

Monitoring Log Generator is a Python-based logging system designed to record monitoring-related events and store them in a structured JSON format for future analysis.

The system tracks events such as:

* Phone Detection
* Face Missing
* Multiple Persons Detected

Each event is logged with a timestamp, enabling monitoring history, auditing, and future analysis.

---

## Features

* Record monitoring events
* Automatic timestamp generation
* JSON-based log storage
* Duplicate log handling
* Easy-to-read output format
* Lightweight and simple implementation

---

## Project Structure

```text
Monitoring Log Generator/
│
├── monitoring_log_generator.py
├── monitoring_logs.json
└── README.md
```

### Files

| File                        | Description                                      |
| --------------------------- | ------------------------------------------------ |
| monitoring_log_generator.py | Main Python script responsible for event logging |
| monitoring_logs.json        | Stores generated monitoring logs                 |
| README.md                   | Project documentation                            |

---

## Technologies Used

* Python 3
* JSON
* Datetime Module

---

## Supported Events

The system currently supports the following monitoring events:

```python
PHONE_DETECTED = "phone_detected"
FACE_MISSING = "face_missing"
MULTIPLE_PERSONS = "multiple_persons"
```

---

## Sample Output

```json
{
  "event": "phone_detected",
  "timestamp": "2026-06-11T10:30:00"
}
```

---

## How It Works

1. User selects or detects a monitoring event.
2. The system generates a timestamp.
3. A log entry is created.
4. The log is stored in `monitoring_logs.json`.
5. The event is displayed in the console.

---

## Usage

Run the Python file:

```bash
python monitoring_log_generator.py
```

Example output:

```json
{
  "event": "phone_detected",
  "timestamp": "2026-06-11T10:30:00"
}
```

---

## Testing

The following scenarios were tested:

* Phone detected event
* Face missing event
* Multiple persons detected event
* Missing timestamp handling
* Duplicate log handling

---

## Challenges Faced

* Preventing duplicate logs
* Managing JSON file storage
* Preserving log history
* Handling missing timestamps

---






