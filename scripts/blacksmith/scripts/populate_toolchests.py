#!/usr/bin/env python3
import os

import numpy as np
import orgparse as op
import pandas as pd

TOOLCHESTS = ["toolchest", "workflows", "mobile_apps", "datasets"]
TOOLCHEST_PATHS = dict(
    zip(
        TOOLCHESTS,
        [
            {
                "source": os.path.join(os.environ["TEMP_DIR"], f"{c}.json"),
                "destination": os.path.join(os.environ["ORG_DIR"], f"{c}.org"),
            }
            for c in TOOLCHESTS
        ],
    )
)


def write_toolchest_file(toolchest):
    dest_file = TOOLCHEST_PATHS["toolchest"]["destination"]
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write("🫶: selfhosted, ☠: outdated \n")
        for cat, rows in toolchest.items():
            f.write(f"* {cat}\n")
            f.write("| Name | Description | Usecase | Type |\n")
            for t in rows:
                f.write(f"{t}\n")


def process_toolchest_file():
    source_file = TOOLCHEST_PATHS["toolchest"]["source"]
    df = pd.read_json(source_file).replace(np.nan, "", regex=True)
    gg = df.groupby("Category")
    cat_tool_map = {}
    for name, group in gg.groups.items():
        items_in_cat = len(list(group))
        category = f"{name}({items_in_cat})"
        tool_indexes = list(group)
        rows = []
        for t in tool_indexes:
            row = dict(df.iloc[t])
            legends = {
                "selfhost": ("🫶" if bool(row["Selfhost"]) else ""),
                "outdated": ("☠" if bool(row["Outdated"]) else ""),
            }
            final_cells = {
                "legends": "".join(legends.values()),
                "name": f"[[{row['URL']}][{row['Name']}]]",
                "desc": row["Description"].strip().replace("\n", ""),
                "use_case": row["Use cases"],
                "type": row["Type"],
            }
            final_row = "| {legends} {name} | {desc} | {use_case} | {type} |".format(
                **final_cells
            )
            rows.append(final_row)
        cat_tool_map[category] = rows
    # write cat_tool_map to a file
    write_toolchest_file(cat_tool_map)


def process_mobile_apps_file():
    source_file = TOOLCHEST_PATHS["mobile_apps"]["source"]
    df = pd.read_json(source_file).replace(np.nan, "", regex=True)
    df["org_link"] = "[[" + df["Link"] + "][" + df["Name"] + "]]"
    all_apps = list(df["org_link"])

    # write org
    dest_file = TOOLCHEST_PATHS["mobile_apps"]["destination"]
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write(" ○ ".join(all_apps))


def process_datasets_file():
    source_file = TOOLCHEST_PATHS["datasets"]["source"]
    df = pd.read_json(source_file).replace(np.nan, "", regex=True)
    df["org_link"] = "[[" + df["Link"] + "][" + df["Name"] + "]]"
    all_datasets = list(df["org_link"])

    # write org
    dest_file = TOOLCHEST_PATHS["datasets"]["destination"]
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write(" ○ ".join(all_datasets))


def populate_workflows_file():
    """
    - Add missing workflows(categories) from airtable to workflows.org.
    - This is append only.
    - This is supposed to only add the heading if missing and absolutely nothing else.
    """
    # get existing categories
    workflows = op.load(os.environ["WORKFLOW_ORG_FILE"])
    existing_categories = [c.heading for c in workflows.children]

    # get remote categories
    source_file = TOOLCHEST_PATHS["workflows"]["source"]
    df = pd.read_json(source_file).replace(np.nan, "", regex=True)
    gg = df.groupby("Category")
    remote_categories = list(gg.indices.keys())

    # add missing categories
    missing_categories = set(remote_categories).difference(existing_categories)
    if len(missing_categories) > 0:
        print("Adding missing workflows:", missing_categories)
        with open(os.environ["WORKFLOW_ORG_FILE"], "a", encoding="utf-8") as f:
            for c in missing_categories:
                f.write(f"* {c}\n")


# TODO: Currently links are not rendered. Simple body text will be shown.
# see: https://github.com/karlicoss/orgparse/issues/8
# TODO: We'll need to implement some recursive logic to generate the body by visiting each child of the heading
def populate_final_workflows_file():
    workflows = op.load(os.environ["WORKFLOW_ORG_FILE"])
    existing_categories = dict(
        [
            (c.heading, {"node": c, "body": c.get_body(format="raw")})
            for c in workflows.children
        ]
    )
    existing_categories_names = existing_categories.keys()

    # remote
    source_file = TOOLCHEST_PATHS["workflows"]["source"]
    df = pd.read_json(source_file).replace(np.nan, "", regex=True)
    gg = df.groupby("Category")
    for name, group in gg.groups.items():
        if name not in existing_categories_names:
            continue
        # items_in_cat = len(list(group))
        tool_indexes = list(group)
        rows = []
        extra_resources = []
        for t in tool_indexes:
            row = dict(df.iloc[t])
            final_cells = {
                "name": f"[[{row['URL']}][{row['Name']}]]",
                "remark": row["Remark"].strip(),
            }
            final_row = "| {name} | {remark} |".format(**final_cells)
            # NOTE: Value of is_primary is either ''(falsy) or 1.0. So we can just check for the truthy
            if row["is_primary"]:
                rows.append(final_row)
            else:
                extra_resources.append(final_row)
            # rows.append(final_row)
        existing_categories[name]["rows"] = rows
        existing_categories[name]["extra_resources"] = extra_resources
        # existing_categories[name]["category_name_with_freq"] = f"{name}({len(rows)})"
        existing_categories[name]["category_name_with_freq"] = name

    # write final file
    dest_file = TOOLCHEST_PATHS["workflows"]["destination"]
    with open(dest_file, "w", encoding="utf-8") as f:
        for cat, info in existing_categories.items():
            info["category_name_with_freq"]
            f.write(f"\n* {info['category_name_with_freq']}\n")
            # main body from org file
            f.write(info["body"])

            if len(info["rows"]):
                # primary tools
                f.write(
                    """\n
                    #+attr_html: :class book-hint info small-text mb-2
                    #+begin_details
                    #+begin_summary
                    Primary Tools
                    #+end_summary
                    """
                )
                f.write("| Name | Remark |\n")
                for t in info["rows"]:
                    f.write(f"{t}\n")
                f.write("#+end_details\n")

            if len(info["extra_resources"]):
                # extra info
                f.write(
                    """\n\n
                    #+attr_html: :class book-hint warning small-text
                    #+begin_details
                    #+begin_summary
                    Additional Resources/Tools
                    #+end_summary
                    """
                )
                f.write("| Name | Remark |\n")
                for t in info["extra_resources"]:
                    f.write(f"{t}\n")
                f.write("#+end_details\n")


# Deprecated
# NOTE: Used to call this method in main and it would create a nice workflow.org
# in the assets/org-include directory but the format was very cumbersome as I
# could not see what I needed to see and because half the data came from
# airtable it became hard to annotate it my style. So basically deprecating this
# but still keeping the function for a while because the utility itself is
# useful and might need somewhere else
# NOTE: When removing this method, might as well extract it out into something
# solid rather than completely getting rid of it
# NOTE: This also removes the following from the makefile. The airtable table
# will stay for a while.
# airtable-export ${TEMP_DIR} appHCIWcQJnvFYG2n workflows --json
def populate_workflow():
    populate_workflows_file()
    populate_final_workflows_file()


def main():
    process_toolchest_file()
    process_mobile_apps_file()


if __name__ == "__main__":
    main()
