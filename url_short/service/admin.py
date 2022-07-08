from django.contrib import admin

from .models import URL


class URLAdmin(admin.ModelAdmin):
    """Отображение объектов модели URL"""
    list_display = (
        'pk',
        'full_url',
        'short_url',
        'user'

    )


admin.site.register(URL, URLAdmin)
