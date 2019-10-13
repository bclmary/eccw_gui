ifndef VERBOSE
.SILENT:
endif

VIEWER_DIRS = \
	shared\
	calculator_app\
	plot_app\
	main_app

export sub_make_tab='  '

all: viewers ressources

viewers: 
	echo viewers:
	for d in $(VIEWER_DIRS); do (\
		echo "* $$d"; \
		$(MAKE) -C eccw_gui/$$d/viewers \
	) ; done

ressources: 
	echo ressources:
	$(MAKE) -C eccw_gui/images
