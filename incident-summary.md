## Incident Summary — Attempted Lateral Movement (Blocked)

### What Happened
Internal reconnaissance activity was detected, followed by the creation
of a local administrator account.

Subsequent lateral movement attempts over SMB were blocked by host-based
and network firewall controls.

### Impact
- No authentication to remote hosts
- No lateral spread
- No persistence achieved

### Detection Signals
- Network port scan activity
- Local admin account creation
- Blocked SMB (TCP/445) traffic

### Outcome
Incident classified as:
**Attempted Lateral Movement — Prevented**

### SOC Disposition
Closed as **Contained / No Impact**
