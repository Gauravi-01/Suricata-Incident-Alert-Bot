import os
import time
import requests

# ==================== CONFIGURATION ====================
# For Linux/Kali: "/var/log/suricata/fast.log"
# For Windows: "C:/Program Files/Suricata/log/fast.log"
SURICATA_LOG_PATH = "/var/log/suricata/fast.log"  
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL_HERE"
# =======================================================

def send_discord_alert(alert_text):
    """Parses the Suricata log line and pushes a styled alert to Discord."""
    payload = {
        "content": "🚨 **CRITICAL NETWORK INTRA-ALARM TRIGGERED** 🚨",
        "embeds": [{
            "title": "Suricata IDS Detection Event",
            "description": f"```text\n{alert_text.strip()}\n```",
            "color": 15158332,  # Alert Red
            "footer": {
                "text": "Automated Incident Response Bot v1.0"
            }
        }]
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("[+] Alert successfully forwarded to Discord.")
        else:
            print(f"[-] Discord API responded with error code: {response.status_code}")
    except Exception as e:
        print(f"[-] Connectivity Error: {e}")

def monitor_log():
    """Real-time log tailing mechanism."""
    print(f"[*] Starting Security Event Streamer on: {SURICATA_LOG_PATH}")
    
    # Auto-generates a mock environment path for testing if Suricata isn't actively running
    if not os.path.exists(SURICATA_LOG_PATH):
        print(f"[-] Target log file not found. Initializing sandbox simulation path.")
        os.makedirs(os.path.dirname(SURICATA_LOG_PATH), exist_ok=True)
        with open(SURICATA_LOG_PATH, "w") as f:
            f.write("")

    # Seek to the end of the file to ignore old logs and capture live network events
    with open(SURICATA_LOG_PATH, "r") as f:
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)  # Resource conservation pause
                continue
            
            print(f"[!] New Event Intercepted: {line.strip()}")
            send_discord_alert(line)

if __name__ == "__main__":
    monitor_log()
