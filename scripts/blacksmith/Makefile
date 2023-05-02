.PHONY: everything # fetch and generate evrying
everything: packages toolchests pages

.PHONY: packages # Generate org files for locally installed stuff
packages:
	./scripts/populate_current_packages.fish

.PHONY: toolchests # Fetch and generate tools from airtable
toolchests: toolchests-fetch toolchests-generate
.PHONY: toolchests-fetch
toolchests-fetch:
	airtable-export ${TEMP_DIR} appWjub9re6jaNTpA toolchest --json
	airtable-export ${TEMP_DIR} appWjub9re6jaNTpA datasets --json
	airtable-export ${TEMP_DIR} appHCIWcQJnvFYG2n mobile_apps --json
.PHONY: toolchests-generate
toolchests-generate:
	./scripts/populate_toolchests.py

.PHONY: pages # Fetch and generate misc pages
pages: tw_bots_page
.PHONY: tw_bots_page
tw_bots_page: tw_bots-fetch tw_bots-generate
.PHONY: tw_bots-fetch
tw_bots-fetch:
	airtable-export ${TEMP_DIR} appt7Gq1QtO46mh0S tw_bots --json
.PHONY: tw_bots-generate
tw_bots-generate:
	./scripts/populate_bots.py

.PHONY: clean # Clean temporary files
clean:
	rm -rf temp

include $(HOME)/infra/workshop/common/Makefile.common
#    __
# __( o)>
# \ <_ ) r90
