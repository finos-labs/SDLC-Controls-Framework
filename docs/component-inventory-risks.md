# Component Inventory — Risk and description

Risks addressed by the Component Inventory mitigation (mi-9).

| Risk | Description | Mitigation | Recommended SBOM elements |
|------|-------------|------------|---------------------------|
| Lack of visibility and traceability of components in software | No visibility into what components are in each artifact and no ability to trace them, blocking response to issues and downstream analysis. | Component inventory | Component name, version, PURL, dependency relationships |
| Exposure to known vulnerabilities (CVEs) | Inability to assess or remediate vulnerabilities in dependencies. | Component inventory + vulnerability scanning | Component name, version, PURL, CPE, dependency relationships |
| Incompatible or prohibited licenses | Legal or compliance issues from license violations. | Component inventory + license compliance checks | License information |
| Supply chain tampering | Packages swapped or modified in transit. | Component inventory (actual vs declared comparison) | Supplier name, PURL, file hashes, signature |
| Typosquatting and dependency confusion | Malicious or incorrect packages pulled instead of intended ones. | Component inventory (actual vs declared comparison) | Supplier name, PURL, file hashes, signature |
| Compromised or malicious packages | Backdoors or malware in dependencies. | Component inventory + vulnerability scanning | Supplier name, PURL, file hashes, signature |
| Discrepancies between declared and actual components | What is in the artifact differs from what is declared. | Component inventory (from artifact) | Author, unique SBOM identifier, timestamp |
| Inability to respond quickly to new advisories | Dependency graph unknown, so remediation is reactive and slow. | Component inventory + vulnerability scanning | Component name, version, PURL, CPE, dependency relationships |
