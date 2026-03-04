---
sequence: 4
title: Automated Security Scanning
layout: mitigation
doc-status: Draft
type: PREV
nist-sp-800-53r5_references:
  - ra-5   # RA-5 Vulnerability Monitoring And Scanning
  - sa-11  # SA-11 Developer Testing And Evaluation
  - sa-15  # SA-15 Development Process, Standards, And Tools
  - si-2   # SI-2 Flaw Remediation
mitigates:
related_mitigations:
  - mi-5   # Vulnerability Scanning - SAST
  - mi-6   # Vulnerability Scanning - DAST
  - mi-7   # Vulnerability Scanning - Dependencies
  - mi-10  # Secret Detection
  - mi-11  # Vulnerability Remediation SLAs
  - mi-12  # Deployment Gating
---

## Summary

Automated security scanning is integrated into the software development lifecycle to identify vulnerabilities, weaknesses, and exposures before software is deployed.

## Description

Automated security scanning is the practice of using tooling to detect security vulnerabilities in software as it is developed, built, and deployed. By embedding scanning into the development workflow and CI/CD pipeline, organisations gain continuous visibility into the security posture of their applications and can address issues early — when remediation is fastest and cheapest.

Common scanning techniques include static application security testing (SAST), dynamic application security testing (DAST), software composition analysis (SCA) for dependencies, and secret detection — each addressed in a dedicated control within this framework. The appropriate combination of techniques will vary depending on application architecture, technology stack, risk profile, and regulatory context.

## Requirements

* Automated security scanning MUST be integrated into the software development lifecycle
* The scanning programme MUST be appropriate to the organisation's application portfolio, covering the types of vulnerabilities and exposures relevant to their technology stack, architecture, and deployment model
* Scanning MUST be automated and integrated into development workflows and CI/CD pipelines — manual-only assessment processes are not sufficient as a primary control
* Scan results MUST be classified by severity and tracked to resolution
* The scanning programme MUST be documented, including the rationale for the scanning techniques selected, the tools in use, what is scanned, scan frequency, and how findings are managed
* The scanning programme MUST be reviewed at least annually — or when significant changes to the technology stack, application portfolio, or threat landscape occur — to ensure continued appropriateness and effectiveness

## Examples & Commentary

* **Risk-Based Selection:** An organisation running primarily web applications and APIs might prioritise SAST and DAST, while an organisation heavily reliant on open-source components might prioritise dependency scanning. The key is that the selection is deliberate, documented, and proportionate to risk
* **Pipeline Integration:** Scanning should be embedded into the CI/CD pipeline so that developers receive security feedback in the same workflow where they receive build and test results, rather than through a separate process that runs on a different cadence
* **Centralised Visibility:** Aggregate findings from all scanning tools into a single view to enable prioritisation, trend analysis, and compliance reporting. Track metrics such as mean-time-to-remediate and finding density to measure programme effectiveness
* **Incremental Maturity:** Organisations do not need to implement every scanning technique simultaneously. Starting with the highest-value scanning approach for the application portfolio and expanding coverage over time is a practical path — provided the rationale is documented and the programme is reviewed regularly
* **Complementing Manual Review:** Automated scanning complements but does not replace manual security activities such as peer code review, threat modelling, and penetration testing. Scanning provides breadth and consistency; manual activities provide depth and contextual judgement

## Links

- [NIST SP 800-53r5 RA-5: Vulnerability Monitoring and Scanning](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/)
- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final)
- [FFIEC IT Handbook - Information Security](https://ithandbook.ffiec.gov/)
