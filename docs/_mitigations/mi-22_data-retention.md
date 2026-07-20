---
sequence: 22
title: Data Retention and Disposal
layout: mitigation
doc-status: Draft
type: PREV
phase: LIFECYCLE
nist-sp-800-53r5_references:
  - au-11  # AU-11 Audit Record Retention
  - mp-6   # MP-6 Media Sanitization
  - si-12  # SI-12 Information Management and Retention
  - sa-4   # SA-4 Acquisition Process
uk-fca_references:
  - sysc-15a-2   # SYSC 15A.2, operational resilience requirements
  - pra-ss1-21   # PRA SS1/21, operational resilience impact tolerances
ffiec-itbooklets_references:
  - sec-3  # SEC: III Security Operations, data classification, sanitisation, secure disposal
  - dam-7  # DAM: VII Maintenance, retirement and decommissioning of components and their data
us-nydfs_references:
  - nydfs-500-13  # 23 NYCRR §500.13, Limitations on Data Retention
mitigates:
  - ri-5   # Audit and Compliance Evidence Failure
related_mitigations:
  - mi-1   # Code Review
  - mi-14  # Test Evidence Retention
  - mi-3   # Software Artifact Provenance
  - mi-13  # System Ownership
  - mi-20  # Requirements Approval
---

## Summary

The organisation must define, for each class of SDLC-generated record and artefact, a minimum period for which it must be retained and a point at which it must be securely disposed of, so that governance evidence survives long enough to support oversight and to be produced on demand, while data that is no longer needed does not persist as an unmanaged exposure.

## Description

SDLC activity generates records and artefacts across the lifecycle, such as review outcomes, test evidence, scan results, approval records, deployment records, build artefacts, audit logs, and exception records. Each of these is produced by a more specific mitigation elsewhere in this catalogue, for example [SDLC-PREV-001]({% link _mitigations/mi-1_code-review.md %}) for review outcomes and [SDLC-PREV-014]({% link _mitigations/mi-14_test-evidence.md %}) for test evidence. This mitigation is the general policy those records are governed by. It does not replace the record producing controls; it sets how long their output must be kept, and what happens to it afterwards.

Retention has two failure directions. An organisation that deletes a review outcome, test result, or approval record too early cannot use it to investigate an incident, assess whether a control is working, or hold a decision accountable. On the other hand, stale build artefacts, decommissioned environment snapshots, superseded test data, and old pipeline logs that persist only because nobody set an end date add up to an exposure surface no one is managing.

A record class therefore has two boundaries. The floor is a minimum retention period, set by the longest applicable regulatory or contractual requirement, below which disposal is prohibited. The ceiling is a maximum period, or a triggering event, beyond which disposal is required. These obligations follow the record, not the system that produced it. They apply equally to records held internally and to records held in third-party or SaaS tooling, and they can be suspended by a legal or regulatory hold without being permanently disabled.

## Requirements

* The organisation MUST maintain a data retention and disposal policy that classifies SDLC-generated record and artefact types and assigns each class a minimum retention period and a maximum retention period or disposal-triggering event
* The minimum retention period for a record class MUST NOT be less than the longest applicable regulatory or contractual retention requirement for that class
* Records subject to a minimum retention period MUST be immutable for the duration of that period; they MUST NOT be modifiable, deletable, or replaceable outside an approved and auditable exception process
* Once a record class reaches its maximum retention period or disposal-triggering event, it MUST be securely disposed of unless a legal hold or an approved retention exception applies
* Secure disposal MUST use a sanitisation method appropriate to the storage medium such that the disposed data is not recoverable through ordinary means
* A legal hold process MUST exist that can suspend scheduled disposal for records subject to litigation, regulatory examination, or investigation, and that hold MUST be releasable only by an authorised approver
* Retention and disposal obligations MUST extend to third-party or SaaS tooling that stores SDLC records on the organisation's behalf, through contractual terms, configuration, or both
* Disposal actions MUST themselves be logged, including the record class, volume or identity of the disposed records, the actor or automated process that performed the disposal, and the timestamp
* The organisation MUST review the retention and disposal policy periodically and whenever an applicable regulatory or contractual retention requirement is introduced or changes
* An exception process MUST exist for retaining a record class beyond its maximum period or disposing of it before its minimum period has elapsed; exceptions MUST require named approval, documented justification, and are subject to periodic governance review

## Examples & Commentary

* **Setting the floor per record class:** The longest applicable requirement usually differs by record type and jurisdiction. Audit and compliance evidence, financial transaction adjacent records, and general operational records often carry different regulatory minimums. The policy should record, per class, which requirement sets the floor rather than applying one blanket period to all SDLC records.

* **Disposal as a scheduled event, not an afterthought:** Configure object storage lifecycle rules, log retention settings, and artefact repository cleanup jobs to enforce the maximum period automatically, rather than relying on manual purges. Automated enforcement also produces the disposal log entries the policy requires.

* **Sanitisation methods:** Cryptographic erasure (destroying the key protecting encrypted data at rest) is typically sufficient and auditable for cloud object storage; physical media destruction with a certificate of destruction may be required for on-premises hardware being decommissioned.

* **Legal hold interaction:** When an incident or regulatory inquiry is opened, the records relevant to the affected systems and time period should be placed on hold before any scheduled disposal job runs, and the hold should be scoped and time-bound so it is lifted once no longer needed rather than becoming a silent, permanent retention exception.

* **Third-party flow-down:** Where CI/CD, ticketing, or artefact hosting is outsourced to a SaaS vendor, the retention and disposal obligations should appear in the vendor contract, including the vendor's obligation to support export before offboarding and to confirm deletion afterwards. The organisation remains accountable for the record even though it does not control the storage.

* **Stale lower-environment data:** Test and staging environments that retain copies of production-like data past their operational need are a common source of ceiling failures. Data refresh and expiry policies for these environments should be governed by the same policy as other SDLC records, even though the data did not originate from a governance process.

## Links

- [NIST SP 800-53r5 AU-11: Audit Record Retention](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [NIST SP 800-53r5 MP-6: Media Sanitization](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [NIST SP 800-53r5 SI-12: Information Management and Retention](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [NIST SSDF SP 800-218 PS.3: Archive and Protect Each Software Release](https://csrc.nist.gov/pubs/sp/800/218/final)
- [NYDFS 23 NYCRR 500.13: Limitations on Data Retention](https://www.dfs.ny.gov/system/files/documents/2023/03/23NYCRR500_0.pdf)
