
COMP = pdflatex
SRC  = src/main.tex
PDF  = documentation-mmg.pdf
DIR  = output

all: check-output-dir pdf

pdf : $(SRC)
	$(COMP) -output-directory=$(DIR) -jobname=mmg-manual $(SRC)
	$(COMP) -output-directory=$(DIR) -jobname=mmg-manual $(SRC)

check-output-dir :
	@if [ ! -d "$(DIR)" ]; then \
		echo "Directory $(DIR) does not exist. Creating..."; \
		mkdir -p $(DIR); \
	fi
