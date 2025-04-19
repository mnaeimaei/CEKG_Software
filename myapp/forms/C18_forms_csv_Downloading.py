from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json

import os


class DownButton(forms.Form):
    downButtonMode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'Download CSV Files'})
    )



