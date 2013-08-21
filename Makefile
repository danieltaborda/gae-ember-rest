test:
	@$(MAKE) test --no-print-directory -C test

example:
	@$(MAKE) --no-print-directory -C test

deps:
	@pip install -r requirements.txt


publish:
	@python setup.py sdist upload
	@$(MAKE) clean

clean:
	@$(MAKE) clean -sC test/
	@rm -rf build dist gae_ember_rest.egg-info $(shell find -name '*.pyc')

.PHONY: clean publish deps example test
