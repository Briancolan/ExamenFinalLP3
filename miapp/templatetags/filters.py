from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo(valor):
    return f"<h1 style='background:red; color:black;'> Bienvenido, {valor} </h1>"