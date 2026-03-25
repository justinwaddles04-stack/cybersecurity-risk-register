# Cybersecurity Risk Register
### Healthcare Scenario | GRC Portfolio Project

---

## Scenario

Midwest Regional Health Network is a fictional 1,200-employee healthcare provider 
operating across three hospital campuses in Indiana. The organization processes 
protected health information (PHI) for approximately 85,000 active patients and 
is subject to HIPAA Security Rule requirements.

I was brought in as a GRC analyst to build a structured risk register from scratch — 
identifying the organization's key cybersecurity risks, evaluating them against 
existing controls, and producing a prioritized mitigation roadmap for leadership.

---

## What I Did

Using a likelihood × impact scoring methodology aligned with NIST CSF principles, 
I identified and assessed 8 risks across the organization's people, processes, 
and technology. For each risk I documented the threat scenario, the existing control 
environment, control gaps, and a specific mitigation recommendation.

The accompanying Python script (`risk_calculator.py`) automates risk scoring and 
classifies each risk as Low, Medium, or High — the kind of lightweight tooling a 
small GRC team would actually use before investing in a full GRC platform.

---

## Key Findings

**Credential compromise and MFA gaps were the highest-priority finding.** 
Clinical staff access to the EHR system lacked MFA enforcement, creating direct 
exposure to PHI in the event of a phishing-driven credential theft — which is 
the most common HIPAA breach vector in healthcare.

**Third-party vendor risk was systematically unmanaged.** The organization had 
no formal vendor risk assessment process despite relying on 12+ external vendors 
with varying levels of PHI access. This represents both a HIPAA Business Associate 
Agreement compliance gap and a material operational risk.

**Patch management delays were creating compounding exposure.** Unpatched systems 
combined with excessive user permissions meant that a single compromised endpoint 
had a realistic path to lateral movement across clinical systems.

---

## My Recommendations (Priority Order)

1. **Enforce MFA on all EHR and PHI-adjacent systems within 30 days** — this is 
the highest-impact, lowest-cost control available and directly addresses the 
organization's most likely breach scenario.

2. **Establish a vendor risk tiering process** — classify all vendors by PHI 
access level and require security questionnaires from Tier 1 vendors within 
90 days. This closes the BAA compliance gap before it becomes a regulatory issue.

3. **Implement a formal patch management policy with defined SLAs** — critical 
patches within 72 hours, high within 14 days. Pair with quarterly access reviews 
to reduce the lateral movement risk from over-permissioned accounts.

---

## Files

| File | Description |
|------|-------------|
| `Cybersecurity_Risk_Register.xlsx` | Full risk register with scoring, controls mapping, and mitigation strategies |
| `risk_register.csv` | Underlying dataset used for analysis and script input |
| `risk_calculator.py` | Python script that calculates risk scores and classifies risks by severity |
| `risk-register-screenshot.PNG` | Visual snapshot of the completed register |

---

## Frameworks Referenced

- **NIST Cybersecurity Framework (CSF)** — risk categorization by function 
(Identify, Protect, Detect, Respond, Recover)
- **HIPAA Security Rule** — regulatory lens for PHI-related risks and controls
- **Risk Scoring** — Likelihood × Impact (1–3 scale), producing Low / Medium / High 
classifications

---

*This is a fictional scenario created for portfolio purposes. 
No real patient data or organizational information was used.*
