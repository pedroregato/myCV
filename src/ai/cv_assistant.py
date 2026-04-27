"""
CV Assistant — uses Claude API to help maintain and improve Pedro Gentil's CV.

Features:
- improve_bullet: rewrites a rough description as a polished CV bullet
- translate: translates CV text between PT and EN
- review_section: reviews a section and suggests improvements
- draft_linkedin_post: generates a LinkedIn post draft
- suggest_yaml_update: suggests a YAML snippet to add to the profile
"""

import os
import anthropic
from dotenv import load_dotenv
from src.ai import prompts

load_dotenv()

MODEL = "claude-sonnet-4-6"
MAX_TOKENS = 1024


def _client() -> anthropic.Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key."
        )
    return anthropic.Anthropic(api_key=api_key)


def _ask(user_prompt: str, system: str = prompts.SYSTEM_CV_EXPERT, max_tokens: int = MAX_TOKENS) -> str:
    client = _client()
    message = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return message.content[0].text.strip()


def improve_bullet(description: str, context: str = "experiência profissional", lang: str = "pt") -> str:
    """
    Rewrites a rough description as a polished CV bullet point.

    Args:
        description: Raw description of the achievement or activity.
        context:     Which CV section this belongs to (for tone guidance).
        lang:        'pt' or 'en'.

    Returns:
        A single polished bullet point string.
    """
    template = prompts.IMPROVE_BULLET_PT if lang == "pt" else prompts.IMPROVE_BULLET_EN
    prompt = template.format(description=description, context=context)
    return _ask(prompt)


def translate(text: str, target_lang: str = "en") -> str:
    """
    Translates CV text between PT and EN.

    Args:
        text:        The text to translate.
        target_lang: 'en' (from PT) or 'pt' (from EN).

    Returns:
        Translated text preserving structure and tone.
    """
    if target_lang == "en":
        prompt = prompts.TRANSLATE_TO_EN.format(text=text)
    else:
        prompt = prompts.TRANSLATE_TO_PT.format(text=text)
    return _ask(prompt, max_tokens=2048)


def review_section(section_name: str, content: str, lang: str = "pt") -> str:
    """
    Reviews a CV section and suggests improvements.

    Args:
        section_name: Name of the section (e.g. 'resumo_texto', 'destaques').
        content:      Current text content of the section.
        lang:         'pt' or 'en'.

    Returns:
        Analysis with strengths, suggestions, and revised version.
    """
    template = prompts.REVIEW_SECTION_PT if lang == "pt" else prompts.REVIEW_SECTION_EN
    prompt = template.format(section=section_name, content=content)
    return _ask(prompt, max_tokens=2048)


def draft_linkedin_post(achievement: str, post_type: str = "case", lang: str = "pt") -> str:
    """
    Generates a LinkedIn post draft based on an achievement or topic.

    Args:
        achievement: Description of the achievement, project, or topic.
        post_type:   'case', 'tecnico' / 'technical', or 'reflexao' / 'reflection'.
        lang:        'pt' or 'en'.

    Returns:
        A ready-to-publish LinkedIn post string.
    """
    template = prompts.LINKEDIN_POST_PT if lang == "pt" else prompts.LINKEDIN_POST_EN
    prompt = template.format(achievement=achievement, post_type=post_type)
    return _ask(prompt, max_tokens=1024)


def suggest_yaml_update(section: str, description: str, example: str = "") -> str:
    """
    Suggests a YAML snippet to add to the PT profile based on a description.
    The caller should review and apply it manually to the YAML file.

    Args:
        section:     Target section key (e.g. 'destaques', 'experiencia', 'publicacoes').
        description: What happened — in plain language.
        example:     Optional: paste the current YAML block of that section as reference.

    Returns:
        A YAML snippet ready to be added to data/profile_pt.yaml.
    """
    prompt = prompts.SUGGEST_YAML_UPDATE_PT.format(
        section=section,
        description=description,
        example=example or "(see the existing structure in data/profile_pt.yaml)",
    )
    return _ask(prompt, max_tokens=1024)
