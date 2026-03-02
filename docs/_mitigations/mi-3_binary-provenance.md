---
sequence: 3
title: Binary Provenance
layout: mitigation
doc-status: Pre-Draft
type: PREV
nist-sp-800-53r5_references:
  - sa-10  # SA-10 Developer Configuration Management
  - sa-11  # SA-11 Developer Testing And Evaluation
  - cm-3   # CM-3 Configuration Change Control
  - si-7   # SI-7 Software, Firmware, And Information Integrity
  - au-10  # AU-10 Non-repudiation
mitigates:
  - ri-1  # Insider Threat
related_mitigations:
  - mi-2  # Content Addressable Identities
  - mi-1  # Peer Source Code Review
---

**Binary Provenance**

## Purpose
To ensure that every software artifact running in a production environment has known and verifiable provenance, establishing a documented chain of custody from source code commit through build and into deployment. This control enables organizations to answer the question "where did this binary come from?" for any artifact at any time.

## Key Principles
* Every production artifact must be traceable back to a specific source code commit, build process, and build environment
* Provenance records are created at build time and are immutable once written
* Provenance information includes the source commit, repository state, build environment details, build log references, and the resulting artifact identity
* No artifact may be deployed to production without a corresponding provenance record
* Provenance records are stored in a tamper-evident system that prevents retroactive modification

## Implementation Guidance
* Record the following for every official build: SHA-256 hash of the output artifact, source git commit reference, repository URL, build log URL, build environment identifier, and timestamp
* Use a dedicated provenance store or attestation service to maintain build records independently of the CI/CD system
* Implement deployment gates that verify an artifact has a valid provenance record before allowing promotion to production environments
* Ensure provenance records link the cryptographic identity of the artifact (from content addressable identities) to its source and build metadata
* Periodically audit provenance records against running deployments to confirm that all production artifacts have known origins

## Importance and Benefits
* **Insider Threat Mitigation:** Makes it extremely difficult for a malicious insider to introduce unauthorized binaries into production, as every artifact must have a verifiable build record
* **Supply Chain Security:** Ensures that only artifacts built from known source code through authorized build processes reach production
* **Incident Response:** Enables rapid identification of exactly what source code and dependencies produced any given production artifact during security investigations
* **Regulatory Compliance:** Provides the audit trail required by financial regulators to demonstrate control over what software is running in production systems
* **Deployment Confidence:** Guarantees that the artifact deployed is the same one that was tested and approved, eliminating risks from manual or ad-hoc artifact handling
