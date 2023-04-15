.PHONY: export # Export org-md and org-html files
export: export-org

.PHONY: export-org # Export .org files to .md
# NOTE: Export Takes about 2m for ~200 files)
#		This export exports everything and not only the changed files. Which is
#		what we want sometimes if we commited things without exporting
export-org:
	@echo "Starting export "
	@emacsclient -e '(cf/hugo-export-all "$(PWD)/content-org")'
	@echo "Exported successfully"

include $(HOME)/infra/workshop/common/Makefile.common
