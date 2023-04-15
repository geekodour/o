STATIC_PAGES ?= syllabus project_ideas technical_learning_resources engineering_blogposts

define export_static_html
    $(eval $@_PAGE = $(1))
	emacs --batch --load "$(HOME)/.emacs.d/early-init.el" --eval "(require 'org)" assets/pages/${$@_PAGE}.org --funcall org-html-export-to-html
endef


.PHONY: export # Export org-md and org-html files
export: export-org

.PHONY: export-static # Export static html files
export-static:
	$(foreach var,$(STATIC_PAGES),$(call export_static_html, $(var));)

.PHONY: export-org # Export .org files to .md
export-org:
	@echo "Starting export "
	@emacsclient -e '(cf/hugo-export-all "$(PWD)/content-org")'
	@echo "Exported successfully"

include $(HOME)/infra/workshop/common/Makefile.common
