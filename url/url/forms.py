from django import forms
from .models import UrlShortener

class UrlShortenerForm(forms.ModelForm):
    class Meta:
        model = UrlShortener
        fields = ['long_url']
        widgets = {
            'long_url': forms.URLInput(attrs={'placeholder': 'Long URL'}),
        }
