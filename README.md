# Automated SIEM Log Parser & Discord Incident Alert Bot

## 📌 Project Overview
A lightweight, Python-based automation tool engineered to parse **Suricata Intrusion Detection System (IDS)** alerts in real-time. This project acts as a mini-SIEM dashboard pipeline, continuously tracking network activity logs (`fast.log`) and immediately routing critical security anomalies to a security team's Discord channel via structured incoming webhooks.

This architecture bridges the gap between **threat detection** (Blue Teaming) and **automated incident alerting**.

---

## 🛠️ Tech Stack & Concepts Demonstrated
* **Language:** Python 3
* **Libraries:** `requests`, `os`, `time`
* **Security Tooling:** Suricata IDS, hping3, Network Traffic Analysis
* **Core Concepts:** Log Forwarding, Custom Signature Formulation, Automation Scripting

---

## 📁 Repository Structure
* `alert_bot.py`: Main engine tracking log updates and handling secure API calls to Discord.
* `local.rules`: Production-ready signature criteria mapping out conditions for DoS & protocol anomalies.

---

## 🚀 Deployment Instructions

### 1. Prerequisites
Ensure you have Python installed and the required `requests` framework dependency:
```bash
pip install requests
```

### 2. Configuration
Open `alert_bot.py` and modify the setup configurations:
* Change `SURICATA_LOG_PATH` to point to your live Suricata output path.
* Insert your customized incoming application Webhook address into `DISCORD_WEBHOOK_URL`.

### 3. Execution
Start the real-time event processing script:
```bash
python alert_bot.py
```

---

## 🔬 Proof of Concept & Testing
To manually test the monitoring thread without initializing an active network attack, issue a string append command mimicking a live exploit capture:

**On Linux environments:**
```bash
echo "[1:1000001:1] ALERT: POTENTIAL DOS - hping3 ICMP Flood Detected from 192.168.1.45" >> /var/log/suricata/fast.log
```
