---
sequence: 5
title: Secret Management
layout: controls
doc-status: Approved-Specification
type: PREV
iso-42001_references:
  - A-8-1  # ISO/IEC 42001 – Management of sensitive data
  - A-8-2  # ISO/IEC 42001 – Cryptographic key management
  - A‑6‑2‑3  # ISO/IEC 42001: Access control for sensitive systems
  - A.9.1  # ISO/IEC 27001 Access control policy
nist-sp-800-53r5_references:
  - ac-2  # AC-2 – Account Management
  - ac-3  # AC-3 – Access Enforcement
  - ia-5  # IA-5 – Authenticator Management
  - sc-12  # SC-12 – Cryptographic Key Establishment and Management
  - cm-6  # CM-6 – Configuration Settings

mitigates:
  - ri-11   # Insider Threat
  - ri-12   # Credential and secret exposure
  - ri-13  # Unauthorized system access
---

**Secret Management**

## Summary
Build and runtime secrets are stored securely on organization approved tools and documented appropriately

## Description
This control provides a framework for managing sensitive application secrets throughout their lifecycle. It ensures that credentials, keys, and other confidential information are handled in a secure and consistent manner, reducing the risk of unauthorized access or exposure. By promoting centralized management, controlled access, and ongoing monitoring, the control helps organizations maintain the confidentiality and integrity of critical information while supporting compliance with security and regulatory standards.

## Requirements
* All application secrets (including API keys, credentials, certificates, and tokens) are centrally managed using an approved secrets management solution.
* Secrets are encrypted at rest and in transit.
* Secrets are never hardcoded in source code or configuration files.
* Access is enforced through role-based, least-privilege controls.
* All access to secrets is logged and continuously monitored.
* Automated rotation and revocation processes are implemented.
* Audit capabilities are maintained to support security best practices and regulatory compliance requirements.

## Examples & Commentary
* **Centralized vault storage** Using tools like HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault to store API keys, database passwords, certificates, and tokens.
* **Environment-Specific Secrets** Separate secrets for development, testing, and production environments.Each environment has unique credentials to prevent accidental exposure.
* **Encryption of Secrets** Secrets are encrypted at rest (stored securely) and in transit (sent securely over networks).Often done with AES-256 or other industry-standard cryptography.
* **Access Controls** Implement least-privilege access: only services or users that need a secret can access it.FOr instance, a web app can read a database password but cannot access encryption master keys.
* **Integration with CI/CD** CI/CD pipelines retrieve secrets dynamically from a vault during builds/deployments, rather than embedding credentials in scripts.

## Links

- OWASP - https://owasp.org/Top10/2021/A02_2021-Cryptographic_Failures/index.html


---
