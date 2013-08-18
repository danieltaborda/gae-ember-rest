test:
	@$(MAKE) test --no-print-directory -C test

example:
	@$(MAKE) --no-print-directory -C test

deps:
	@pip install -r requirements.txt

.PHONY: test example deps