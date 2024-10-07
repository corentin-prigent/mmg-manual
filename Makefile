
COMP = pdflatex
SRC  = main.tex
PDF  = documentation-mmg.pdf

all: pdf

pdf : $(SRC)
	$(COMP) -jobname=mmg-manual $(SRC)
