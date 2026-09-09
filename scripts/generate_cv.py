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
PHOTO_PATH = os.path.join(os.path.dirname(__file__), '..', 'assets', 'FotoCV.png')

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


def generate_custom(data_file, output_file):
    with open(data_file, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    create_cv(output_file, data, photo_path=PHOTO_PATH)
    print(f"Generated: {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Generate CV PDFs from YAML data.')
    parser.add_argument('--lang', choices=['pt', 'en', 'all'], default='all',
                        help='Language to generate (default: all)')
    parser.add_argument('--data-file', help='Custom YAML data file (overrides --lang)')
    parser.add_argument('--output-file', help='Custom output PDF path (used with --data-file)')
    args = parser.parse_args()

    if args.data_file or args.output_file:
        if not (args.data_file and args.output_file):
            parser.error('--data-file and --output-file must be used together')
        generate_custom(args.data_file, args.output_file)
        return

    langs = ['pt', 'en'] if args.lang == 'all' else [args.lang]
    for lang in langs:
        generate(lang)


if __name__ == '__main__':
    main()
