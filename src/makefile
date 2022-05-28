.PHONY: clean

NAME 	   	:= Proxy Configuration
VERSION	:= 1.0
DEVELOPERS	:= Ariel Plasencia
COPYRIGHT  	:= Copyright © 2022: $(DEVELOPERS)

run: ## Run the project ;)
	chmod +x proxy.py
	sudo ./proxy.py

info: ## Display project description
	@echo "$(NAME) v$(VERSION)"
	@echo "$(COPYRIGHT)"

version: ## Show the project version
	@echo "$(NAME) v$(VERSION)"

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
