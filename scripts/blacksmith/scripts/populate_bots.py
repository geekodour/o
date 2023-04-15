#!/usr/bin/env python3
# this translates my tw bot list on airtable to org mode file
import os
import numpy as np
import pandas as pd


BOT_PATHS = {
    "source": os.path.join(os.environ["TEMP_DIR"], "tw_bots.json"),
    "destination": os.path.join(os.environ["ORG_DIR"], "tw_bots.org"),
}


def process_bots():
    source_file = BOT_PATHS["source"]
    df = pd.read_json(source_file).replace(np.nan, "", regex=True)
    df = df.assign(org_link="[[" + df["Link"] + "][" + df["username"] + "]]")
    df = df[["org_link", "Description"]]
    df["Description"] = df["Description"].str.replace(
        "|", ".", regex=False
    )  # org table uses pipes for sep.

    dest_file = BOT_PATHS["destination"]
    with open(dest_file, "w", encoding="utf-8") as f:
        f.write("| Name | Description |\n")
        for i, row in df.iterrows():
            f.write(f"| {row['org_link']} | {row['Description']} |\n")


process_bots()
