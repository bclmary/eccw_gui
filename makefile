ifndef VERBOSE
.SILENT:
endif

VIEWER_DIRS = \
	shared\
	calculator_app\
	plot_app\
	main_app

export sub_make_tab='  '

all: viewers ressources pypi

viewers: 
	echo "\nviewers:"
	for d in $(VIEWER_DIRS); do (\
		echo "* $$d"; \
		$(MAKE) -C eccw_gui/$$d/viewers \
	) ; done

ressources: 
	echo "\nressources:"
	$(MAKE) -C eccw_gui/images

dists:
	@echo "\ndistributions:"
	@echo "* make source dist"
	python3 setup.py --quiet sdist
	@echo "* make built dist"
	python3 setup.py --quiet bdist_wheel

DIST=$$(python3 setup.py --fullname)

pypi: dists
	@echo "\nupload to pypi"
	@echo "* version=$(DIST)"
	twine upload dist/$(DIST)*

clean:
	@echo clean builds:
	python3 setup.py --quiet clean --all
