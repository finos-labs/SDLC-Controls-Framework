.PHONY: build run stop clean

DOCKER_IMAGE := jekyll/jekyll:4
PORT := 4000
CONTAINER_NAME := sdlc-controls-jekyll

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
		jekyll serve --host 0.0.0.0 --port $(PORT) --config _config.yml,_config_dev.yml

stop: ## Stop the running Jekyll dev server
	docker stop $(CONTAINER_NAME)

clean: ## Remove the generated _site directory
	rm -rf docs/_site docs/.jekyll-cache

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'
