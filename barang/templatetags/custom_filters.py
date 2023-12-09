from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    classes = value.field.widget.attrs.get('class', '').split()
    classes.extend(arg.split())
    value.field.widget.attrs['class'] = ' '.join(classes)
    return value