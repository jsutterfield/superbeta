from django import template
register = template.Library()

@register.filter
def lt(a, b):
    return a < b