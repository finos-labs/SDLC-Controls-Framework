.PHONY: build run clean readiness data data-nist data-ffiec data-owasp data-eu-ai-act

DOCKER_IMAGE := jekyll/jekyll
CONTAINER_NAME := sdlc-controls-jekyll
PORT := 4000

build: ## Build the Jekyll site
	docker run --rm \
		-v ./docs:/srv/jekyll \
		$(DOCKER_IMAGE) \
		jekyll build

run: ## Run the Jekyll dev server on localhost:4000
	docker run --rm \
		--name $(CONTAINER_NAME) \
		-p $(PORT):$(PORT) \
		-v ./docs:/srv/jekyll \
		$(DOCKER_IMAGE) \
		jekyll serve --host 0.0.0.0 --port $(PORT)

clean: ## Remove the generated _site directory and Jekyll cache
	rm -rf docs/_site docs/.jekyll-cache

readiness: ## Check document readiness and write readiness-report.md
	python3 scripts/readiness-check --report readiness-report.md

data: data-nist data-owasp data-eu-ai-act ## Regenerate regulatory reference data files (excluding FFIEC for the moment)

data-nist: ## Regenerate NIST SP 800-53r5 and AI 600-1 data files
	python3 scripts/dl_nist-sp-800-53r5.py
	python3 scripts/dl_nist-ai-600-1.py --leafs

data-ffiec: ## Regenerate FFIEC IT Booklets data file (requires pandoc)
	python3 scripts/dl_ffiec-itbooklets.py --yml

data-owasp: ## Regenerate OWASP LLM and ML Top 10 data files
	python3 scripts/dl_owasp.py

data-eu-ai-act: ## Regenerate EU AI Act data file
	python3 scripts/dl_eu-ai-act.py
