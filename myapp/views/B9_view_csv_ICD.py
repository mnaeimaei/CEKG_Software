from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import IdcClinicalEntityForm
from myapp.forms import IdcCodeForm
from myapp.forms import IdcVersionForm
from myapp.forms import IdcCodeTitleForm

from myapp.forms import NextButton1

import subprocess
import os
import pandas as pd
import ast
import fcntl



from django.http import HttpResponse
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")

def ICD(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an ICD view and B9_csv_ICD.html")
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

    dataDirectory = f'./media/{username}/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    if request.method == 'POST':
        logger.info(f"################ request.method == 'POST' ################")


        idc_clinical_entity_form = IdcClinicalEntityForm(request.POST)
        idc_code_form = IdcCodeForm(request.POST)
        idc_version_form = IdcVersionForm(request.POST)
        idc_code_title_form = IdcCodeTitleForm(request.POST)

        logger.info(f"idc_clinical_entity_form.is_valid() = {idc_clinical_entity_form.is_valid()}")
        logger.info(f"idc_code_form.is_valid() = {idc_code_form.is_valid()}")
        logger.info(f"idc_version_form.is_valid() = {idc_version_form.is_valid()}")
        logger.info(f"idc_code_title_form.is_valid() = {idc_code_title_form.is_valid()}")

        options_text_path = confPath + "/9_icdOptionMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.info(f"options_text_map = {options_text_map}")


        savingPath = confPath + "/9_icdDefault.txt"


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
            logger.info(f"updated = {updated}")
            if updated:
                with open(file_path, 'w') as file:
                    file.writelines(lines)

        if idc_clinical_entity_form.is_valid():
            ClinicalEntity = idc_clinical_entity_form.cleaned_data.get('dynamic_choice_B9_1')
            ClinicalEntity = options_text_map[ClinicalEntity]
            update_variable_in_file(savingPath, "CE_ClinicalEntity", ClinicalEntity)

        if idc_code_form.is_valid():
            icd_code = idc_code_form.cleaned_data.get('dynamic_choice_B9_2')
            icd_code = options_text_map[icd_code]
            update_variable_in_file(savingPath, "CE_icd_code", icd_code)

        if idc_version_form.is_valid():
            icd_version = idc_version_form.cleaned_data.get('dynamic_choice_B9_3')
            icd_version = options_text_map[icd_version]
            update_variable_in_file(savingPath, "CE_icd_version", icd_version)

        if idc_code_title_form.is_valid():
            icd_code_title = idc_code_title_form.cleaned_data.get('dynamic_choice_B9_4')
            icd_code_title = options_text_map[icd_code_title]
            update_variable_in_file(savingPath, "CE_icd_code_title", icd_code_title)

        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)


        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[6])

    else:
        logger.info(f"################ request.method == 'ELSE' ################")


        idc_clinical_entity_form = IdcClinicalEntityForm()
        idc_code_form = IdcCodeForm()
        idc_version_form = IdcVersionForm()
        idc_code_title_form = IdcCodeTitleForm()

        nextButton = NextButton1()

        openingPath = confPath + "/9_icdDefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b9 = json.dumps(listData2)

        openingPath2 = confPath + "/9_icdNumber.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b9 = json.dumps(listData4)

        #Start of Finding the CSV File Name
        sheetTitleshelperPath = confPath + "/2_sheetTitleshelper.txt"
        with open(sheetTitleshelperPath, 'r') as file:
            default3 = file.read()
            sheetTitleshelperList = ast.literal_eval(default3)
        sheetTitlesPath = confPath + "/3_previewXConf.txt"
        sheetTitles = []
        with open(sheetTitlesPath, 'r') as file:
            for line in file:
                variable_name3, value3 = line.split('=')
                value3 = value3.strip()
                sheetTitles = ast.literal_eval(value3)

        index_of_x = sheetTitleshelperList.index("CE_PoNode_FileName")
        csvFileName = sheetTitles[index_of_x]  # C_Log
        logger.debug(f"csvFileName = {csvFileName}")
        #End of the CSV File Name


        csvPath = dataPath + "/" + csvFileName + ".csv"
        df_ICD = pd.read_csv(csvPath)
        logger.info(df_ICD)
        html_ICD = df_ICD.to_html(classes='dataframe', index=False)



        return render(request, 'B9_csv_ICD.html', {
            'html_ICD': html_ICD,
            'idc_clinical_entity_form': idc_clinical_entity_form,
            'idc_code_form': idc_code_form,
            'idc_version_form': idc_version_form,
            'idc_code_title_form': idc_code_title_form,
            'options_to_show_default_b9': options_to_show_default_b9,
            'button_lists_b9': button_lists_b9,
            'nextButton': nextButton

                                            }
                  )


