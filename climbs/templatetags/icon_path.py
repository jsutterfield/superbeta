from django import template
register = template.Library()

@register.filter
def icon_path(icon):
    return "images/weather_images/{0}.gif".format(icon)