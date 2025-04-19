from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

import fcntl




import subprocess

from django.http import HttpResponse
import json
import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")


def browse_view(request):
    logger.info(
        f"********************************************************************************************************************************************************************************************")
    logger.info("This is an browse_view view and A02_browse.html")

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

    logger.info("The username=" + username)

    genConfDirectory = f"./myapp/Data/general/0_GenConf"
    genfPath = os.path.realpath(genConfDirectory)

    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    webSocketTypeDirectory = "./myapp/Data/general/0_GenConf/webSocketType.txt"
    webSocketTypeTxt = os.path.realpath(webSocketTypeDirectory)

    with open(webSocketTypeTxt, 'r') as file:
        for line in file:
            variable_name, value = line.split('=')
            variable_name = variable_name.strip()
            value = str(value.strip())
            if variable_name == 'webSocketType':
                softwareProtocol = value



    if request.method == 'POST':
        logger.info(f"################ request.method == 'POST' ################")



        neo4jTypeTxt = genfPath + "/neo4jType.txt"
        with open(neo4jTypeTxt, 'r') as file:
            for line in file:
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                value = int(value.strip())
                if variable_name == 'neo4jType':
                    neo4jType = value

            logger.info(f"neo4jType = {neo4jType}")

        if neo4jType == 0:

            subprocess.run(['python', 'A2_FileLocation_Step4_Aura_Step.py'], cwd=script_directory)

            return redirect('excelPreview')

        if neo4jType == 1:
            return redirect('auoraInfo')

    else:
        logger.info(f"################ request.method == 'ELSE' ################")



        return render(request, 'A02_browse.html', {

            'softwareProtocol': softwareProtocol,


        }
                      )
