
PYS := $(filter-out $(wildcard __*__.py), $(wildcard *.py))
PATH_UIS =../uis/

%.py: $(PATH_UIS)%.ui
	@echo ${sub_make_tab}"- build $@"
	@pyuic5 -x $^ -o $@
	@sed -i -e 's/import ressources_rc/import eccw_gui.images.ressources_rc/g' ./$@

all: $(PYS)