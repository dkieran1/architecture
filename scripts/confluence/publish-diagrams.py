import sys
import argparse
import glob
from pathlib import Path
from atlassian import Confluence
import magic

# Setup args
parser = argparse.ArgumentParser()
parser.add_argument("username", type=str, help="Confluence user")
parser.add_argument("password", type=str, help="API access token")
parser.add_argument("url", type=str, help="Confluence URL")
parser.add_argument("space", type=str, help="Confluence space key")
parser.add_argument("path", type=str, help="Path to diagrams")
parser.add_argument("imgext", type=str, help="Image type/extension to publish")
parser.add_argument("parentid", type=int, help="Confluence parent page id to create/update page under")
args = parser.parse_args()

confluence = Confluence(
    url=args.url,
    username=args.username,
    password=args.password
)

# Assuming that the images will be png (which is default output from plantuml)
# TODO consider writing a check to validate, doesn't seem useful to add more code for it...
diagrams = glob.glob(args.path + "/*." + args.imgext)

for diagram in diagrams:

    # Html to embed image in page and use full width
    img = '<ac:image ac:width="100%"><ri:attachment ri:filename="' + Path(diagram).name + '" /></ac:image>'

    status = confluence.update_or_create(
        title=Path(diagram).stem,
        body=str(img),
        parent_id=args.parentid
    )

    content_type = magic.from_file(diagram, mime=True)
    page_id = confluence.get_page_by_title(space=args.space, title=Path(diagram).stem).get("id") or None

    # Could check id exists, but I'd just make it throw an exception anyway, which it'll do, so doesn't seem useful

    status = confluence.attach_file(
        filename=diagram, 
        name=Path(diagram).name, 
        content_type=content_type, 
        page_id=page_id, 
        space=args.space
    )