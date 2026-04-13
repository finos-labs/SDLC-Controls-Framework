---
sequence: 1
title: Runtime Operations
layout: risk
doc-status: draft
type: RC
owasp-llm_references:
  - llm02-2025  # LLM02:2025 Sensitive Information Disclosure
nist-ai-600-1_references:
  - 2-4  # 2.4. Data Privacy
  - 2-9  # 2.9. Information Security
ffiec-itbooklets_references:
  - sec-2  # SEC: II Information Security Program Management
  - sec-3  # SEC: III Security Operations
  - ots-2  # OTS: Risk Management
eu-ai-act_references:
  - c3-s2-a10  # III.S2.A10: Data and Data Governance
  - c3-s2-a13  # III.S2.A13: Transparency and Provision of Information to Deployers
  - c5-s2-a53  # V.S2.A53: Obligations for Providers of General-Purpose AI Models
related_risks:
  - ri-2   # Information Leaked to Vector Store
  - ri-23  # Intellectual Property and Copyright
---
## Summary

State of runtime support documentation is out of risk with the current runtime environment. This creates a growing operational risk of increased MTTR.

## Description

One of the outcomes of a successful SDLC is maintaining runbooks, telemetry, production tests, synthetic tests, etc.


Examples


### Consequences




* **Complicated incident response** — When the actual state of systems is unknown or differs from documentation, incident responders cannot reliably assess the scope of a compromise or determine whether specific controls were in place at the time of an incident.
* **Increased operational risk** — Teams making changes based on stale documentation or incorrect assumptions about the current environment are more likely to cause outages, introduce conflicts, or break dependent services. Increased MTTR.
* **Erosion of trust in automation** — When manual changes routinely override automated configuration management, teams lose confidence in infrastructure-as-code processes, leading to a cycle of increasing manual intervention and further drift.

* **Financial Losses:** Fraudulent transactions, theft of funds, unauthorized wire transfers, or manipulation of accounts can result in immediate monetary losses to the institution and its customers.

* **Breach of Data Privacy Regulations:** Unauthorized access to or exfiltration of customer PII can lead to significant fines under regulations like GDPR, CCPA, and GLBA, alongside mandated breach notifications and regulatory scrutiny.

* **Violation of Financial Regulations:** Insider actions compromising system integrity, audit trails, or customer data can breach banking regulations (e.g., SOX, PCI DSS, Basel III) and trigger enforcement actions from regulatory bodies.

* **Reputational Damage:** Public disclosure of insider attacks—particularly those involving customer funds or data—can severely erode customer trust, leading to account closures, deposit flight, and long-term brand damage.


---

Does this capture the right scope and tone for your risk register?

## Links

- [FFIEC IT Handbook](https://ithandbook.ffiec.gov/)
