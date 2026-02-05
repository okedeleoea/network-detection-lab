## 8️⃣ Correlation Detection (Recon → Admin → Blocked SMB)

`detections/correlation-detection.md`

```md
## Detection: Reconnaissance Followed by Blocked Lateral Movement

### Description
Correlates multiple low-level detections into a high-confidence incident.

### Correlation Logic
Within 15 minutes:
- Port scan detected
- Local admin account created
- SMB connection attempt blocked

### SOC Value
- Reduces alert fatigue
- Confirms control effectiveness
- Elevates severity only when justified

### Outcome
Incident severity: **Medium**
Disposition: **Prevented**
