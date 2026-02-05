## 7️⃣ Blocked SMB Detection (Elastic KQL)

`detections/blocked-smb-detection.md`

```md
## Detection: Blocked SMB Connection Attempt

### Description
Detects attempted SMB connections that were blocked by firewall controls.

### Elastic KQL
```kql
network.transport: "tcp" and
destination.port: 445 and
event.action: ("DROP", "BLOCK", "DENY")
```

MITRE ATT&CK
TA0008 – Lateral Movement
T1021.002 – SMB (Attempted)
Analyst Notes
A blocked connection is still a high-signal event when correlated with reconnaissance or privilege escalation.
