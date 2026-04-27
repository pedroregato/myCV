"""
Interactive CLI to update the CV with Claude AI assistance.

Usage:
    python scripts/update_with_ai.py bullet
    python scripts/update_with_ai.py review  --section resumo_texto --lang pt
    python scripts/update_with_ai.py translate --section resumo_texto --from-lang pt
    python scripts/update_with_ai.py yaml-update --section destaques
    python scripts/update_with_ai.py post --type case --lang pt
"""

import argparse
import os
import sys
import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.ai.cv_assistant import improve_bullet, review_section, translate, suggest_yaml_update, draft_linkedin_post

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


def _load_profile(lang: str) -> dict:
    path = os.path.join(DATA_DIR, f'profile_{lang}.yaml')
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)


def _get_section_content(profile: dict, section: str) -> str:
    value = profile.get(section)
    if value is None:
        return ""
    if isinstance(value, list):
        return yaml.dump(value, allow_unicode=True, default_flow_style=False)
    return str(value)


def cmd_bullet(args):
    print("\nDescreva a conquista ou atividade (pode ser informal, em PT ou EN):")
    description = input("> ").strip()
    print(f"\nEm qual seção ficaria? (ex: experiencia FGV, destaques, publicacoes) [experiência profissional]:")
    context = input("> ").strip() or "experiência profissional"

    print(f"\nIdioma do bullet [pt/en, default: pt]:")
    lang = input("> ").strip() or "pt"

    print("\nConsultando Claude...\n")
    result = improve_bullet(description, context=context, lang=lang)
    print("=" * 60)
    print("SUGESTAO DE BULLET:")
    print()
    print(f"  - {result}")
    print("=" * 60)
    print("\nCopie e adicione ao arquivo data/profile_pt.yaml (ou en) na secao correta.")


def cmd_review(args):
    lang = args.lang or "pt"
    profile = _load_profile(lang)
    section = args.section

    if section not in profile:
        print(f"Secao '{section}' nao encontrada no profile_{lang}.yaml.")
        print(f"Secoes disponíveis: {', '.join(profile.keys())}")
        sys.exit(1)

    content = _get_section_content(profile, section)
    print(f"\nRevisando secao '{section}' ({lang.upper()}) com Claude...\n")
    result = review_section(section, content, lang=lang)
    print("=" * 60)
    print(result)
    print("=" * 60)


def cmd_translate(args):
    from_lang = args.from_lang or "pt"
    to_lang = "en" if from_lang == "pt" else "pt"
    section = args.section

    profile = _load_profile(from_lang)
    if section not in profile:
        print(f"Secao '{section}' nao encontrada no profile_{from_lang}.yaml.")
        sys.exit(1)

    content = _get_section_content(profile, section)
    print(f"\nTraduzindo '{section}' de {from_lang.upper()} para {to_lang.upper()}...\n")
    result = translate(content, target_lang=to_lang)
    print("=" * 60)
    print(f"TRADUCAO ({to_lang.upper()}):")
    print()
    print(result)
    print("=" * 60)
    print(f"\nRevise e cole em data/profile_{to_lang}.yaml na secao '{section}'.")


def cmd_yaml_update(args):
    section = args.section
    profile_pt = _load_profile("pt")
    example = _get_section_content(profile_pt, section) if section in profile_pt else ""

    print(f"\nDescreva o que aconteceu para adicionar em '{section}':")
    description = input("> ").strip()

    print("\nConsultando Claude...\n")
    result = suggest_yaml_update(section, description, example=example)
    print("=" * 60)
    print("SUGESTAO DE YAML (adicionar em data/profile_pt.yaml):")
    print()
    print(result)
    print("=" * 60)
    print("\nRevise, ajuste se necessario, e adicione ao arquivo YAML.")
    print("Depois regenere os PDFs: python scripts/generate_cv.py")


def cmd_post(args):
    lang = args.lang or "pt"
    post_type = args.type or "case"

    print("\nDescreva o tema ou conquista para o post do LinkedIn:")
    achievement = input("> ").strip()

    print(f"\nGerando post ({post_type}, {lang.upper()}) com Claude...\n")
    result = draft_linkedin_post(achievement, post_type=post_type, lang=lang)
    print("=" * 60)
    print("RASCUNHO DO POST LINKEDIN:")
    print()
    print(result)
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description='CV AI Assistant — powered by Claude.')
    sub = parser.add_subparsers(dest='command', required=True)

    sub.add_parser('bullet', help='Reescreve uma descricao como bullet profissional')

    p_review = sub.add_parser('review', help='Revisa uma secao do CV')
    p_review.add_argument('--section', required=True, help='Chave da secao no YAML (ex: resumo_texto)')
    p_review.add_argument('--lang', default='pt', choices=['pt', 'en'])

    p_translate = sub.add_parser('translate', help='Traduz uma secao entre PT e EN')
    p_translate.add_argument('--section', required=True, help='Chave da secao no YAML')
    p_translate.add_argument('--from-lang', default='pt', choices=['pt', 'en'])

    p_yaml = sub.add_parser('yaml-update', help='Sugere YAML para nova entrada no CV')
    p_yaml.add_argument('--section', required=True, help='Secao alvo (ex: destaques, experiencia)')

    p_post = sub.add_parser('post', help='Gera rascunho de post para o LinkedIn')
    p_post.add_argument('--type', default='case', choices=['case', 'tecnico', 'technical', 'reflexao', 'reflection'])
    p_post.add_argument('--lang', default='pt', choices=['pt', 'en'])

    args = parser.parse_args()

    commands = {
        'bullet': cmd_bullet,
        'review': cmd_review,
        'translate': cmd_translate,
        'yaml-update': cmd_yaml_update,
        'post': cmd_post,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()
