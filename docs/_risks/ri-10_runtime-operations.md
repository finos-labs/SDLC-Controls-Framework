---
sequence: 1
title: Runtime Operations
layout: risk
doc-status: draft
type: RC
nist-sp-800-53r5_references:
    cp-2 # CP-2 Contingency Plan (primary)
    cp-10 # CP-10 System Recovery and Reconstitution (primary)
    si-4 # SI-4 System Monitoring (primary)
    au-6 # AU-6 Audit Record Review, Analysis, and Reporting (supporting)
    ca-7 # CA-7 Continuous Monitoring (supporting)
ffiec-itbooklets_references:
    aio-6 # AIO: VI Operations (primary)
    aio-11 # AIO: XI Business Continuity Management (supporting)
related_risks:
    ri-7 # Configuration Drift

---
## Summary

State of runtime support documentation is out of risk with the current runtime environment. This creates a growing operational risk of increased MTTR. Focuses on how systems are operated compared to how systems are defined (i.e. config drift.)

## Description

One of the outcomes of a successful SDLC is maintaining runbooks, telemetry, production tests, synthetic tests, etc.

- Manual production changes — Ad hoc modifications applied directly to production infrastructure or application configuration outside the standard change management process
- Not updating observability systems for new features and services.
- Runbook drift. Particularly when they manually maintained, and separate from the code.


### Examples
- Delays in resolving incidents, and further outages.

### Consequences


* **Complicated incident response** — When the actual state of systems is unknown or differs from documentation, incident responders cannot reliably assess the scope of a compromise or determine whether specific controls were in place at the time of an incident.
* **Increased operational risk** — Teams making changes based on stale documentation or incorrect assumptions about the current environment are more likely to cause outages, introduce conflicts, or break dependent services. Increased MTTR.

* **Financial Losses:** Fraudulent transactions, theft of funds, unauthorized wire transfers, or manipulation of accounts can result in immediate monetary losses to the institution and its customers.

* **Breach of Data Privacy Regulations:** Unauthorized access to or exfiltration of customer PII can lead to significant fines under regulations like GDPR, CCPA, and GLBA, alongside mandated breach notifications and regulatory scrutiny.

* **Violation of Financial Regulations:** Insider actions compromising system integrity, audit trails, or customer data can breach banking regulations (e.g., SOX, PCI DSS, Basel III) and trigger enforcement actions from regulatory bodies.

* **Reputational Damage:** Public disclosure of insider attacks—particularly those involving customer funds or data—can severely erode customer trust, leading to account closures, deposit flight, and long-term brand damage.


---

Does this capture the right scope and tone for your risk register?

## Links

- [FFIEC IT Handbook](https://ithandbook.ffiec.gov/)
