component=./node_modules/component-hooks/node_modules/.bin/component
client = $(shell find client -type f)

default: node_modules components public

node_modules:
	@npm install

components:
	@$(component) install

public: $(client)
	@node build.js
	@du -h $@/$@.*
	@touch public/

run: lib default
	@dev_appserver.py . --port 5000 --admin_port 7000

test: lib
	@python tests.py -f

lib:
	@ln -fs $(PWD)/../$@ $@

clean:

.PHONY: test run default
