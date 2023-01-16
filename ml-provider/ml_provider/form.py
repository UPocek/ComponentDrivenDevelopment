from django import forms
from django.core.validators import FileExtensionValidator

class JsonNeuralNetworkForm(forms.Form):
    title = forms.CharField(max_length=50)
    file_content = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=["json"])])
    