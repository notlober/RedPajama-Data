import json
from pathlib import Path
from typing import Dict, Set

_DEFAULT_LANGS = ("en", "fr", "it", "es", "de", "tr")


def load_bad_urls_index(bad_urls_dir: Path) -> Dict[str, int]:
    with open(bad_urls_dir / "domain_to_category_id.json", "r") as f:
        domain_to_category_id = json.load(f)
    return domain_to_category_id

def load_bad_urls_index_tr(bad_urls_file: Path) -> Dict[str, int]:
    domain_to_category_id = {}
    with open(bad_urls_file, "r") as f:
        for i, line in enumerate(f):
            domain = line.strip()  # Extract the domain directly 
            domain_to_category_id[domain] = i  # Assign a unique category ID
    return domain_to_category_id

def load_bad_words(bad_words_dir: Path, lang: str) -> Set[str]:
    r""" load the LDNOOBW word list for a given language

    Source:
        https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words

    Args:
        bad_words_dir (Path): The path to the resources directory where the
            list is stored
        lang (str): The language for which to fetch the word list

    Returns:
        A set of words
    """
    if lang == "tr":
        with open(bad_words_dir / f"{lang}.txt", "r") as f:  # Load from tr.txt
            data = f.readlines()
            return set(line.strip() for line in data)  # Strip newlines

    if lang not in _DEFAULT_LANGS:
        return set()

    ldnoobw_fp = bad_words_dir / f"{lang}.txt"

    if not ldnoobw_fp.exists():
        raise FileNotFoundError(f"LDNOOBW word list {ldnoobw_fp} not found!")

    with open(ldnoobw_fp, 'r') as f:
        data = set(ln.strip() for ln in f.readlines())

    return data
