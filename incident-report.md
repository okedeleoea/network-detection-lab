Incident Report: Internal Network Discovery Activity
1. Executive Summary
An internal network discovery activity was detected originating from a non-authorized host within the internal network. The activity included network scanning, service enumeration, and unauthorized local user account creation.
An attempted privilege abuse via scheduled task creation was observed but failed, and no lateral movement occurred. Preventive firewall controls successfully blocked SMB-based access attempts.
The incident was contained with no business impact.
Severity: Low–Medium
Status: Contained
Impact: None
2. Incident Overview
Field
Value
Incident Type
Internal Reconnaissance
Detection Category
Network Discovery / Credential Abuse Attempt
Environment
Simulated Enterprise Network
Affected Systems
Single Windows Host
Lateral Movement
Not achieved
Data Exfiltration
None
3. Timeline of Events
Time (Relative)
Event
T0
Network scanning activity detected (multi-port probing)
T1
Service enumeration observed on target host
T2
Unauthorized local user account created
T3
Scheduled task creation attempted (failed)
T4
SMB connection attempts blocked by firewall
T5
Activity ceased; incident confirmed contained
4. Detection & Alert Sources
The incident was identified through a combination of log analysis and behavioral indicators:
Network logs indicating horizontal port scanning
Windows Security Events showing local user account creation
System logs revealing failed scheduled task creation
Firewall logs confirming blocked SMB traffic (TCP/445)
Detection logic was modeled using Elastic-style KQL for conceptual SIEM correlation.
5. Investigation Findings
Key Observations
The attacker demonstrated reconnaissance intent, not persistence.
Unauthorized account creation suggested an attempt to establish local access.
Scheduled task creation failed due to insufficient privileges.
SMB traffic was effectively blocked, preventing lateral movement.
What Did NOT Occur
No credential dumping
No successful privilege escalation
No remote command execution
No lateral spread to additional hosts
6. Impact Assessment
Area
Impact
Availability
None
Integrity
None
Confidentiality
None
Business Operations
Unaffected
This incident remained in the reconnaissance and failed execution phase.
7. Response Actions Taken
Confirmed unauthorized account creation
Verified firewall enforcement blocking SMB traffic
Reviewed scheduled task failure logs
Documented detection gaps and improvement opportunities
Classified incident as contained
No eradication or recovery actions were required due to lack of persistence.
8. Detection Gaps Identified
No alert specifically triggered for failed scheduled task creation
Service account creation lacked behavioral correlation with prior scanning
Firewall block events were not automatically linked to reconnaissance activity
9. Recommendations
Add detection rules for repeated task creation failures
Correlate account creation with prior network scanning activity
Include firewall block logs in attack chain correlation
Apply least-privilege controls on local account creation
10. Lessons Learned
Failed attacks still provide valuable detection signals
Preventive controls are effective but must be paired with alerting
SOC visibility should include attempted abuse, not only successful compromise
Early-stage detection prevents escalation
Final Incident Status: Closed – Contained
Prepared by: SOC Analyst (Lab Simulation)
