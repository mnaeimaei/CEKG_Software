from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from myapp.forms import SignUpForm, LoginForm
from myapp.models import UserProfile
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")

def signPage(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an signPage view and A0_view_singUpIn.html")
    if request.method == 'POST':
        logger.info(f"################ request.method == 'POST' ################")
        if 'signup' in request.POST:
            signup_form = SignUpForm(request.POST)
            login_form = LoginForm()
            if signup_form.is_valid():
                user = signup_form.save()
                user.refresh_from_db()
                user.userprofile.organization = signup_form.cleaned_data.get('organization')
                user.userprofile.request_text = signup_form.cleaned_data.get('request_text')
                user.save()
                send_mail(
                    'New Sign-Up Request',
                    f'User {user.username} (Email: {user.email}) has requested to sign up with the following information:\n\n'
                    f'Organization: {user.userprofile.organization}\n'
                    f'Request Text: {user.userprofile.request_text}',
                    settings.DEFAULT_FROM_EMAIL,
                    ['m.naeimaei@gmail.com'],
                )
                return redirect('signup_success')
        elif 'login' in request.POST:
            signup_form = SignUpForm()
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if user.userprofile.is_approved:
                        create_user_folder(user.username)
                        logger.info("The username=" +username)
                        return redirect('directory')
                    else:
                        return redirect('approval_pending')
    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        signup_form = SignUpForm()
        login_form = LoginForm()

    return render(request, 'A0_view_singUpIn.html', {'signup_form': signup_form, 'login_form': login_form})



def create_user_folder(username):
    user_folder = os.path.join(settings.MEDIA_ROOT, f"{username}")
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    download_folder = os.path.join(user_folder, 'download')
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    download_temp_folder = os.path.join(user_folder, 'download_temp')
    if not os.path.exists(download_temp_folder):
        os.makedirs(download_temp_folder)

    upload_folder = os.path.join(user_folder, 'uploads')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    download_dfgTool_folder = os.path.join(user_folder, 'download/dfgTool')
    if not os.path.exists(download_dfgTool_folder):
        os.makedirs(download_dfgTool_folder)


    upload_data_folder = os.path.join(user_folder, 'uploads/0_Data')
    if not os.path.exists(upload_data_folder):
        os.makedirs(upload_data_folder)

    ##################################################################


    confDirectory = "./myapp/Data/users"
    confPath = os.path.realpath(confDirectory)
    user_folder_backend = os.path.join(confPath, f"{username}")
    if not os.path.exists(user_folder_backend):
        os.makedirs(user_folder_backend)


    user_Conf_folder_backend = os.path.join(user_folder_backend, "0_Conf")
    if not os.path.exists(user_Conf_folder_backend):
        os.makedirs(user_Conf_folder_backend)

    user_DataConf_folder_backend = os.path.join(user_folder_backend, "0_DataConf")
    if not os.path.exists(user_DataConf_folder_backend):
        os.makedirs(user_DataConf_folder_backend)

    user_qRelationship_folder_backend = os.path.join(user_folder_backend, "0_qRelationship")
    if not os.path.exists(user_qRelationship_folder_backend):
        os.makedirs(user_qRelationship_folder_backend)


    user_utilExc_folder_backend = os.path.join(user_folder_backend, "0_utilsExecution")
    if not os.path.exists(user_utilExc_folder_backend):
        os.makedirs(user_utilExc_folder_backend)
        text_file_path = os.path.join(user_utilExc_folder_backend, "taskExecution.txt")
        with open(text_file_path, 'w') as file:
            pass  # No need to write anything, just creating the file





