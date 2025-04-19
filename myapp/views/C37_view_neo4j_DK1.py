from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.forms import NxButton
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

def DK1Neo4jFunc(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an DK1Neo4jFunc view and C37_neo4j_DK1.html")



    import os
    import ast
    username = request.user.username
    userDirectory = f"./myapp/Data/registration/0_username.txt"
    userPath = os.path.realpath(userDirectory)
    with open(userPath, 'w') as file:
        fcntl.flock(file, fcntl.LOCK_EX)
        file.write(username)
        fcntl.flock(file, fcntl.LOCK_UN)



    confDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    svgDirectory = "./myapp/Data/general/0_MultiMedia/graph_Location"
    downS = os.path.realpath(svgDirectory)
    svgPath = downS + "/" + '08_DK1'

    dataDirectory = f'./media/{username}/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)


    downloadDir = f"./media/{username}/download/dfgTool"
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '08_DK1'


    webSocketTypeDirectory = "./myapp/Data/general/0_GenConf/webSocketType.txt"
    webSocketTypeTxt = os.path.realpath(webSocketTypeDirectory)

    with open(webSocketTypeTxt, 'r') as file:
        for line in file:
            variable_name, value = line.split('=')
            variable_name = variable_name.strip()
            value = str(value.strip())
            if variable_name == 'webSocketType':
                softwareProtocol = value

    openingPath = confPath + "/3_pageSequencePart2.txt"
    with open(openingPath, 'r') as file:
        data = file.read()
        listData = ast.literal_eval(data)

    if request.method == 'POST':
        logger.info(f"################ request.method == 'POST' ################")


        return redirect(listData[9])

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        nextButton = NxButton()
        runButton = RunButton()



        return render(request, 'C37_neo4j_DK1.html', {
            'nextButton': nextButton,
            'runButton': runButton,
            'softwareProtocol' : softwareProtocol,

        }
                      )


