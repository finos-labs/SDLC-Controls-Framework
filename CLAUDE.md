# SDLC Controls Framework

## Project overview

A Jekyll-based catalogue of SDLC risks and mitigations for software governance in financial institutions. Published as a static site via GitHub Pages.

## Repository structure

```
docs/                        # Jekyll source (this is the Jekyll root)
  _risks/                    # Risk files (Markdown with YAML frontmatter)
  _mitigations/              # Mitigation/control files (Markdown with YAML frontmatter)
  _data/                     # YAML mappings to external standards
  _layouts/                  # Jekyll HTML templates
  _includes/                 # Jekyll HTML partials
  _config.yml                # Jekyll config (baseurl, collections, classifications)
  _config_dev.yml            # Local dev override (clears baseurl)
scripts/                     # Python scripts for downloading/processing external standards
```

## Adding risks

Create a file in `docs/_risks/` named `ri-{sequence}_{title-slug}.md`.

Required frontmatter:
```yaml
---
sequence: <number>           # Next available sequence number
title: "Risk Title"
layout: risk
doc-status: Pre-Draft        # Pre-Draft | Draft | Working-Group-Approved | Published
type: <type>                 # OP (Operational) | SEC (Security) | RC (Regulatory & Compliance)
---
```

Optional frontmatter fields for external standard references:
- `owasp-llm_references` - keys from `_data/owasp-llm.yml`
- `owasp-ml_references` - keys from `_data/owasp-ml.yml`
- `nist-ai-600-1_references` - keys from `_data/nist-ai-600-1.yml`
- `nist-sp-800-53r5_references` - keys from `_data/nist-sp-800-53r5.yml`
- `iso-42001_references` - keys from `_data/iso-42001.yml`
- `ffiec-itbooklets_references` - keys from `_data/ffiec-itbooklets.yml`
- `eu-ai-act_references` - keys from `_data/eu-ai-act.yml`
- `related_risks` - array of `ri-{n}` identifiers

Body sections:
- `## Summary` - one sentence overview of the risk
- `## Description` - detailed explanation of the risk
- `### Consequences` - impact if the risk materialises
- `## Links` - external references

## Adding mitigations

Create a file in `docs/_mitigations/` named `mi-{sequence}_{title-slug}.md`.

Required frontmatter:
```yaml
---
sequence: <number>           # Next available sequence number
title: "Mitigation Title"
layout: mitigation
doc-status: Pre-Draft        # Pre-Draft | Draft | Working-Group-Approved | Published
type: <type>                 # PREV (Preventative) | DET (Detective)
mitigates:                   # Required: which risks this addresses
  - ri-<n>
---
```

Optional: same external standard references as risks, plus `related_mitigations` (array of `mi-{n}`).

Body sections:
- `## Summary` - one sentence overview of the control
- `## Description` - detailed explanation
- `## Requirements` - expectations using RFC 2119 language (MUST, SHOULD, MAY)
- `## Examples & Commentary` - practical implementation examples and guidance

## Referencing external standards

Each reference key must exist in the corresponding YAML file under `docs/_data/`. Add inline comments after each reference for readability:
```yaml
nist-sp-800-53r5_references:
  - si-7   # SI-7 Software, Firmware, And Information Integrity
```

## Running locally

```sh
make run     # Docker: serve at http://localhost:4000
make build   # Docker: build only
make clean   # Remove _site and .jekyll-cache
```

## Commit conventions

- Use present tense, imperative mood ("Add feature" not "Added feature")
- Limit first line to 72 characters
- Commits require DCO sign-off: `Signed-off-by: Name <email>`
- Do not add Co-Authored-By lines
