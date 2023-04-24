from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name title'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons title'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date public'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text title'
            }),
        }