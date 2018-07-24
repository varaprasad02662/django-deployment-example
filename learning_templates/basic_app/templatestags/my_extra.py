from django import template

register = template.Library()

#We register by using Decorator also
@register.filter(name="cut")
def cut(value,arg):
    return value.replace(arg,'')


# register.filter("cut",cut)
