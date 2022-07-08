from django import forms

from .models import URL


class UrlForm(forms.ModelForm):
    """Форма, связанная с моделью URL"""
    class Meta:
        model = URL
        fields = ['full_url', ]
