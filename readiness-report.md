# SDLC Controls Framework — Readiness Report

Generated: 2026-06-07

_Scope: full repository_

## Risks

| ID | Title | Doc Status | Type | Sections | Cross-refs | Ready |
|:---|:------|:-----------|:-----|:--------:|:----------:|:-----:|
| ri-1 | Insider Threat | Working-Group-Approved | RC | ✅ | ❌ | ❌ |
| ri-3 | Credential and Secret Exposure | Draft | SEC | ✅ | ✅ | ✅ |
| ri-4 | Vulnerable Software in Production | Draft | SEC | ✅ | ✅ | ✅ |
| ri-5 | Audit and Compliance Evidence Failure | Draft | RC | ✅ | ✅ | ✅ |
| ri-6 | Unauthorised System Access | Draft | SEC | ✅ | ✅ | ✅ |
| ri-7 | Configuration Drift | Draft | OP | ✅ | ✅ | ✅ |
| ri-8 | Unauthorised Change | Draft | SEC | ❌ | ✅ | ❌ |
| ri-9 | Environment Breach | Draft | SEC | ✅ | ✅ | ✅ |
| ri-10 | Dependency and Transitive Supply Chain Compromise | Draft | SEC | ✅ | ✅ | ✅ |
| ri-11 | Build Toolchain and Service Supply Chain Compromise | Draft | SEC | ✅ | ✅ | ✅ |

## Mitigations

| ID | Title | Doc Status | Type | Sections | Mitigates | Reg. Refs | Cross-refs | Ready |
|:---|:------|:-----------|:-----|:--------:|:---------:|:---------:|:----------:|:-----:|
| mi-2 | Content Addressable Identities | Draft | PREV | ❌ | ✅ | ✅ | ❌ | ❌ |
| mi-3 | Software Artifact Provenance | Draft | PREV | ❌ | ✅ | ✅ | ❌ | ❌ |
| mi-4 | Requirements Management | Pre-Draft | PREV | ❌ | ❌ | ❌ | ✅ | ❌ |
| mi-5 | Vulnerability Scanning - SAST | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-6 | Vulnerability Scanning - DAST | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-7 | Vulnerability Scanning - Dependencies | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-8 | Version Control | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-9 | Component Inventory | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-10 | Secret Detection | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-11 | Vulnerability Remediation SLAs | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-12 | Deployment Gating | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-13 | System Inventory | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-14 | Test Evidence Retention | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-15 | Testing Requirements | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-16 | Test Execution and Sign-Off | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |
| mi-17 | Service Dependency Control | Draft | PREV | ✅ | ✅ | ✅ | ✅ | ✅ |

## Framework Validation Coverage

Reference IDs are validated against a data file when one is available.
Run the corresponding make target to generate any missing file.

| Framework | Status |
|:----------|:-------|
| `eu-ai-act` | ✅ validated |
| `ffiec-itbooklets` | ⚠️ not currently automated due to source access restrictions — see `scripts_docs/RUNBOOK.md` |
| `ffiec-itbooklets_v2` | ⚠️ not currently automated due to source access restrictions — see `scripts_docs/RUNBOOK.md` |
| `iso-42001` | ⚠️ not currently automated — see `scripts_docs/RUNBOOK.md` |
| `nist-ai-600-1` | ✅ validated |
| `nist-sp-800-53r5` | ✅ validated |
| `owasp-llm` | ✅ validated |
| `owasp-ml` | ✅ validated |

## Issues Detail

**`docs/_risks/ri-1_insider-threat.md`**
- 'related_risks' references 'ri-2' which does not exist
- 'related_risks' references 'ri-23' which does not exist

**`docs/_mitigations/mi-2_content-addressable-identities.md`**
- missing section '## Links'
- 'related_mitigations' references 'mi-1' which does not exist

**`docs/_mitigations/mi-3_software-artifact-provenance.md`**
- missing section '## Links'
- 'related_mitigations' references 'mi-1' which does not exist

**`docs/_mitigations/mi-4_requirements.md`**
- missing section '## Links'
- missing section '## Requirements'
- unexpected heading '## Map to related risks'
- unexpected heading '## Requirements (Expectations)'
- unexpected heading '## Map to related risks'
- 'mitigates' is empty — every mitigation must reference at least one risk
- no regulatory references found (nist-sp-800-53r5, ffiec, owasp, etc.)

**`docs/_risks/ri-8_unauthorised-change.md`**
- missing section '### Consequences'
- unexpected heading '## Consequences'

## Risk–Mitigation Coverage Matrix

| Risk | mi-2 | mi-3 | mi-4 | mi-5 | mi-6 | mi-7 | mi-8 | mi-9 | mi-10 | mi-11 | mi-12 | mi-13 | mi-14 | mi-15 | mi-16 | mi-17 |
|:-----|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **ri-1** Insider Threat | ✅ | ✅ |  |  |  |  | ✅ |  |  |  |  |  |  |  |  |  |
| **ri-3** Credential and Secret Exposure |  |  |  |  |  |  |  |  | ✅ |  |  |  |  |  |  |  |
| **ri-4** Vulnerable Software in Production |  |  |  | ✅ | ✅ | ✅ |  |  |  | ✅ | ✅ |  |  | ✅ | ✅ | ✅ |
| **ri-5** Audit and Compliance Evidence Failure |  |  |  |  |  |  |  |  |  |  |  |  | ✅ | ✅ | ✅ |  |
| **ri-6** Unauthorised System Access |  |  |  |  |  |  |  |  |  |  |  | ✅ |  |  |  |  |
| **ri-7** Configuration Drift | ✅ |  |  |  |  |  |  | ✅ |  |  |  |  |  |  |  | ✅ |
| **ri-8** Unauthorised Change |  |  |  |  |  |  | ✅ |  |  |  |  |  | ✅ |  | ✅ |  |
| **ri-9** Environment Breach |  | ✅ |  |  |  |  |  |  |  |  | ✅ |  |  |  |  |  |
| **ri-10** Dependency and Transitive Supply Chain Compromise |  | ✅ |  |  |  | ✅ |  | ✅ |  |  |  |  |  |  |  | ✅ |
| **ri-11** Build Toolchain and Service Supply Chain Compromise | ✅ | ✅ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
