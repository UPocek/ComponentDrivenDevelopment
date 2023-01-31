from django import forms
from django.core.validators import FileExtensionValidator


class XmlParserUploadForm(forms.Form):
    graph_name = forms.CharField(max_length=50)
    graph_description = forms.CharField(max_length=50)
    file_content = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=["xml"])])
