.PHONY: build run clean

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
