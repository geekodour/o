STATIC_PAGES ?= syllabus project_ideas technical_learning_resources engineering_blogposts

# NOTE: If not emacsclient, this is also possible using emacs directly using the following
#		emacs --batch --load "$(HOME)/.emacs.d/early-init.el" --eval "(require 'org)" assets/pages/$(PAGE).org --funcall org-html-export-to-html
define export_static_html
    $(eval PAGE = $(1))
	emacsclient -e '(cf/export-static-html "$(PWD)/assets/pages/${PAGE}.org")'
endef

.PHONY: export # Export org-md and org-html files
export: export-org export-static

.PHONY: export-static # Export static html files
export-static:
	@echo "export-static starting"
	$(foreach var,$(STATIC_PAGES),$(call export_static_html, $(var));)
	@echo "export-static finished"

# TODO: We should generate includes before running export
.PHONY: export-org # Export .org files to .md
export-org:
	@echo "export-org starting"
	@emacsclient -e '(cf/hugo-export-all "$(PWD)/content-org")'
	@echo "export-org finished"

include $(HOME)/infra/workshop/common/Makefile.common
