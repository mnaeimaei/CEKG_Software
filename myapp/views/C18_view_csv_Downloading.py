from django.shortcuts import render,redirect
from django.http import JsonResponse
from myapp.forms import NextButton1
from myapp.forms import DownButton
import subprocess
import pandas as pd
from django.http import HttpResponse
import json
import fcntl
import os
from io import BytesIO
import zipfile
from django.http import HttpResponse
from django.conf import settings

def downloadingCsv(request):
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("myapp")

    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an downloadingCSV view and C18_csv_Downloading.html")



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

    downloadTempDirectory = f'./media/{username}/download_temp'
    downloadTempPath = os.path.realpath(downloadTempDirectory)


    if request.method == 'POST':
        logger.info(f"################ request.method == 'POST' ################")


        # Redirect after the process
        return redirect('csvLinkingName')

    elif request.method == 'GET':
        logger.info(f"################ request.method == 'GET' ################")

        if 'download' in request.GET:
            logger.info("Preparing download...")
            subprocess.run(['python', 'A3_EntryCol_Step2_logConf_Step.py'], cwd=script_directory)
            subprocess.run(['python', 'A5_EntryCol_Step3_Step.py'], cwd=script_directory)
            subprocess.run(['python', 'A6_Scenario_Final_Step.py'], cwd=script_directory)
            subprocess.run(['python', 'A7_csv_generator_Step.py'], cwd=script_directory)
            subprocess.run(['python', 'A8_csv_save_Step.py'], cwd=script_directory)


            response = BytesIO()
            with zipfile.ZipFile(response, 'w') as zip_file:
                for filename in os.listdir(downloadTempDirectory):
                    if filename.endswith('.csv'):
                        file_path = os.path.join(downloadTempDirectory, filename)
                        zip_file.write(file_path, filename)
            response.seek(0)
            http_response = HttpResponse(response.getvalue(), content_type='application/zip')
            http_response['Content-Disposition'] = f'attachment; filename="{username}_files.zip"'
            return http_response
        else:
            logger.info("Handling regular GET request...")
            nextButton = NextButton1()
            downButton = DownButton ()
            return render(request, 'C18_csv_Downloading.html', {'nextButton': nextButton
                                                                ,'downButton': downButton
                                                                })


    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        logger.info("Handling unsupported method...")
        return HttpResponse("Method not supported", status=405)


