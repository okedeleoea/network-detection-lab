# Endpoint Detection
# (Correlation Engine)
import csv
from collections import defaultdict
from datetime import datetime, timedelta

TIME_WINDOW_MINUTES = 15
PORT_SCAN_THRESHOLD = 20

def parse_time(ts):
    return datetime.fromisoformat(ts)

events = defaultdict(lambda: {
    "ports": set(),
    "admin_events": [],
    "persistence_events": []
})

with open("network.log") as f:
    reader = csv.DictReader(f)
    for row in reader:
        src = row["src_ip"]
        events[src]["ports"].add(row["dest_port"])

with open("windows_events.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        host = row["host"]
        event_id = row["event_id"]
        ts = parse_time(row["timestamp"])

        if event_id in ["4720", "4732"]:
            events[host]["admin_events"].append(ts)

        if event_id in ["4698", "4657"]:
            events[host]["persistence_events"].append(ts)

print("\n=== SOC CORRELATION REPORT ===\n")

for host, data in events.items():
    if len(data["ports"]) >= PORT_SCAN_THRESHOLD:
        for admin_time in data["admin_events"]:
            for persist_time in data["persistence_events"]:
                if abs((persist_time - admin_time).total_seconds()) <= TIME_WINDOW_MINUTES * 60:
                    print("[INCIDENT] Multi-stage compromise detected")
                    print(f" Host        : {host}")
                    print(f" Recon Ports : {len(data['ports'])}")
                    print(f" Admin Event : {admin_time}")
                    print(f" Persistence : {persist_time}")
                    print("-" * 50)
