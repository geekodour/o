#!/usr/bin/env fish

set REQUIRED_ENV_VARS PROJECT_ROOT TEMP_DIR ORG_DIR
for i in $REQUIRED_ENV_VARS
    if not string length --quiet $$i
        echo "ERROR: ENV VARS not set correctly"
        exit 1
    end
end
mkdir -p $TEMP_DIR
mkdir -p $ORG_DIR

# Arch Packages
listpackages aur | xargs -I % fish -c 'pacman -Qi %| rg "Name|Description|URL"| awk -F " : " \'{print $2}\'| string join ";"' >$TEMP_DIR/aur_packages.csv
listpackages official | xargs -I % fish -c 'pacman -Qi %| rg "Name|Description|URL"| awk -F " : " \'{print $2}\'| string join ";"' >$TEMP_DIR/official_packages.csv


# Firefox extensions
# NOTE: We create a JSON intermediate for debugging easier if anything odd happens
# NOTE: There's also addons.json but it conatins disabled/uninstalled extensions aswell and no way to filter it.
set FF_ADDON_PATH ~/.config/firefox/geekodour/extensions.json
set FF_JQ_FILTER 'map(select(.type == "extension" and .location == "app-profile" and (.userDisabled | not)))'
set FF_JQ_EXTRACT '{Name: .defaultLocale.name, Description: .defaultLocale.description, URL: .installTelemetryInfo.sourceURL}'
# NOTE: used sed for some descriptions that contain newlines that we do not want
# NOTE: We use ;; as the separator
# NOTE: I am not exactly sure why I picked dasel an not jq join for what I did there
cat $FF_ADDON_PATH | jq -r ".addons | $FF_JQ_FILTER | .[] | $FF_JQ_EXTRACT" | sed "s/\\\\n//g" >$TEMP_DIR/ff_addons.json
dasel -m -r json --format '{{select ".Name"}};;{{select ".Description"}};;{{select ".URL"}}' '.[*]' <$TEMP_DIR/ff_addons.json >$TEMP_DIR/ff_addons.csv

# org-tables
# TODO: We need a proper csv to org converter, the following is not very robust but works
awk -F ";" '{print "| [[" $3 "]["$1"]] |" $2 "| "}' $TEMP_DIR/official_packages.csv >$ORG_DIR/official_packages.org
awk -F ";" '{print "| [[" $3 "]["$1"]] |" $2 "| "}' $TEMP_DIR/aur_packages.csv >$ORG_DIR/aur_packages.org
awk -F ";;" '{print "| [[" $3 "]["$1"]] |" $2 "| "}' $TEMP_DIR/ff_addons.csv >$ORG_DIR/ff_addons.org
