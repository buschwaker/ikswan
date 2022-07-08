from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    """Фильтр,
    добавляет аттрибуту класс значение переданное к качестве аргумента"""
    return field.as_widget(attrs={'class': css})
