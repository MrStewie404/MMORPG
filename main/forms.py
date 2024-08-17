from django import forms
from .models import Ads, Reviews
from django.core.exceptions import ValidationError
class AdForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text_input'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'title_input'}))

    class Meta:
        model = Ads
        fields = [
            'title', 
            'text', 
            'content_type'
        ]

class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text_input'}))
    class Meta:
        model = Reviews
        fields = [
            'text', 
        ]