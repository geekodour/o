STATIC_PAGES ?= syllabus project_ideas technical_learning_resources engineering_blogposts

# If not emacsclient, this is also possible using emacs directly using the following
# emacs --batch --load "$(HOME)/.emacs.d/early-init.el" --eval "(require 'org)" \
# 	assets/pages/file_name.org --funcall org-html-export-to-html
define export_static_html
    $(eval PAGE = $(1))
	emacsclient -e '(cf/export-static-html "$(PWD)/assets/pages/${PAGE}.org")'
endef

.PHONY: export # Export org-md and org-html files
export: generate-org-include-files export-org export-static

.PHONY: export-static # Export static html files
export-static:
	@echo "export-static starting"
	$(foreach var,$(STATIC_PAGES),$(call export_static_html, $(var));)
	@echo "export-static finished"

.PHONY: export-org # Export .org files to .md
export-org:
	@echo "export-org starting"
	@emacsclient -e '(cf/hugo-export-all "$(PWD)/content-org")'
	@echo "export-org finished"

.PHONY: generate-org-include-files # Generate files to be included in other org files
# see https://github.com/direnv/direnv/issues/262
generate-org-include-files:
	@cd ./scripts/blacksmith && ./scripts/env_aware_make_everything.sh
