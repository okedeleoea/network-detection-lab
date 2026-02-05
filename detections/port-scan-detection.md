## Detection: TCP Port Scan

### Description
Detects a single source IP connecting to many destination ports
within a short time window.

### Elastic KQL
```kql
network.transport: "tcp" and
event.category: "network"
Threshold Logic
Group by: source.ip
Count unique destination.port
```
### Threshold: ≥ 20 ports within 5 minutes
MITRE ATT&CK
TA0043 – Reconnaissance
T1046 – Network Service Scanning
Notes
False positives may include vulnerability scanners. Asset context should be applied.
