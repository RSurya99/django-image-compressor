from django.forms import ModelForm
from django import forms
from .models import ImageCompressor

class FormCompressor(ModelForm):
    image_file = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                "class": "form-control-file"
            }))

    class Meta:
        model = ImageCompressor
        fields = ['image_file']