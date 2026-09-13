#!/usr/bin/env python3

import sys
from zim.notebook import Notebook
from zim.newfs import LocalFolder


def main():
    page_name = sys.argv[1]
    notebook_path = sys.argv[2]

    nb = Notebook.new_from_dir(LocalFolder(notebook_path))

    prefix = page_name + ":"
    children = []

    for p in nb.pages.walk():
        if not p.name.startswith(prefix):
            continue

        rest = p.name[len(prefix):]
        if ":" in rest:
            continue

        children.append(p)

    children.sort(key=lambda x: x.name.lower())

    for p in children:
        short = p.name.rsplit(":", 1)[-1]
        print(f"[[+{short}]]")


if __name__ == "__main__":
    main()
