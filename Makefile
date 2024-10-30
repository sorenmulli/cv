.PHONY: all install run

all: install

install:
	@pip install -e .

run:
	@python fh_soren_cv/run.py
