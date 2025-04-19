from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class LoginButton(forms.Form):
    LoginButtonMode = forms.CharField(
        label='Click to Login',
        widget=forms.TextInput(attrs={'type': 'submit', 'value': 'Login'})
    )


class SignUpForm(UserCreationForm):

    username = forms.CharField(
        max_length=150,
        required=True,
        help_text=' ',
        label='Username'
    )

    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='',
        label='Email Address'
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        help_text=(
            'Your password must contain at least 8 characters,<br>'
            'can’t be too similar to your other personal information,<br>'
            'can’t be a commonly used password,<br>'
            'and can’t be entirely numeric.'
        ),
        label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        help_text='Enter the same password as before, for verification.',
        label='Confirm Password'
    )

    organization = forms.CharField(
        max_length=255,
        required=True,
        help_text='Please enter the name of your organization, university, or research institute.',
        label='Organization/University'
    )

    request_text = forms.CharField(
        widget=forms.Textarea,
        required=True,
    help_text = 'Please provide a brief explanation of yourself and your intention to use the CEKG tool.',
    label = 'Request text'

    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'organization', 'request_text')

class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)