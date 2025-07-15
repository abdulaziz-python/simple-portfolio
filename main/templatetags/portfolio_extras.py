from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def split(value, delimiter=','):
    """Split a string by delimiter and return a list"""
    if not value:
        return []
    return [item.strip() for item in str(value).split(delimiter) if item.strip()]

@register.filter
def trim(value):
    """Remove whitespace from both ends of a string"""
    if not value:
        return ''
    return str(value).strip()

@register.filter
def highlight_code(value):
    """Add syntax highlighting to code snippets"""
    if not value:
        return ''
    
    # Simple syntax highlighting for Python-like code
    patterns = [
        (r'\b(def|class|import|from|if|else|elif|for|while|try|except|finally|with|as|return|yield|break|continue|pass|lambda|global|nonlocal)\b', 
         r'<span style="color: var(--terminal-blue);">\1</span>'),
        (r'\b(True|False|None)\b', 
         r'<span style="color: var(--terminal-purple);">\1</span>'),
        (r'(#.*$)', 
         r'<span style="color: var(--terminal-green);">\1</span>'),
        (r'(["\'].*?["\'])', 
         r'<span style="color: var(--warning-color);">\1</span>'),
        (r'\b(\d+)\b', 
         r'<span style="color: var(--terminal-orange);">\1</span>'),
    ]
    
    result = str(value)
    for pattern, replacement in patterns:
        result = re.sub(pattern, replacement, result, flags=re.MULTILINE)
    
    return mark_safe(result)

@register.filter
def get_skill_icon(skill):
    """Get appropriate icon for a skill"""
    skill_lower = str(skill).lower()
    
    icon_map = {
        'python': 'fab fa-python',
        'django': 'fas fa-server',
        'tensorflow': 'fas fa-brain',
        'ai': 'fas fa-brain',
        'ml': 'fas fa-brain',
        'machine learning': 'fas fa-brain',
        'docker': 'fab fa-docker',
        'git': 'fab fa-git-alt',
        'github': 'fab fa-github',
        'postgresql': 'fas fa-database',
        'database': 'fas fa-database',
        'telegram': 'fas fa-robot',
        'bot': 'fas fa-robot',
        'api': 'fas fa-plug',
        'rest': 'fas fa-plug',
        'javascript': 'fab fa-js',
        'html': 'fab fa-html5',
        'css': 'fab fa-css3-alt',
        'react': 'fab fa-react',
        'node': 'fab fa-node-js',
        'linux': 'fab fa-linux',
        'aws': 'fab fa-aws',
        'redis': 'fas fa-memory',
        'celery': 'fas fa-tasks',
    }
    
    for key, icon in icon_map.items():
        if key in skill_lower:
            return icon
    
    return 'fas fa-code'

@register.filter
def markdown_to_html(value):
    """Convert basic markdown to HTML"""
    if not value:
        return ''
    
    # Simple markdown conversion
    result = str(value)
    
    # Bold text
    result = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', result)
    
    # Italic text
    result = re.sub(r'\*(.*?)\*', r'<em>\1</em>', result)
    
    # Code blocks
    result = re.sub(r'`(.*?)`', r'<code>\1</code>', result)
    
    # Line breaks
    result = result.replace('\n', '<br>')
    
    return mark_safe(result)

@register.simple_tag
def get_social_icon(platform):
    """Get social media icon"""
    icons = {
        'github': 'fab fa-github',
        'telegram': 'fab fa-telegram',
        'twitter': 'fab fa-twitter',
        'linkedin': 'fab fa-linkedin',
        'instagram': 'fab fa-instagram',
        'facebook': 'fab fa-facebook',
        'youtube': 'fab fa-youtube',
        'blog': 'fas fa-blog',
        'channel': 'fas fa-broadcast-tower',
        'email': 'fas fa-envelope',
    }
    return icons.get(platform.lower(), 'fas fa-link')

@register.inclusion_tag('components/skill_card.html')
def skill_card(skill, icon=None):
    """Render a skill card component"""
    return {
        'skill': skill,
        'icon': icon or get_skill_icon(skill),
    }

@register.inclusion_tag('components/project_card.html')
def project_card(project):
    """Render a project card component"""
    return {'project': project}
