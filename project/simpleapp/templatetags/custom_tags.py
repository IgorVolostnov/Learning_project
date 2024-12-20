import datetime

from django import template


register = template.Library()


@register.simple_tag()
def current_time(format_string='%b %d %Y'):
   return datetime.datetime.strftime(datetime.datetime.now(), format_string)