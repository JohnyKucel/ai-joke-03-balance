"""Write the competition joke entry to a text file.

Writes entry.txt into the output directory named by the
MAKEFUN_OUTPUT_DIR environment variable, or /output when unset.
"""

import os

ENTRY_FILENAME = "entry.txt"

JOKE = "I planned my whole year in January \u2014 my bank balance rewrote it by February."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, ENTRY_FILENAME)
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
