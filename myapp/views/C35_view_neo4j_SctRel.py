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

def SctRelNeo4jFunc(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an SctRelNeo4jFunc view and C35_neo4j_SctRel.html")



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
    svgPath = downS + "/" + '07_OCT_REL'

    dataDirectory = f'./media/{username}/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)


    downloadDir = f"./media/{username}/download/dfgTool"
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '07_OCT_REL'




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




        return redirect(listData[8])

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        nextButton = NxButton()
        runButton = RunButton()

        savingTxt1 = outDir + "/" + "Q1.txt"
        savingTxt2 = outDir + "/" + "Q2_short.txt"
        savingTxt3 = outDir + "/" + "Q3.txt"


        savingSvg2 = svgPath + "/" + "Q2_svg_location.txt"
        savingSvg3 = svgPath + "/" + "Q3_svg_location.txt"



        with open(savingTxt1, 'r') as file:
            query1 = file.read()
            logger.info(f"\nquery1 : {query1}")

        with open(savingTxt2, 'r') as file:
            query2 = file.read()
            logger.info(f"\nquery2 : {query2}")

        with open(savingTxt3, 'r') as file:
            query3 = file.read()
            logger.info(f"\nquery3 : {query3}")

        ###############################################3


        with open(savingSvg2, 'r') as file:
            svg2 = file.read()
            logger.info(f"\nsvg2 : {svg2}")

        with open(savingSvg3, 'r') as file:
            svg3 = file.read()
            logger.info(f"\nsvg3 : {svg3}")






        return render(request, 'C35_neo4j_SctRel.html', {
            'nextButton': nextButton,
            'runButton': runButton,
            'softwareProtocol' : softwareProtocol,
            'query1': query1,
            'query2': query2,
            'query3': query3,

            'svg2': svg2,
            'svg3': svg3,



        }
                      )


