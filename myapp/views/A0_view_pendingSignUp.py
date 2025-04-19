from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from myapp.forms import SignUpForm, LoginForm
from myapp.models import UserProfile
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def approval_pending(request):
    return render(request, 'A0_view_pendingSignUp.html')


