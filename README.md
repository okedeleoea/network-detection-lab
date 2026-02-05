# Network Discovery Lab (SOC Detection Focus)

## Overview
This lab demonstrates how a SOC detects and investigates internal network discovery activity and validates defensive controls that prevent lateral movement.

The focus is on detection logic, investigation workflow, and incident documentation — not exploitation.

## Objectives
- Detect internal network discovery activity
- Analyze service enumeration behavior
- Validate firewall controls blocking SMB
- Document a SOC-style incident response
- Identify detection gaps and improvement areas

## Lab Environment
- Kali Linux (simulated attacker)
- Windows host (target)
- Logs: Network + Windows Security Events
- SIEM: Detection logic written in Elastic-style KQL (conceptual)

## Attack Simulation Summary 
1. Internal network scanning and service discovery
2. Unauthorized local user account created
3. Attempted credential abuse via scheduled task **failed**
4. SMB-based lateral movement **blocked by firewall**
5. No lateral spread occurred

## Detection Summary
- Port scan detection using Python
- Identification of privileged account creation
- Validation of blocked SMB traffic (TCP/445)
- Incident confirmed as **contained**

## Incident Outcome
- Impact: None
- Status: Contained
- Severity: Low–Medium
- Root cause: Insecure local account creation

## Detection Gaps Identified
- No alert on failed scheduled task creation
- No behavioral alert for service account misuse
- Limited visibility into blocked authentication attempts

## Lessons Learned
- Preventive controls are effective when paired with visibility
- Failed attacks still provide valuable detection signals
- Detection coverage should include **failed abuse**, not just success

## Repository Contents
- analysis.md — scan findings
- investigation-timeline.md — SOC investigation steps
- remediation.md — hardening recommendations
- elastic-detection.md — detection logic examples
- soar-playbook.md — response workflow

## Background Context
This lab builds on foundational training from:
- Google Cybersecurity Professional Certificate
- Google Cloud Cybersecurity Certificate
- IBM Cybersecurity Case Studies
- Google Security Operations (Chronicle)

Focus: translating theory into **observable detections and controls**.
