from django import template

register=template.Library()

@register.filter
def subtotal(item):
    return item.product.price * item.quantity

@register.filter
def totalsum(ordered_items):
    total=0
    for item in ordered_items:
         total=total+(item.product.price*item.quantity)
    return total