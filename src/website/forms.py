from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput())

    class Meta:
        model = Photo
        fields = ("file",)
