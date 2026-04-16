---
sequence: 2
title: Content Addressable Identities
layout: mitigation
doc-status: Draft
type: PREV
nist-sp-800-53r5_references:
  - si-7   # SI-7 Software, Firmware, And Information Integrity
  - sa-10  # SA-10 Developer Configuration Management
  - au-10  # AU-10 Non-repudiation
mitigates:
  - ri-1   # Insider Threat
  - ri-7   # Configuration Drift
  - ri-11  # Build Toolchain and Service Supply Chain Compromise
related_mitigations:
  - mi-3  # Binary Provenance
  - mi-1  # Peer Source Code Review
---

## Summary

Software artifacts are identified by cryptographic hashes of their contents, ensuring that any change to an artifact produces a different identity and making tampering immediately detectable.

## Description

High-security environments require a tamper-proof identity scheme for software artifacts (e.g. compiled binaries, container images, JAR files, npm packages, Helm charts, configuration bundles). Content addressable identification uses cryptographic hashing (e.g., SHA-256) to derive an artifact's identity directly from its contents. Unlike mutable labels such as version tags or filenames, these identities are immutable: even a single-byte change produces a completely different hash. This provides the foundation for verifiable integrity of binaries, containers, packages, and other deliverables throughout the software development lifecycle.

Human-readable identifiers (semantic versions, branch names, commit references) remain useful for navigation and convenience but must never be relied upon for security or compliance verification.

## Requirements

* Every software artifact MUST be identified by a cryptographic hash (SHA-256 or stronger) of its contents
* Any modification to an artifact MUST produce a completely different identity
* Content addressable identities MUST be immutable and cannot be forged or reassigned to different content
* All systems that store, transfer, or deploy artifacts MUST reference them by their cryptographic identity

## Examples & Commentary

* Generate SHA-256 hashes for all build outputs including container images, compiled binaries, archives, and packages
* Configure container registries and artifact repositories to use content-addressable storage (e.g., Docker content trust, OCI image digests)
* CI/CD pipelines should propagate cryptographic identities rather than mutable tags when referencing artifacts across stages
* Implement verification checks at deployment boundaries that confirm the cryptographic identity of an artifact before allowing it to proceed
* Store artifact hashes in a secure, append-only record that serves as the source of truth for artifact identity
