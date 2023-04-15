.PHONY: generate # Processes all the .tex into .pdf(s)
generate:
	tectonic origin.tex
	tectonic hrishikesh_barman_general.tex
	tectonic hrishikesh_barman_fullstack.tex
	tectonic hrishikesh_barman_sre.tex
	tectonic hrishikesh_barman_de.tex
	tectonic hrishikesh_barman_freelance.tex

.PHONY: copy # Copy all the generated resume into site root
copy:
	cp *.pdf ../../static/cv

.PHONY: clean # Clean stuff
clean:
	rm -rf *.log .auctex-auto *.synctex.gz *.pdf

include $(HOME)/infra/workshop/common/Makefile.common
