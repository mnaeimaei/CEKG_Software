from django.shortcuts import render,redirect

from myapp.forms import EventLogForm
from myapp.forms import OtherEntitiesForm
from myapp.forms import OtherEntitiesRelForm
from myapp.forms import ActivitiesValueForm
from myapp.forms import DomainSelectionForm
from myapp.forms import ICDForm
from myapp.forms import SnomedCtNodeForm
from myapp.forms import SnomedCtRelForm
from myapp.forms import DK1
from myapp.forms import DK2
from myapp.forms import DK3
from myapp.forms import DK4
from myapp.forms import DK5
from myapp.forms import DK61
from myapp.forms import DK62
from myapp.forms import DK7
from myapp.forms import NxButton
from myapp.forms import ApplyButton

import os
import ast
import json
import fcntl
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")


import pandas as pd
from django.http import JsonResponse




def preview_view(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an preview_view view and A3_preview.html")
    import os
    import ast
    username = request.user.username
    logger.info("The username=" + username)
    userDirectory = f"./myapp/Data/registration/0_username.txt"
    userPath = os.path.realpath(userDirectory)
    with open(userPath, 'w') as file:
        fcntl.flock(file, fcntl.LOCK_EX)
        file.write(username)
        fcntl.flock(file, fcntl.LOCK_UN)


    dataConfDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    dataConfPath = os.path.realpath(dataConfDirectory)



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
        logger.info("The username=" + username)
        eventLogform = EventLogForm(request.POST)
        otherEntitiesForm = OtherEntitiesForm(request.POST)
        otherEntitiesRelForm = OtherEntitiesRelForm(request.POST)
        activitiesValueForm = ActivitiesValueForm(request.POST)
        domainForm = DomainSelectionForm(request.POST)
        iCDForm = ICDForm(request.POST)
        snomedCtRelNode = SnomedCtNodeForm(request.POST)
        snomedCtRelForm = SnomedCtRelForm(request.POST)
        dk1 = DK1(request.POST)
        dk2 = DK2(request.POST)
        dk3 = DK3(request.POST)
        dk4 = DK4(request.POST)
        dk5 = DK5(request.POST)
        dk61 = DK61(request.POST)
        dk62 = DK62(request.POST)
        dk7 = DK7(request.POST)

        logger.debug(f"eventLogform.is_valid() = {eventLogform.is_valid()}")
        logger.debug(f"otherEntitiesForm.is_valid() = {otherEntitiesForm.is_valid()}")
        logger.debug(f"otherEntitiesRelForm.is_valid() = {otherEntitiesRelForm.is_valid()}")
        logger.debug(f"activitiesValueForm.is_valid() = {activitiesValueForm.is_valid()}")
        logger.debug(f"domainForm.is_valid() = {domainForm.is_valid()}")
        logger.debug(f"iCDForm.is_valid() = {iCDForm.is_valid()}")
        logger.debug(f"snomedCtRelNode.is_valid() = {snomedCtRelNode.is_valid()}")
        logger.debug(f"snomedCtRelForm.is_valid() = {snomedCtRelForm.is_valid()}")
        logger.debug(f"dk1.is_valid() = {dk1.is_valid()}")
        logger.debug(f"dk2.is_valid() = {dk2.is_valid()}")
        logger.debug(f"dk3.is_valid() = {dk3.is_valid()}")
        logger.debug(f"dk4.is_valid() = {dk4.is_valid()}")
        logger.debug(f"dk5.is_valid() = {dk5.is_valid()}")
        logger.debug(f"dk61.is_valid() = {dk61.is_valid()}")
        logger.debug(f"dk62.is_valid() = {dk62.is_valid()}")
        logger.debug(f"dk7.is_valid() = {dk7.is_valid()}")

        options_text_path = dataConfPath + "/3_previewOptionSheetNamesMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")



        savingPath = dataConfPath + "/3_previewDefault.txt"

        def update_variable_in_file(file_path, variable_to_update, new_value):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Update the specific line
            updated = False
            for i, line in enumerate(lines):
                if line.strip().startswith(variable_to_update):
                    lines[i] = f"{variable_to_update}={new_value}\n"
                    updated = True
                    break
            if updated:
                with open(file_path, 'w') as file:
                    file.writelines(lines)






        if eventLogform.is_valid():
            eventLogDiv = eventLogform.cleaned_data.get('dynamic_choice_EventLog')
            eventLogDiv = options_text_map[eventLogDiv]
            update_variable_in_file(savingPath, "eventLogDiv", eventLogDiv)

        if otherEntitiesForm.is_valid():
            otherEntitiesDiv = otherEntitiesForm.cleaned_data.get('dynamic_choice_OtherEntities')
            otherEntitiesDiv = options_text_map[otherEntitiesDiv]
            update_variable_in_file(savingPath, "otherEntitiesDiv", otherEntitiesDiv)


        if otherEntitiesRelForm.is_valid():
            otherEntitiesRelDiv = otherEntitiesRelForm.cleaned_data.get('dynamic_choice_OtherEntitiesRel')
            otherEntitiesRelDiv = options_text_map[otherEntitiesRelDiv]
            update_variable_in_file(savingPath, "otherEntitiesRelDiv", otherEntitiesRelDiv)


        if activitiesValueForm.is_valid():
            activitiesValueDiv = activitiesValueForm.cleaned_data.get('dynamic_choice_ActivitiesValue')
            activitiesValueDiv = options_text_map[activitiesValueDiv]
            update_variable_in_file(savingPath, "activitiesValueDiv", activitiesValueDiv)


        if domainForm.is_valid():
            domainDiv = domainForm.cleaned_data.get('dynamic_choice_Domain')
            domainDiv = options_text_map[domainDiv]
            update_variable_in_file(savingPath, "domainDiv", domainDiv)


        if iCDForm.is_valid():
            iCDDiv = iCDForm.cleaned_data.get('dynamic_choice_ICD')
            iCDDiv = options_text_map[iCDDiv]
            update_variable_in_file(savingPath, "iCDDiv", iCDDiv)


        if snomedCtRelNode.is_valid():
            snomedCtRelNodeDiv = snomedCtRelNode.cleaned_data.get('dynamic_choice_SnomedCt_Node')
            snomedCtRelNodeDiv = options_text_map[snomedCtRelNodeDiv]
            update_variable_in_file(savingPath, "snomedCtRelNodeDiv", snomedCtRelNodeDiv)


        if snomedCtRelForm.is_valid():
            snomedCtRelDiv = snomedCtRelForm.cleaned_data.get('dynamic_choice_SnomedCtRel')
            snomedCtRelDiv = options_text_map[snomedCtRelDiv]
            update_variable_in_file(savingPath, "snomedCtRelDiv", snomedCtRelDiv)


        if dk1.is_valid():
            dk1Div = dk1.cleaned_data.get('dynamic_choice_DK1')
            dk1Div = options_text_map[dk1Div]
            update_variable_in_file(savingPath, "dk1Div", dk1Div)


        if dk2.is_valid():
            dk2Div = dk2.cleaned_data.get('dynamic_choice_DK2')
            dk2Div = options_text_map[dk2Div]
            update_variable_in_file(savingPath, "dk2Div", dk2Div)


        if dk3.is_valid():
            dk3Div = dk3.cleaned_data.get('dynamic_choice_DK3')
            dk3Div = options_text_map[dk3Div]
            update_variable_in_file(savingPath, "dk3Div", dk3Div)


        if dk4.is_valid():
            dk4Div = dk4.cleaned_data.get('dynamic_choice_DK4')
            dk4Div = options_text_map[dk4Div]
            update_variable_in_file(savingPath, "dk4Div", dk4Div)


        if dk5.is_valid():
            dk5Div = dk5.cleaned_data.get('dynamic_choice_DK5')
            dk5Div = options_text_map[dk5Div]
            update_variable_in_file(savingPath, "dk5Div", dk5Div)


        if dk61.is_valid():
            dk61Div = dk61.cleaned_data.get('dynamic_choice_DK61')
            dk61Div = options_text_map[dk61Div]
            update_variable_in_file(savingPath, "dk61Div", dk61Div)


        if dk62.is_valid():
            dk62Div = dk62.cleaned_data.get('dynamic_choice_DK62')
            dk62Div = options_text_map[dk62Div]
            update_variable_in_file(savingPath, "dk62Div", dk62Div)


        if dk7.is_valid():
            dk7Div = dk7.cleaned_data.get('dynamic_choice_DK7')
            dk7Div = options_text_map[dk7Div]
            update_variable_in_file(savingPath, "dk7Div", dk7Div)






        openingPath = dataConfPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)


        return redirect(listData[0])

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        eventLogform = EventLogForm()
        otherEntitiesForm = OtherEntitiesForm()
        otherEntitiesRelForm = OtherEntitiesRelForm()
        activitiesValueForm = ActivitiesValueForm()
        domainForm = DomainSelectionForm()
        iCDForm = ICDForm()
        snomedCtRelNode = SnomedCtNodeForm()
        snomedCtRelForm = SnomedCtRelForm()
        dk1 = DK1()
        dk2 = DK2()
        dk3 = DK3()
        dk4 = DK4()
        dk5 = DK5()
        dk61 = DK61()
        dk62 = DK62()
        dk7 = DK7()
        nextButton = NxButton()
        applyButton = ApplyButton()




        openingPath = dataConfPath + "/3_previewNumberOfQuestions.txt"
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)
            options_to_show = json.dumps(listData)

        openingPath = dataConfPath + "/3_previewDefaultValue.txt"
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default = json.dumps(listData2)

        dataDirectory = f'./media/{username}/uploads/0_Data'
        dataPath = os.path.realpath(dataDirectory)
        excel_file = dataPath + '/EventLog_short.xlsx'
        logger.info(excel_file)
        xls = pd.ExcelFile(excel_file)
        sheets_data = {}
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            sheets_data[sheet_name] = df.to_dict(orient='records')



        return render(request, 'A3_preview.html', {
            'eventLogform': eventLogform,
            'otherEntitiesForm': otherEntitiesForm,
            'otherEntitiesRelForm': otherEntitiesRelForm,
            'activitiesValueForm': activitiesValueForm,
            'domainForm': domainForm,
            'iCDForm': iCDForm,
            'snomedCtRelNode': snomedCtRelNode,
            'snomedCtRelForm': snomedCtRelForm,
            'dk1': dk1,
            'dk2': dk2,
            'dk3': dk3,
            'dk4': dk4,
            'dk5': dk5,
            'dk61': dk61,
            'dk62': dk62,
            'dk7': dk7,
            'options_to_show': options_to_show,
            'options_to_show_default':options_to_show_default,
            'nextButton': nextButton,
            'applyButton': applyButton,
            'softwareProtocol' : softwareProtocol,
            'sheets_data': sheets_data,
                                            }
                  )



def get_excel_data(request):

    username = request.user.username
    logger.info("The username=" + username)
    userDirectory = f"./myapp/Data/registration/0_username.txt"
    userPath = os.path.realpath(userDirectory)
    with open(userPath, 'w') as file:
        fcntl.flock(file, fcntl.LOCK_EX)
        file.write(username)
        fcntl.flock(file, fcntl.LOCK_UN)




    dataDirectory = f'./media/{username}/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)
    excel_file = dataPath + '/EventLog_short.xlsx'
    logger.info(excel_file)
    xls = pd.ExcelFile(excel_file)

    try:
        xls = pd.ExcelFile(excel_file)
    except Exception as e:
        return JsonResponse({"error": str(e)})

    sheets_data = {}
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        if df.isnull().values.any():
            #logger.info(f'NaN found in sheet: {sheet_name}')
            nan_columns = df.columns[df.isnull().any()].tolist()
            #logger.info(f'Columns with NaN in {sheet_name}: {nan_columns}')
        sheets_data[sheet_name] = df.to_dict(orient='records')

    print(sheets_data)  # Check what is being outputted
    return JsonResponse(sheets_data)