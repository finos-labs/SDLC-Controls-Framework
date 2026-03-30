---
sequence: 5
title: Audit and Compliance Failure
layout: risk
doc-status: Draft
type: RC
nist-sp-800-53r5_references:
  - au-2   # AU-2 Event Logging (primary)
  - au-6   # AU-6 Audit Record Review, Analysis, and Reporting (primary)
  - ca-7   # CA-7 Continuous Monitoring (supporting)
ffiec-itbooklets_references:
  - aud-3  # AUD: III Internal Audit Program (primary)
  - aud-4  # AUD: IV Risk Assessment and Risk-Based Auditing (primary)
  - mgt-2  # MGT: II Risk Management (supporting)
related_risks:
  - ri-7   # Configuration Drift
  - ri-8   # Unauthorised Change
---

## Summary

An organisation cannot produce sufficient evidence that its software development and operational controls are functioning as intended, creating exposure to regulatory enforcement actions, failed customer audits, and loss of certifications essential to operating in financial services.

## Description

This risk is not about the absence of controls themselves, but about the inability to demonstrate their existence and effectiveness to regulators, auditors, or enterprise customers. It arises from gaps in record-keeping, inconsistent control enforcement, lack of traceability between changes and approvals, or reliance on manual processes that leave insufficient audit trails. In regulated industries, the burden of proof lies with the organisation — controls that cannot be evidenced are treated as controls that do not exist.

- **Gaps in change records** — Missing or incomplete records linking code changes to reviews, approvals, and deployments, making it impossible to reconstruct the history of what was deployed and why
- **Inconsistent control enforcement** — Controls that are sometimes applied and sometimes bypassed, producing an unreliable evidence trail that fails to satisfy audit requirements
- **Manual and undocumented processes** — Reliance on informal approvals, verbal sign-offs, or manual steps that leave no verifiable record of compliance
- **Fragmented tooling and evidence** — Compliance evidence scattered across disconnected systems (ticketing tools, CI/CD logs, email threads) with no unified view or correlation
- **Inability to demonstrate continuous compliance** — Point-in-time evidence that does not show ongoing adherence to controls between audit periods

### Consequences

* **Regulatory enforcement actions** — Failure to demonstrate effective controls to banking regulators can result in formal enforcement actions, restrictions on business activities, increased supervisory scrutiny, and mandated remediation programs.
* **Financial penalties** — Regulators can impose significant fines for non-compliance with SOX, PCI DSS, DORA, and other applicable frameworks, with penalties scaling based on the severity and duration of compliance gaps.
* **Loss of licences and certifications** — Sustained inability to evidence controls can jeopardise banking licences, payment processing certifications (PCI DSS), and other authorisations essential to operating in financial services.
* **Failed customer and partner audits** — Enterprise customers and partners increasingly require evidence of SDLC controls as part of vendor due diligence. Audit failures can result in lost contracts, exclusion from procurement processes, and damage to commercial relationships.
* **Increased audit costs** — Organisations that cannot efficiently produce compliance evidence face prolonged audit cycles, higher audit fees, and the need for expensive remediation efforts to reconstruct missing evidence.
* **Reputational damage** — Public disclosure of regulatory enforcement actions or compliance failures signals poor governance to customers, partners, and the market, potentially impacting share price and customer confidence.
* **Operational burden** — Reactive compliance — scrambling to produce evidence in response to audit requests — diverts engineering and management resources from productive work and creates a cycle of perpetual catch-up.

## Links
