from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField


class ApplyButton(forms.Form):
    # Define the field for the button
    ApplyButtonMode = forms.CharField(
        label='',  # No label for the button
        widget=forms.TextInput(attrs={
            'type': 'submit',  # Use 'submit' to make this a submit button
            'value': 'Apply',    # Button display text
            'name': 'action',  # Include the 'name' attribute as in the original HTML
            'id': 'runButton'  # Include the 'id' attribute as in the original HTML
        })
    )




class StartButton(forms.Form):
    # Define the field for the button
    StartButtonMode = forms.CharField(
        label='',  # No label for the button
        widget=forms.TextInput(attrs={
            'type': 'submit',  # Use 'submit' to make this a submit button
            'value': 'START CEKG',    # Button display text
            'name': 'action',  # Include the 'name' attribute as in the original HTML
            'id': 'startButton'  # Include the 'id' attribute as in the original HTML
        })
    )




class RunButton(forms.Form):
    # Define the field for the button
    RunButtonMode = forms.CharField(
        label='',  # No label for the button
        widget=forms.TextInput(attrs={
            'type': 'submit',  # Use 'submit' to make this a submit button
            'value': 'Run',    # Button display text
            'name': 'action',  # Include the 'name' attribute as in the original HTML
            'id': 'runButton'  # Include the 'id' attribute as in the original HTML
        })
    )




class NxButton(forms.Form):
    # Define the field for the button
    NxButtonMode = forms.CharField(
        label='',  # No label for the button
        widget=forms.TextInput(attrs={
            'type': 'submit',  # Use 'submit' to make this a submit button
            'value': 'Next',    # Button display text
            'name': 'action',  # Include the 'name' attribute as in the original HTML
            'id': 'runButton'  # Include the 'id' attribute as in the original HTML
        })
    )


class RsButton(forms.Form):
    # Define the field for the button
    RsButtonMode = forms.CharField(
        label='',  # No label for the button
        widget=forms.TextInput(attrs={
            'type': 'submit',  # Use 'submit' to make this a submit button
            'value': 'Result',    # Button display text
            'name': 'action',  # Include the 'name' attribute as in the original HTML
            'id': 'runButton'  # Include the 'id' attribute as in the original HTML
        })
    )



class BroweserButton(forms.Form):
    BroweserButtonMode = forms.CharField(
        label = '',
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'FINISH'})
    )


