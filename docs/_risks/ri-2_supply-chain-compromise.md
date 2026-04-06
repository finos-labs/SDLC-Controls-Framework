---
sequence: 2
title: Supply Chain Compromise
layout: risk
doc-status: Draft
type: SEC
nist-sp-800-53r5_references:
  - sr-3   # SR-3 Supply Chain Controls and Processes (primary)
  - sr-4   # SR-4 Provenance (primary)
  - sa-9   # SA-9 External System Services (supporting)
ffiec-itbooklets_references:
  - dam-4  # DAM: IV Common Development, Acquisition, and Maintenance Risk Topics (primary)
  - ots-2  # OTS: Risk Management (primary)
  - sec-3  # SEC: III Security Operations (supporting)
related_risks:
  - ri-1   # Insider Threat
  - ri-4   # Vulnerable Software in Production
  - ri-8   # Unauthorised Change
---

## Summary

Malicious or tampered software components — including open source libraries, base container images, build tools, or third-party services — enter the software development lifecycle, resulting in compromised applications being built, tested, and deployed to production environments.

## Description

Unlike direct attacks on an organisation's own systems, supply chain attacks exploit the inherent trust placed in third-party software, making them particularly difficult to detect. A single compromised upstream component can propagate malicious code to thousands of downstream consumers before the compromise is discovered. While the resulting artefacts may contain known vulnerabilities (ri-4), the distinguishing characteristic of supply chain compromise is the deliberate introduction of malicious or tampered components at the point of origin or distribution.

- **Compromised open source dependencies** — Malicious code injected into widely-used libraries via maintainer account takeover, typosquatting, or dependency confusion attacks
- **Tampered base images** — Container base images or VM images modified to include backdoors, credential harvesters, or persistent malware
- **Build toolchain compromise** — Compilers, build systems, or CI/CD tools altered to inject malicious code during the build process without modifying source
- **Third-party service compromise** — SaaS tools, package registries, or external APIs used in the pipeline becoming vectors for malicious payloads
- **Malicious package substitution** — Attackers publishing packages that mimic legitimate internal or popular public packages to exploit misconfigured dependency resolution

### Consequences

* **Undetected backdoors in production** — Malicious code embedded in trusted components can persist in production systems for extended periods, providing attackers with persistent access to sensitive systems, transaction data, and customer information.
* **Breach of data privacy regulations** — Exfiltration of customer PII or financial data through a compromised dependency can trigger GDPR, CCPA, and GLBA breach notification obligations, significant fines, and regulatory investigations.
* **Violation of financial regulations** — Compromised software integrity undermines audit trails and system controls required by SOX Section 404, PCI DSS, DORA, and FFIEC supervisory expectations, potentially resulting in enforcement actions and mandatory remediation programs.
* **Reputational damage** — Disclosure that customer-facing systems were built on compromised components — particularly if customer funds or data were affected — can severely damage institutional trust and trigger customer attrition.
* **Operational disruption** — Discovery of a supply chain compromise may require emergency takedown of affected systems, emergency patching across the estate, or full rebuilds of the software delivery pipeline, causing significant service disruption.
* **Widespread blast radius** — Because supply chain compromises affect the build process itself, all applications built using the affected component or toolchain may be impacted simultaneously, amplifying the scope of incident response.
* **Legal liabilities** — Customers, partners, or regulators may pursue legal action if compromised software led to financial losses, data breaches, or failure to meet contractual security obligations.

## Links
