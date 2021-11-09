from django import forms
from .models import CustomSettings


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = CustomSettings
        fields = ['id_provider', 'photo']