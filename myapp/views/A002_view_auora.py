from django.shortcuts import render, redirect


from myapp.forms import UserNameNeo
from myapp.forms import PassWordNeo
from myapp.forms import UriNeo
from myapp.forms import NextButton1





import subprocess

from django.http import HttpResponse
import json
import logging
import fcntl

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")


def auora_view(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an auora_view view and A002_auora.html")
    import os
    import ast
    import os
    username = request.user.username
    userDirectory = f"./myapp/Data/registration/0_username.txt"
    userPath = os.path.realpath(userDirectory)
    with open(userPath, 'w') as file:
        fcntl.flock(file, fcntl.LOCK_EX)
        file.write(username)
        fcntl.flock(file, fcntl.LOCK_UN)

    dataConfDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    confPath = os.path.realpath(dataConfDirectory)


    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)



    if request.method == 'POST' :
        logger.info(f"################ request.method == 'POST' ################")

        logger.info("The username=" + username)
        userNameNeo = UserNameNeo(request.POST)
        passWordNeo = PassWordNeo(request.POST)
        uriNeo = UriNeo(request.POST)

        logger.info(f"userNameNeo.is_valid() = {userNameNeo.is_valid()}")
        logger.info(f"passWordNeo.is_valid() = {passWordNeo.is_valid()}")
        logger.info(f"uriNeo.is_valid() = {uriNeo.is_valid()}")

        if userNameNeo.is_valid():
            logger.info(f"userNameNeo.cleaned_data = {userNameNeo.cleaned_data}")
            userNameNeo_json = json.dumps(userNameNeo.cleaned_data)
            finalUserName = userNameNeo.cleaned_data.get('userNameNeoMode')
            logger.info(f"finalUserName = {finalUserName}")


        if passWordNeo.is_valid():
            logger.info(f"passWordNeo.cleaned_data = {passWordNeo.cleaned_data}")
            passWordNeo_json = json.dumps(passWordNeo.cleaned_data)
            finalPassWord = passWordNeo.cleaned_data.get('passWordNeoMode')
            logger.info(f"finalPassWord = {finalPassWord}")

        if uriNeo.is_valid():
            logger.info(f"uriNeo.cleaned_data = {uriNeo.cleaned_data}")
            uriNeo_json = json.dumps(uriNeo.cleaned_data)
            finalUri = uriNeo.cleaned_data.get('uriNeoMode')
            logger.info(f"finalUri = {finalUri}")

        savingFile4 = confPath + "/" + "2_downloadingLocal1.txt"
        with open(savingFile4, 'w') as file:
            file.write(f'''finalUsrWord={finalUserName}''' + "\n")

        savingFile5 = confPath + "/" + "2_downloadingLocal2.txt"
        with open(savingFile5, 'w') as file:
            file.write(f'''finalPassWord={finalPassWord}''' + "\n")

        savingFile6 = confPath + "/" + "2_downloadingLocal3.txt"
        with open(savingFile6, 'w') as file:
            file.write(f'''finalUri={finalUri}''' + "\n")


        subprocess.run(['python', 'A2_FileLocation_Step4_Aura_Step.py'], cwd=script_directory)

        return redirect('excelPreview')

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        userNameNeo = UserNameNeo()
        passWordNeo = PassWordNeo()
        uriNeo = UriNeo()
        nextButton=NextButton1()

        inputTex_FilePath1 = confPath + "/2_downloadingLocal1.txt"
        inputTex_FilePath2 = confPath + "/2_downloadingLocal2.txt"
        inputTex_FilePath3 = confPath + "/2_downloadingLocal3.txt"


        defaultUser, defaultPass , defaultUri= existanceFileName(inputTex_FilePath1,inputTex_FilePath2,inputTex_FilePath3)
        logger.info(defaultUser)
        logger.info(defaultPass)
        logger.info(defaultUri)

        return render(request, 'A002_auora.html', {
            'uriNeo': uriNeo,
            'userNameNeo': userNameNeo,
            'passWordNeo': passWordNeo,

            'defaultUri': defaultUri,
            'defaultUser': defaultUser,
            'defaultPass': defaultPass,

            'nextButton': nextButton,


        }
                      )


def existanceFileName(inputTex_FilePath1,inputTex_FilePath2,inputTex_FilePath3):
    value3 = ""
    value4 = ""
    value5 = ""

    import os

    if os.path.exists(inputTex_FilePath1):
        with open(inputTex_FilePath1, 'r') as file:
            for line in file:
                variable_name, value3 = line.split('=')
                value3 = value3.strip()
    else:
        with open(inputTex_FilePath1, 'w') as file:
            file.write('')  # Creating an empty file


    if os.path.exists(inputTex_FilePath2):
        with open(inputTex_FilePath2, 'r') as file:
            for line in file:
                variable_name, value4 = line.split('=')
                value4 = value4.strip()
    else:
        with open(inputTex_FilePath2, 'w') as file:
            file.write('')  # Creating an empty file


    if os.path.exists(inputTex_FilePath3):
        with open(inputTex_FilePath3, 'r') as file:
            for line in file:
                variable_name, value5 = line.split('=')
                value5 = value5.strip()

    else:
        with open(inputTex_FilePath3, 'w') as file:
            file.write('')  # Creating an empty file
    return value3, value4, value5