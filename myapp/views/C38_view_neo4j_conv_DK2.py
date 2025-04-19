from django.shortcuts import render,redirect
from django.http import JsonResponse
from myapp.forms import NxButton
from myapp.forms import RsButton

from myapp.forms import RunButton
import subprocess
import pandas as pd
from django.http import HttpResponse
import json
import logging


import fcntl
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")

def conv_DK2(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an convertingNeo4jFunc view and C20_neo4j_Conv_EventLog.html")



    import os
    import ast
    username = request.user.username
    userDirectory = f"./myapp/Data/registration/0_username.txt"
    userPath = os.path.realpath(userDirectory)
    with open(userPath, 'w') as file:
        fcntl.flock(file, fcntl.LOCK_EX)
        file.write(username)
        fcntl.flock(file, fcntl.LOCK_UN)

    multiDirectory = "./myapp/Data/general/0_MultiMedia"
    multiD = os.path.realpath(multiDirectory)

    confDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    dataDirectory = f'./media/{username}/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

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

        return redirect('DK2Neo4jName')


    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        nextButton = RsButton()
        runButton = RunButton()

        return render(request, 'C38_neo4j_Conv_DK2.html', {
            'nextButton': nextButton,
            'runButton': runButton,
            'softwareProtocol' : softwareProtocol,

                                            }
                      )