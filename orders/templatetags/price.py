from django import template

register=template.Library()

@register.filter
def price(price,quantity):
    return price*quantity