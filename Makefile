publish:
	@python setup.py sdist upload
	@$(MAKE) clean

deps:
	@pip install -r requirements.txt

clean:
	@$(MAKE) clean -sC test/
	@rm -rf build dist gae_ember_rest.egg-info $(shell find -name '*.pyc')

.PHONY: clean publish deps test
