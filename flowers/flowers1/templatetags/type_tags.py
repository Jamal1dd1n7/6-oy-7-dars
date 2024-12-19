from django import template
from ..models import Type1
register = template.Library()

@register.simple_tag
def all_types():
    return Type1.objects.all()