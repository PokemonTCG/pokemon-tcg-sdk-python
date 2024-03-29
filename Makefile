# This file is part of pokemontcgsdk.
# https://github.com/PokemonTCG/pokemon-tcg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# create a virtual environment
.PHONY: env
env:
	@python3 -m venv env

# install all dependencies (do not forget to create a virtualenv first)
setup: env
	@env/bin/pip install -U -e .\[tests\]

# test your application (tests in the tests/ directory)
test: unit

unit: env
	@env/bin/coverage run --branch env/bin/nosetests -v --with-yanc -s tests/
	@env/bin/coverage report -m --fail-under=80

# show coverage in html format
coverage-html: env unit
	@env/bin/coverage html

# run tests against all supported python versions
tox: env
	@env/bin/tox

#docs:
	#@cd mtgsdk/docs && make html && open _build/html/index.html
