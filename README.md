# Zim Child Links Generator

A small Python utility for generating Zim wiki links to the direct child pages of a specified page.

The script scans a Zim notebook, finds all pages that are immediate children of the specified parent page, sorts them alphabetically, and prints their links using Zim's `+` relative-link syntax.

## What it does

Suppose a notebook contains:

```text
1 Дневник:2026
1 Дневник:2026:01
1 Дневник:2026:02
1 Дневник:2026:03
1 Дневник:2026:01:01
1 Дневник:2026:01:02
```

If the parent page is:

```text
1 Дневник:2026
```

the script prints:

```text
[[+01]]
[[+02]]
[[+03]]
```

The pages `01` and `02` under `1 Дневник:2026:01` are not included because they are grandchildren, not direct children of the specified page.

## Usage

The script expects two command-line arguments:

1. The Zim page name whose direct children should be listed.
2. The path to the Zim notebook.

```bash
python3 zim_child_links.py "PAGE_NAME" "/path/to/notebook"
```

Example:

```bash
python3 zim_child_links.py "1 Дневник:2026" "/home/user/My Notebook"
```

Output:

```text
[[+01]]
[[+02]]
[[+03]]
```

The output can be copied directly into a Zim page.

## How it works

The script:

1. Opens the specified Zim notebook.
2. Looks through all indexed pages.
3. Selects pages whose names begin with:

```text
PAGE_NAME:
```

4. Removes the parent page prefix.
5. Keeps only pages whose remaining name contains no additional `:`.
6. Sorts the resulting child pages alphabetically.
7. Prints each child as a Zim relative link:

```text
[[+Child Page]]
```

The `+` syntax is intentional: in Zim, `[[+Child Page]]` refers to a child page relative to the current page.

## Important

The script only **prints** the generated links. It does not modify the notebook or any of its files.

It is therefore safe to use for generating lists of links that can then be inserted into Zim manually or used by another script.

## Requirements

* Python 3
* Zim Desktop Wiki
* Zim's Python modules available to Python

The script was developed for Zim 0.77.x.

## Typical use case

This utility is useful when a page has many direct subpages and you want to quickly create a list of links to them.

For example, a monthly page may contain:

```text
2026:09
2026:09:01
2026:09:02
2026:09:03
...
2026:09:30
```

Running the script for `2026:09` produces:

```text
[[+01]]
[[+02]]
[[+03]]
...
[[+30]]
```

The generated block can then be inserted into the parent page.
