"""
Entry point: loads CV data from YAML files and generates PDFs.

Usage:
    python scripts/generate_cv.py
    python scripts/generate_cv.py --lang pt
    python scripts/generate_cv.py --lang en
"""

import argparse
import os
import sys
import yaml

# Allow running from project root or from scripts/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.generators.pdf_generator import create_cv

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')
PHOTO_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'FotoLinkedin.png')

CONFIGS = {
    'pt': {
        'data_file': os.path.join(DATA_DIR, 'profile_pt.yaml'),
        'output_file': os.path.join(OUTPUT_DIR, 'Curriculo_Pedro_Gentil.pdf'),
    },
    'en': {
        'data_file': os.path.join(DATA_DIR, 'profile_en.yaml'),
        'output_file': os.path.join(OUTPUT_DIR, 'Resume_Pedro_Gentil.pdf'),
    },
}


def load_profile(lang):
    config = CONFIGS[lang]
    with open(config['data_file'], encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate(lang):
    config = CONFIGS[lang]
    data = load_profile(lang)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    create_cv(config['output_file'], data, photo_path=PHOTO_PATH)
    print(f"[{lang.upper()}] Generated: {config['output_file']}")


def main():
    parser = argparse.ArgumentParser(description='Generate CV PDFs from YAML data.')
    parser.add_argument('--lang', choices=['pt', 'en', 'all'], default='all',
                        help='Language to generate (default: all)')
    args = parser.parse_args()

    langs = ['pt', 'en'] if args.lang == 'all' else [args.lang]
    for lang in langs:
        generate(lang)


if __name__ == '__main__':
    main()
