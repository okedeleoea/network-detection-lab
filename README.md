⚠️ This repository has been archived.

This project evolved into:
➡️ soc-detection-engineering-lifecycle-lab

🚨 Network Detection Lab
## Background Context

This detection lab builds on reconnaissance and discovery activity documented in:

👉 **network-discovery-lab**  
https://github.com/okedeleoea/network-discovery-lab

The focus here is SIEM-first alerting, triage, investigation, and incident reporting.

📌 Overview

This lab demonstrates how a Security Operations Center (SOC) detects, investigates, and documents internal reconnaissance and attempted abuse activity using SIEM-style detection logic and investigation workflows.

The focus is detection, correlation, and incident response documentation — not exploitation.

This project builds directly on findings from the network-discovery phase and shows how those activities are translated into actionable detections, incident reports, and improvement plans.

🎯 Objectives

Detect internal network discovery activity

Identify unauthorized privileged account creation

Validate firewall controls blocking SMB lateral movement

Investigate attempted (but failed) credential abuse

Document a SOC-style incident response

Identify detection gaps and detection maturity level

🧪 Lab Environment
Component	Details
Analyst / Attacker	Kali Linux
Target Host	Windows workstation
Logs Reviewed	Network traffic, Windows Security Events
SIEM	Elastic-style KQL (conceptual, production-aligned)
Scope	Detection, investigation, documentation

⚠️ No successful exploitation, persistence, or lateral movement occurred.

🔍 Attack & Detection Summary 

Internal network scanning and service discovery

Unauthorized local user account created

Attempted credential abuse via scheduled task

Task creation failed

Attempted SMB-based lateral movement

TCP/445 blocked by firewall

Outcome

No authentication success

No persistence achieved

No lateral spread

🛡️ Detection Capabilities Demonstrated
1️⃣ Network Discovery Detection

Identification of port scanning behavior

Correlation of multiple destination ports

2️⃣ Privileged Account Monitoring

Detection of local user creation

Identification of administrator group modification

3️⃣ Credential Abuse (Attempted)

Review of failed scheduled task creation

Investigation of misuse attempts without execution

4️⃣ Lateral Movement Prevention

Validation of blocked SMB traffic (TCP/445)

Confirmation of firewall effectiveness

📊 SIEM Detection Logic (Conceptual)
Elastic KQL – Blocked SMB Attempt
network.transport : "tcp" and
destination.port : 445 and
event.action : ("DROP", "BLOCK")


Detection logic is conceptual, written to reflect how Elastic Security detections are authored in production SOCs.

🚨 Incident Outcome
Attribute	Value
Impact	None
Status	Contained
Severity	Low–Medium
Root Cause	Unauthorized local account creation attempt
Lateral Movement	Prevented
📉 Detection Gap Analysis

Identified gaps during investigation:

❌ No alert on failed scheduled task creation

❌ No behavioral detection for service account misuse

❌ Limited visibility into blocked authentication attempts

⚠️ Correlation required manual analysis

These gaps directly inform future detection engineering and automation efforts.

📈 Detection Maturity Assessment
Area	Maturity
Reconnaissance Detection	🟡 Basic
Privileged Account Monitoring	🟡 Partial
Credential Abuse Detection	🔴 Weak
Lateral Movement Prevention	🟢 Strong
Automated Correlation	🔴 Not Implemented
🧠 Lessons Learned

Failed attacks provide valuable detection signals

SOC visibility must include attempted abuse, not just success

Preventive controls are strongest when paired with detection

Detection gaps are actionable roadmap items, not failures

🧩 MITRE ATT&CK Mapping (Partial / Prevented)

TA0043 – Reconnaissance

T1046 – Network Service Scanning

TA0006 – Credential Access (Attempted)

Failed scheduled task execution

TA0008 – Lateral Movement (Prevented)

T1021.002 – SMB / Admin Shares

📂 Repository Structure
network-detection-lab/
├── README.md
├── incident-report.md          # Formal SOC incident report
├── detection-gap-analysis.md   # Identified detection weaknesses
├── detection-maturity.md       # SOC maturity assessment
├── detections/                 # KQL / detection logic examples
└── remediation.md              # Detection & hardening recommendations

🧠 Background Context

This lab builds on hands-on training from:

Google Cybersecurity Professional Certificate

Google Cloud Cybersecurity Certificate

IBM Cybersecurity Case Studies

Google Security Operations (Chronicle)

Focus: Translating theory into observable detections, investigations, and SOC-ready documentation.

