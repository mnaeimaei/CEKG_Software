from django.shortcuts import render,redirect
from django.http import JsonResponse
from myapp.models import UserProfile



from myapp.forms import MainDfgForm
from myapp.forms import Dfg1Form
from myapp.forms import Dfg2Form
from myapp.forms import Dfg3Form
from myapp.forms import Dfg4Form
from myapp.forms import Dfg5Form
from myapp.forms import Dfg6Form
from myapp.forms import InputForm
from myapp.forms import InputFormDFG6
from myapp.forms import ActivitySelectionForm
from myapp.forms import ActivityFormDFG6
from myapp.forms import NextButton1
import subprocess

import fcntl




from django.http import HttpResponse
import json
import logging


def home_view_old(request):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("myapp")
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an home_view view and A1_home_new.html")

    import os

    username = request.user.username
    logger.info("The username=" + username)
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

    if request.method == 'POST':
        logger.info(f"################ request.method == 'POST' ################")


        mainDfgForm = MainDfgForm(request.POST)
        dfg1Form = Dfg1Form(request.POST)
        dfg2Form = Dfg2Form(request.POST)
        dfg3Form = Dfg3Form(request.POST)
        dfg4Form = Dfg4Form(request.POST)
        dfg5Form = Dfg5Form(request.POST)
        dfg6Form = Dfg6Form(request.POST)
        inputform = InputForm(request.POST)
        inputFormDFG6 = InputFormDFG6(request.POST)
        activityForm = ActivitySelectionForm(request.POST)
        activityFormDFG6 = ActivityFormDFG6(request.POST)






        logger.debug(f"mainDfgForm.is_valid() = {mainDfgForm.is_valid()}")
        logger.debug(f"dfg1Form.is_valid() = {dfg1Form.is_valid()}")
        logger.debug(f"dfg2Form.is_valid() = {dfg2Form.is_valid()}")
        logger.debug(f"dfg3Form.is_valid() = {dfg3Form.is_valid()}")
        logger.debug(f"dfg4Form.is_valid() = {dfg4Form.is_valid()}")
        logger.debug(f"dfg5Form.is_valid() = {dfg5Form.is_valid()}")
        logger.debug(f"dfg6Form.is_valid() = {dfg6Form.is_valid()}")
        logger.debug(f"inputform.is_valid() = {inputform.is_valid()}")
        logger.debug(f"inputFormDFG6.is_valid() = {inputFormDFG6.is_valid()}")
        logger.debug(f"activityForm.is_valid() = {activityForm.is_valid()}")
        logger.debug(f"activityFormDFG6.is_valid() = {activityFormDFG6.is_valid()}")


        if mainDfgForm.is_valid():
            logger.debug(f"mainDfgForm.cleaned_data = {mainDfgForm.cleaned_data}")
            mainDfgForm_json = json.dumps(mainDfgForm.cleaned_data)
        if dfg1Form.is_valid():
            logger.debug(f"dfg1Form.cleaned_data = {dfg1Form.cleaned_data}")
            dfg1Form_json = json.dumps(dfg1Form.cleaned_data)
        if dfg2Form.is_valid():
            logger.debug(f"dfg2Form.cleaned_data = {dfg2Form.cleaned_data}")
            dfg2Form_json = json.dumps(dfg2Form.cleaned_data)
        if dfg3Form.is_valid():
            logger.debug(f"dfg3Form.cleaned_data = {dfg3Form.cleaned_data}")
            dfg3Form_json = json.dumps(dfg3Form.cleaned_data)
        if dfg4Form.is_valid():
            logger.debug(f"dfg4Form.cleaned_data = {dfg4Form.cleaned_data}")
            dfg4Form_json = json.dumps(dfg4Form.cleaned_data)
        if dfg5Form.is_valid():
            logger.debug(f"dfg5Form.cleaned_data = {dfg5Form.cleaned_data}")
            dfg5Form_json = json.dumps(dfg5Form.cleaned_data)
        if dfg6Form.is_valid():
            logger.debug(f"dfg6Form.cleaned_data = {dfg6Form.cleaned_data}")
            dfg6Form_json = json.dumps(dfg6Form.cleaned_data)
        if inputform.is_valid():
            logger.debug(f"inputform.cleaned_data = {inputform.cleaned_data}")
            inputform_json = json.dumps(inputform.cleaned_data)
        if inputFormDFG6.is_valid():
            logger.debug(f"inputFormDFG6.cleaned_data = {inputFormDFG6.cleaned_data}")
            inputFormDFG6_json = json.dumps(inputFormDFG6.cleaned_data)
        if activityForm.is_valid():
            logger.debug(f"activityForm.cleaned_data = {activityForm.cleaned_data}")
            activityForm_json = json.dumps(activityForm.cleaned_data)
        if activityFormDFG6.is_valid():
            logger.debug(f"activityFormDFG6.cleaned_data = {activityFormDFG6.cleaned_data}")
            activityFormDFG6_json = json.dumps(activityFormDFG6.cleaned_data)



        savingFile = confPath + "/" + "0_preSelection.txt"


        with open(savingFile, 'w') as file:
            file.write(mainDfgForm_json + '\n')
            file.write(dfg1Form_json + '\n')
            file.write(dfg2Form_json + '\n')
            file.write(dfg3Form_json + '\n')
            file.write(dfg4Form_json + '\n')
            file.write(dfg5Form_json + '\n')
            file.write(dfg6Form_json + '\n')
            file.write(inputform_json + '\n')
            file.write(inputFormDFG6_json + '\n')
            file.write(activityForm_json + '\n')
            file.write(activityFormDFG6_json + '\n')

        logger.debug(f"Subprocess Running")
        subprocess.run(['python', 'A0_softwareType.py'], cwd=script_directory)
        subprocess.run(['python', 'A00_configuration.py'], cwd=script_directory)
        subprocess.run(['python', 'A1_Scenario_Step1_Selecting.py'], cwd=script_directory)
        subprocess.run(['python', 'A1_Scenario_Step2.py'], cwd=script_directory)
        subprocess.run(['python', 'A1_Scenario_Step3.py'], cwd=script_directory)
        subprocess.run(['python', 'A2_FileLocation_Step1_Address_Step.py'], cwd=script_directory)

        return redirect('browseExcel')

    else:
        logger.info(f"################ request.method == 'ELSE' ################")



        mainDfgForm = MainDfgForm()
        dfg1Form = Dfg1Form()
        dfg2Form = Dfg2Form()
        dfg3Form = Dfg3Form()
        dfg4Form = Dfg4Form()
        dfg5Form = Dfg5Form()
        dfg6Form = Dfg6Form()
        inputform = InputForm()
        inputFormDFG6 = InputFormDFG6()
        activityForm = ActivitySelectionForm()
        activityFormDFG6 = ActivityFormDFG6()
        nextButton1 = NextButton1()







        #logger.debug(f"request.POST = {MainDfgForm(request.POST)}")
        #logger.debug(f"request.GET = {MainDfgForm(request.GET)}")
        return render(request, 'A1_home_old.html', {'mainDfgForm': mainDfgForm,
                                            'dfg1Form': dfg1Form,
                                            'dfg2Form': dfg2Form,
                                            'dfg3Form': dfg3Form,
                                            'dfg4Form': dfg4Form,
                                            'dfg5Form': dfg5Form,
                                            'dfg6Form': dfg6Form,
                                            'inputform': inputform,
                                            'inputFormDFG6': inputFormDFG6,
                                            'activityForm': activityForm,
                                            'activityFormDFG6': activityFormDFG6,
                                                    'nextButton1': nextButton1

                                                    }
                      )


