from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
import re

register = template.Library()

@stringfilter
@register.tag
@register.filter(needs_autoescape=True)
def paragraphs(value, autoescape=None):
    """
    Turns paragraphs delineated with newline characters into
    paragraphs wrapped in <p> and </p> HTML tags.
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    paras = re.split(r'[\r\n]+', value)
    paras = ['<p>%s</p>' % esc(p.strip()) for p in paras]
    return mark_safe('\n'.join(paras))
