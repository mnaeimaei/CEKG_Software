from django.shortcuts import render,redirect
from django.http import JsonResponse

from myapp.forms import OerOrigin1Form
from myapp.forms import OerID1Form
from myapp.forms import OerOrigin2Form
from myapp.forms import OerID2Form

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

def entityRel(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an entityRel view and B6_csv_entiyRel.html")
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


        oer_origin1_form = OerOrigin1Form(request.POST)
        oer_id1_form = OerID1Form(request.POST)
        oer_origin2_form = OerOrigin2Form(request.POST)
        oer_id2_form = OerID2Form(request.POST)

        logger.debug(f"oer_origin1_form.is_valid() = {oer_origin1_form.is_valid()}")
        logger.debug(f"oer_id1_form.is_valid() = {oer_id1_form.is_valid()}")
        logger.debug(f"oer_origin2_form.is_valid() = {oer_origin2_form.is_valid()}")
        logger.debug(f"oer_id2_form.is_valid() = {oer_id2_form.is_valid()}")

        options_text_path = confPath + "/6_otherEntitiesMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/6_otherEntitiesRelDefault.txt"

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

        if oer_origin1_form.is_valid():
            EnP_Entity_Origin1 = oer_origin1_form.cleaned_data.get('dynamic_choice_B6_1')
            EnP_Entity_Origin1 = options_text_map[EnP_Entity_Origin1]
            update_variable_in_file(savingPath, "EnP_Entity_Origin1", EnP_Entity_Origin1)

        if oer_id1_form.is_valid():
            EnP_Entity_ID1 = oer_id1_form.cleaned_data.get('dynamic_choice_B6_2')
            EnP_Entity_ID1 = options_text_map[EnP_Entity_ID1]
            update_variable_in_file(savingPath, "EnP_Entity_ID1", EnP_Entity_ID1)

        if oer_origin2_form.is_valid():
            EnP_Entity_Origin2 = oer_origin2_form.cleaned_data.get('dynamic_choice_B6_3')
            EnP_Entity_Origin2 = options_text_map[EnP_Entity_Origin2]
            update_variable_in_file(savingPath, "EnP_Entity_Origin2", EnP_Entity_Origin2)

        if oer_id2_form.is_valid():
            EnP_Entity_ID2 = oer_id2_form.cleaned_data.get('dynamic_choice_B6_4')
            EnP_Entity_ID2 = options_text_map[EnP_Entity_ID2]
            update_variable_in_file(savingPath, "EnP_Entity_ID2", EnP_Entity_ID2)


        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[3])

    else:
        logger.info(f"################ request.method == 'ELSE' ################")



        oer_origin1_form = OerOrigin1Form()
        oer_id1_form = OerID1Form()
        oer_origin2_form = OerOrigin2Form()
        oer_id2_form = OerID2Form()

        nextButton = NextButton1()

        openingPath = confPath + "/6_otherEntitiesRelDefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b6 = json.dumps(listData2)

        openingPath2 = confPath + "/6_otherEntitiesRelNumber.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b6 = json.dumps(listData4)

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

        index_of_x = sheetTitleshelperList.index("EnP_PoNode_FileName_2")
        csvFileName = sheetTitles[index_of_x]  # C_Log
        logger.debug(f"csvFileName = {csvFileName}")
        #End of the CSV File Name


        csvPath = dataPath + "/" + csvFileName + ".csv"
        df_EntityRel = pd.read_csv(csvPath)
        logger.info(df_EntityRel)
        html_EntityRel = df_EntityRel.to_html(classes='dataframe', index=False)



        return render(request, 'B6_csv_entiyRel.html', {
            'html_EntityRel': html_EntityRel,
            'oer_origin1_form': oer_origin1_form,
            'oer_id1_form': oer_id1_form,
            'oer_origin2_form': oer_origin2_form,
            'oer_id2_form': oer_id2_form,
            'options_to_show_default_b6': options_to_show_default_b6,
            'button_lists_b6': button_lists_b6,
            'nextButton': nextButton

                                            }
                  )


