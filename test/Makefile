start: lib
	@dev_appserver.py . --port 7000 --admin_port 5000

test: lib
	@nosetests -q --with-gae -l test.lib,test.tests

lib:
	@ln -fs $(PWD)/$@ $@

.PHONY: test start
