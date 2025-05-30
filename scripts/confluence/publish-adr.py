import sys
import argparse
import glob
from pathlib import Path
from atlassian import Confluence
import markdown

# Setup args
parser = argparse.ArgumentParser()
parser.add_argument("username", type=str, help="Confluence user")
parser.add_argument("password", type=str, help="API access token")
parser.add_argument("url", type=str, help="Confluence URL")
parser.add_argument("space", type=str, help="Confluence space key")
parser.add_argument("path", type=str, help="Path to ADRs")
parser.add_argument("parentid", type=int, help="Confluence parent page id to create/update page under")
args = parser.parse_args()

confluence = Confluence(
    url=args.url,
    username=args.username,
    password=args.password
)

# Only accept files with a data in the 20's and is a number 8 digits long followed by a hyphen
adrs = glob.glob(args.path + "/20"+ ('[0-9]' * 6) + "-*.md")

for adr in adrs:
    data = open(adr, "r").read()
    html = markdown.markdown(data)
    
    # Idempotent upsert
    status = confluence.update_or_create(
        title=Path(adr).stem,
        body=str(html),
        parent_id=args.parentid
    )