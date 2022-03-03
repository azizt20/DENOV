from django import template

register = template.Library()

@register.filter()
def fortwo(value):
    qwe =value[len(value)-2:len(value)]
    return reversed(qwe)


@register.filter()
def forfour(value):
    qwe =value[len(value)-6:len(value)-2]
    return reversed(qwe)


