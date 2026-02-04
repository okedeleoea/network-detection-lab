# Network Detection Lab (SIEM-First, Alert-Driven)

## Overview
This repository demonstrates **SOC detection engineering** focused on
network-based threat detection using SIEM logic — without executing exploitation.

The lab simulates how a SOC detects:
- Internal reconnaissance
- Blocked lateral movement attempts
- Credential abuse indicators
- Multi-signal correlation

This mirrors real-world SOC operations where **prevention succeeds, but detection still matters**.


## Scope & Philosophy
- **No exploitation**
- **No payload execution**
- **Detection-first**
- **Alert accuracy over attack success**

All detections are written as if logs are already flowing into a SIEM
(e.g., Elastic Security, Splunk, Chronicle).


## Detection Use Cases
- TCP port scanning
- Blocked SMB (TCP/445) connection attempts
- Credential abuse indicators (account creation, admin access)
- Correlation of recon + privilege events


## MITRE ATT&CK Coverage (Accurate)
| Tactic | Technique |
|------|----------|
| Reconnaissance | T1046 – Network Service Scanning |
| Credential Access | T1078 – Valid Accounts |
| Lateral Movement | T1021.002 – SMB (Attempted, Blocked) |


## Repository Contents
- `detections/` – SIEM detection logic (KQL/EQL)
- `incident-summary.md` – SOC-style incident report
- `detection-maturity.md` – Detection maturity assessment
- `detection-gap-analysis.md` – Known gaps and future improvements


## Outcome
No lateral movement occurred.  
Security controls functioned correctly.  
**Detection and correlation provided visibility and assurance.**


