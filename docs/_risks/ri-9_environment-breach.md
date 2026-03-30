---
sequence: 9
title: Environment Breach
layout: risk
doc-status: Draft
type: SEC
nist-sp-800-53r5_references:
  - si-4   # SI-4 System Monitoring (primary)
  - ir-4   # IR-4 Incident Handling (primary)
  - sc-7   # SC-7 Boundary Protection (primary)
ffiec-itbooklets_references:
  - sec-3  # SEC: III Security Operations (primary)
  - aio-3  # AIO: III Common AIO Risk Management Topics (supporting)
related_risks:
  - ri-2   # Supply Chain Compromise
  - ri-4   # Vulnerable Software in Production
  - ri-6   # Unauthorised System Access
---

## Summary

An external attacker gains the ability to run unauthorised workloads within an organisation's production infrastructure, establishing a persistent operational presence that enables data theft, resource abuse, and lateral movement across internal systems.

## Description

While unauthorised system access (ri-6) concerns access governance failures, environment breach describes a more severe state: the attacker has moved beyond access to achieve persistent execution capability within the production environment, running their own code alongside legitimate services. This can result from exploitation of vulnerabilities in exposed services, compromised container orchestration platforms, misconfigured cloud IAM policies, or abuse of legitimate deployment mechanisms. The attacker operates within the organisation's own infrastructure, making detection significantly harder and the potential impact far greater.

- **Unauthorised container or workload deployment** — Attackers deploying their own containers, serverless functions, or processes within the organisation's orchestration platform (e.g., Kubernetes, ECS)
- **Compromised orchestration plane** — Exploitation of container orchestration APIs or management interfaces to schedule and run attacker-controlled workloads alongside legitimate services
- **Cryptojacking and resource abuse** — Attackers deploying cryptocurrency mining workloads or using compromised infrastructure for computational tasks, consuming resources and increasing costs
- **Staging ground for further attacks** — Using the breached environment as a launch point for lateral movement into other internal systems, data stores, or connected partner networks
- **Persistent backdoor deployment** — Installing persistent access mechanisms such as reverse shells, web shells, or rogue services that survive routine maintenance and restarts

### Consequences

* **Deep infrastructure access** — An attacker running workloads in production has broad access to the environment, potentially including network access to databases, internal APIs, secret stores, and adjacent systems that are not directly exposed to the internet.
* **Customer data theft at scale** — With operational presence in the production environment, attackers can systematically exfiltrate customer data, transaction records, and financial information over extended periods while evading perimeter-based detection.
* **Financial losses from resource abuse** — Unauthorised workloads — particularly cryptomining operations — can generate significant unexpected cloud computing costs before detection, directly impacting operational budgets.
* **Regulatory escalation** — An environment breach represents a fundamental control failure. Regulators will treat the ability of an external attacker to run workloads in a financial institution's production environment as a critical finding, triggering mandatory incident reporting under DORA Article 17, PCI DSS Requirement 12.10, and GLBA breach notification obligations.
* **Supply chain risk to customers** — Attacker-controlled workloads running within the institution's infrastructure can potentially intercept, modify, or inject data into legitimate business processes, affecting downstream customers and partners.
* **Prolonged and costly incident response** — Detecting and eradicating an attacker with operational presence requires thorough forensic investigation of all running workloads, comprehensive review of deployment history, and potentially rebuilding affected infrastructure from known-good state.
* **Severe reputational damage** — Disclosure that an external attacker was running their own workloads inside a financial institution's production environment represents a serious breach of trust that can significantly damage the institution's standing with customers, partners, and regulators.

## Links
