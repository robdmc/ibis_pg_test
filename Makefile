#! /usr/bin/make 


.PHONY: help \
shell \
test \
clean

help:  ## Print the help documentation
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

shell: ## Open a shell in the container.  Can run ipython from here
	-docker-compose run --rm shell

test: ## Run failing ibis scenario
	-docker-compose run --rm test

clean: ## clean out images you built
	docker-compose down
	-docker images | grep 'ibis_test_base' | awk '{print $3}'  | xargs docker rmi
	-docker images | grep 'ibis_pg' | awk '{print $3}'  | xargs docker rmi
	-docker builder prune -f



