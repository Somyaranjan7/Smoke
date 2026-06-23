# SMOKE - Vulnerability Scanner

## Overview

SMOKE is a web-based vulnerability scanner developed using Python and Flask. It allows users to scan a target host for open ports, detect services and versions, analyze associated risks, and generate detailed reports. Registered users can maintain a scan history and revisit previously generated reports.

---

# Features

## Guest User Features

* Scan an IP address or hostname without logging in.
* Detect open and closed ports.
* Identify running services and service versions.
* View risk levels for discovered ports.
* Receive security recommendations for open ports.

---

## Registered User Features

* User registration and login.
* Persistent scan history stored in MySQL.
* View previous scans.
* View TXT reports inside the website.
* View PDF reports directly inside the browser.
* Repeat scan for individual ports after remediation.

---

# Risk Classification

| Port State                           | Risk Level |
| ------------------------------------ | ---------- |
| Closed                               | No Risk    |
| Open (Common Services)               | Low        |
| Open (Moderately Sensitive Services) | Medium     |
| Open (High-Risk Services)            | High       |

Risk indicators are color coded:

* 🔴 High
* 🟠 Medium
* 🟢 Low
* ⚫ No Risk

---

# Report Generation

Each scan generates:

### TXT Report

Contains:

* Port number
* State
* Service
* Version
* Risk level
* Explanation of why the port may be dangerous
* Security recommendations

TXT reports are displayed inside the website.

---

### PDF Report

Contains:

* Port number
* State
* Service
* Version
* Risk level
* Security explanation
* Recommendations

PDF reports are opened directly in the browser.

---

# Repeat Scan Feature

SMOKE does not attempt to close ports automatically.

Instead:

1. The administrator performs remediation manually.
2. The user clicks **Repeat Scan** beside a port.
3. SMOKE rescans only that specific port.
4. The updated state of the port is displayed.

---

# Technologies Used

## Backend

* Python 3
* Flask
* PyMySQL
* python-nmap
* ReportLab
* Werkzeug Security

## Database

* MySQL

## Frontend

* HTML
* CSS
* JavaScript
* Jinja2 Templates

---

# Project Structure

```text
VulnScanner
│
├── app.py
│
├── database
│   ├── __init__.py
│   ├── db.py
│   ├── queries.py
│   └── create_tables.py
│
├── scanner
│   ├── __init__.py
│   ├── port_scanner.py
│   ├── service_detection.py
│   ├── enumeration.py
│   ├── risk_analysis.py
│   ├── recommendations.py
│   └── scanner_engine.py
│
├── reports
│   ├── __init__.py
│   ├── txt_report.py
│   ├── pdf_report.py
│   └── report_manager.py
│
├── fixes
│   ├── __init__.py
│   └── repeat_scan.py
│
├── generated_reports
│   ├── txt
│   └── pdf
│
├── templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── result.html
│   ├── history.html
│   ├── reports.html
│   ├── repeat_result.html
│   └── txt_report_view.html
│
├── static
│   ├── css
│   │   ├── style.css
│   │   ├── forms.css
│   │   ├── tables.css
│   │   ├── dashboard.css
│   │   └── responsive.css
│   │
│   └── js
│       ├── main.js
│       ├── validation.js
│       └── notifications.js
│
├── requirements.txt
└── README.md
```

---

# Database Tables

## user

Stores user credentials.

Fields:

* id
* username
* email
* password

---

## scan_history

Stores scan metadata.

Fields:

* id
* target
* scan_time
* txt_report_path
* pdf_report_path
* user_id

---

## port_result

Stores information for each scanned port.

Fields:

* id
* port
* state
* service
* version
* risk
* recommendation
* scan_id

---

# Installation

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install flask
pip install pymysql
pip install python-nmap
pip install reportlab
pip install werkzeug
```

or

```bash
pip install -r requirements.txt
```

---

## Create MySQL Database

```sql
CREATE DATABASE vulnscanner;
```

Update credentials inside:

```python
database/db.py
```

Example:

```python
host="localhost"
user="root"
password="your_password"
database="vulnscanner"
```

---

## Create Tables

From the project root:

```bash
python -m database.create_tables
```

---

## Run Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# Workflow

1. User enters an IP address or hostname.
2. Nmap scans the target.
3. Services and versions are detected.
4. Risk analysis is performed.
5. Recommendations are generated.
6. Reports are created.
7. Logged-in users have their scans saved to MySQL.
8. Users may revisit previous reports from History.
9. Users may perform repeat scans on specific ports after remediation.

---

# Future Improvements

* CVSS score integration.
* Dashboard charts and analytics.
* Scheduled scans.
* Email notifications.
* Docker deployment.
* HTTPS support.
* Multi-user administration.

---

# Authors

Developed as a Cybersecurity Vulnerability Assessment Project using Python, Flask, MySQL, and Nmap.

---

SMOKE — Vulnerability Scanner and Security Assessment Tool
