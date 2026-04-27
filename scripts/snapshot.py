"""
Creates a versioned snapshot of the current CV profile files.

Usage:
    python scripts/snapshot.py --message "Adicionei novo projeto X na FGV"
    python scripts/snapshot.py  # uses a generic message
"""

import argparse
import os
import re
import shutil
import sys
from datetime import date

HISTORY_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'history')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
CHANGELOG = os.path.join(HISTORY_DIR, 'changelog.md')


def _next_version() -> int:
    """Returns the next version number based on existing snapshot folders."""
    if not os.path.exists(HISTORY_DIR):
        return 1
    pattern = re.compile(r'^v(\d+)_')
    versions = [
        int(pattern.match(d).group(1))
        for d in os.listdir(HISTORY_DIR)
        if pattern.match(d)
    ]
    return max(versions, default=0) + 1


def create_snapshot(message: str):
    today = date.today().isoformat()
    version = _next_version()
    folder_name = f"v{version}_{today}"
    snapshot_dir = os.path.join(HISTORY_DIR, folder_name)

    os.makedirs(snapshot_dir, exist_ok=True)

    for lang in ('pt', 'en'):
        src = os.path.join(DATA_DIR, f'profile_{lang}.yaml')
        dst = os.path.join(snapshot_dir, f'profile_{lang}.yaml')
        if os.path.exists(src):
            shutil.copy2(src, dst)

    # Append to changelog
    entry = f"\n## v{version} — {today}\n\n{message}\n"
    with open(CHANGELOG, 'a', encoding='utf-8') as f:
        f.write(entry)

    print(f"Snapshot criado: data/history/{folder_name}/")
    print(f"Changelog atualizado: data/history/changelog.md")


def main():
    parser = argparse.ArgumentParser(description='Create a versioned CV snapshot.')
    parser.add_argument('--message', '-m', default='Atualização do CV.',
                        help='Description of what changed in this version.')
    args = parser.parse_args()
    create_snapshot(args.message)


if __name__ == '__main__':
    main()
