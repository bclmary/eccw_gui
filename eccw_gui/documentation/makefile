NAME = ECCW

SRC = ECCW.md

OPTS = \
	--standalone \
	--toc \
	--toc-depth 2 \
	--number-sections \
	--filter pandoc-crossref \
	--citeproc \

EPUB3OPTS = \
 	--to epub3 \
	--css=epub3.css 

.PHONY: all epub epub3

all: epub

epub: $(NAME).epub

$(NAME).epub: $(SRC)
	pandoc $(OPTS) $(EPUB3OPTS) $^ -o $@
