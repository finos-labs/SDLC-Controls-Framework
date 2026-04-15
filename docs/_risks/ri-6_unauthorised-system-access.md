---
sequence: 6
title: Unauthorised System Access
layout: risk
doc-status: Draft
type: SEC
nist-sp-800-53r5_references:
  - id: ac-2
    note: Account Management (primary)
  - id: ac-3
    note: Access Enforcement (primary)
  - id: ac-6
    note: Least Privilege (primary)
  - id: ia-2
    note: Identification and Authentication (primary)
  - id: ac-17
    note: Remote Access (supporting)
related_risks:
  - ri-1   # Insider Threat
  - ri-3   # Credential and Secret Exposure
  - ri-9   # Environment Breach
---

## Summary

Individuals gain access to production environments, infrastructure, or sensitive systems without appropriate authorisation or without their access being fully recorded and auditable, undermining accountability, enabling data theft, and creating undetectable pathways for compromise.

## Description

Unlike insider threat (ri-1), which focuses on the actions of authorised personnel, this risk focuses on access governance — the granting, scoping, and auditing of access itself. It includes scenarios where access controls are too broad, where former employees or contractors retain active credentials, where shared accounts obscure individual accountability, or where privileged access is granted without time-bound restrictions or proper justification. The risk extends to both external attackers who exploit weak access controls and internal personnel whose access exceeds their legitimate operational needs.

- **Overprivileged access** — Users or service accounts granted broader permissions than required for their role, providing unnecessary access to sensitive systems, data, or infrastructure
- **Stale access credentials** — Former employees, contractors, or rotated team members retaining active access to production systems after their need for access has ended
- **Shared and generic accounts** — Use of shared credentials or service accounts that obscure which individual performed a given action, undermining accountability and audit trails
- **Insufficient access logging** — Systems that do not record who accessed what, when, and from where, making it impossible to detect or investigate unauthorised access
- **Lack of time-bound or just-in-time access** — Persistent privileged access that remains active indefinitely rather than being granted on-demand for specific, justified operational needs

### Consequences

* **Data breach and exfiltration** — Unauthorised access to production databases, customer records, or internal systems enables theft of sensitive financial data, PII, and intellectual property.
* **Fraudulent transactions** — Access to transaction processing systems, payment infrastructure, or account management tools can be exploited to initiate unauthorised transfers, manipulate account balances, or conduct fraudulent activities.
* **Regulatory violations** — Financial regulators require strict access controls and audit trails for production systems. Inadequate access governance violates requirements under SOX Section 404, PCI DSS Requirement 7, DORA Article 9, and the GLBA Safeguards Rule, triggering enforcement actions.
* **Loss of accountability** — Shared accounts and insufficient logging make it impossible to attribute actions to specific individuals, undermining incident investigation, forensic analysis, and regulatory reporting obligations.
* **Lateral movement by attackers** — Overly broad access permissions enable attackers who compromise a single account to move laterally across the environment, escalating from low-value systems to critical infrastructure.
* **Reputational damage** — Disclosure that customer data or financial systems were accessed by unauthorised individuals — particularly through preventable access control failures — severely erodes customer trust and market confidence.
* **Prolonged undetected compromise** — Without comprehensive access logging and monitoring, unauthorised access can persist undetected for extended periods, increasing the scope and severity of potential damage.

## Links
