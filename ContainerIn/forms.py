from django import forms
from ContainerIn.models import *

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
