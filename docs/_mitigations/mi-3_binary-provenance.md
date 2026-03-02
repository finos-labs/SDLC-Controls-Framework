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

## Summary

Every internally built software artifact running in a production environment has known and verifiable provenance, establishing a documented chain of custody from source code commit through build and into deployment.

## Description

Binary provenance answers the question "where did this binary come from?" for any artifact at any time. Provenance records are created at build time and capture the source commit, repository state, build environment details, build log references, and the resulting artifact identity. These records are immutable once written and stored in a tamper-evident system that prevents retroactive modification.

By linking the cryptographic identity of an artifact (from content addressable identities) to its source and build metadata, binary provenance ensures that only artifacts built from known source code through authorized build processes reach production.

## Requirements

* Every production artifact MUST be traceable back to a specific source code commit, build process, and build environment
* Provenance records MUST be created at build time and be immutable once written
* Provenance records MUST include:
  * SHA-256 hash of the output artifact
  * Source git commit reference
  * Repository URL
  * Build log URL
  * Build environment identifier
  * Timestamp
* No artifact MAY be deployed to production without a corresponding provenance record
* Provenance records MUST be stored in a tamper-evident system that prevents retroactive modification

## Examples & Commentary

* Use a dedicated provenance store or attestation service to maintain build records independently of the CI/CD system
* Implement deployment gates that verify an artifact has a valid provenance record before allowing promotion to production environments
* Periodically audit provenance records against running deployments to confirm that all production artifacts have known origins
* Distinguish between human-friendly identifiers (semantic versioning, commit references) for navigation and cryptographic hashes for security and compliance purposes
