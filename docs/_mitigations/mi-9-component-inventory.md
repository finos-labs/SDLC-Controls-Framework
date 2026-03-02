---
sequence: 9
title: Component Inventory
layout: mitigation
doc-status: Draft
type: PREV
# nist-sp-800-53r5_references: TBD
---

## Summary

Software must maintain an accurate, machine-readable inventory of what is actually shipped in each artifact, as the input for downstream analysis.

## Description

Component inventory is the practice of identifying and cataloguing all third-party components (libraries, packages, modules) that are included in a software artifact — i.e. what is actually shipped. This includes direct and transitive dependencies. The output is typically a Software Bill of Materials (SBOM) in a standard format such as SPDX or CycloneDX.

Without an inventory of what is shipped, downstream mitigations (vulnerability scanning, license compliance, etc.) cannot be performed; this inventory is the input for those analyses. Extraction from the actual artifact (container image, binary, filesystem) rather than from declarations alone enables detection of discrepancies between what is declared and what is present.

## Map to related risks

- Exposure to known vulnerabilities (CVEs)
- Incompatible or prohibited licenses
- Supply chain tampering
- Typosquatting and dependency confusion
- Compromised or malicious packages
- Discrepancies between declared and actual components
- Inability to respond quickly to new advisories

## Requirements

1. Extraction MUST be performed on what is actually shipped (the artifact: container image, application binary, library, etc.), not only on declared dependencies.
2. The output MUST be a structured, machine-readable SBOM (e.g. SPDX or CycloneDX).
3. The inventory MUST include direct and transitive dependencies with version and provenance information where available.
4. The SBOM MUST be produced for each releasable artifact.
5. The SBOM MAY include recommended elements to address the related risks:
   - *CVEs, advisories:* component name, version, unique identifiers (PURL, CPE), dependency relationships — enables vulnerability matching and rapid response.
   - *Licenses:* license information — enables automated license compliance checks.
   - *Supply chain, typosquatting, compromised packages:* supplier name, component point of origin (PURL), file hashes, signature — enables provenance verification and tampering detection.
   - *Discrepancies:* author of SBOM record, unique SBOM identifier, timestamp — enables auditability and traceability.

## Examples

**Without component inventory:** Without a component inventory, what is expected (e.g. from dependency declarations) may differ from what actually exists in the artifact. Transitive dependencies, swapped packages, or build-time changes are invisible. Vulnerabilities or license issues in those components go undetected, exposing the organisation to risks that would otherwise be identified and addressed.

**Vulnerabilities:** When a new CVE is published (e.g. Log4Shell), an organisation with SBOMs can immediately search across all artifacts to identify which contain the affected component and version. Without an inventory, they would need to manually inspect each codebase or wait for a scan; with SBOMs, remediation can be prioritised and executed within hours.

**Licenses:** An organisation prohibits GPL-licensed components in production for licensing reasons. An SBOM listing all components with their licenses allows automated checks before deployment: any artifact containing a prohibited license can be flagged or blocked, avoiding legal or compliance issues that would only surface after release.

**Tools:** Tools exist to extract components from container images or filesystems, or to generate SBOMs from the build. The SBOM is the input for vulnerability scanning and license compliance checks.

## Links

- [NTIA Minimum Elements for an SBOM](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)
- [OWASP SCVS V2: SBOM Requirements](https://scvs.owasp.org/scvs/v2-software-bill-of-materials/)
- [CycloneDX Specification](https://cyclonedx.org/specification/overview/)
- [SPDX Specification](https://spdx.github.io/spdx-spec/)
- [CISA SBOM Guide](https://www.cisa.gov/sbom)
- [CRA Regulation (EU) 2024/2847](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R2847-20241120) (Annex I, vulnerability handling)
- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) (PS.3.2, RV.1.2)
