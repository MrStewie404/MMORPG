from django import template
from ..models import User, Ads

register = template.Library()

@register.filter
def len_text(context):
    """Returns the length of a string"""
    return len(context)

@register.filter
def ad_is_exist(username_create):
    return (Ads.objects.get(username=username_create))