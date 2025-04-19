from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import SctrS0
from myapp.forms import SctrS0_code
from myapp.forms import SctrS1
from myapp.forms import SctrS1_code

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
def SctRel(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an SctRel view and B11_csv_SctRel.html")
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

        sctr_s0 = SctrS0(request.POST)
        sctr_s0_code = SctrS0_code(request.POST)
        sctr_s1 = SctrS1(request.POST)
        sctr_s1_code = SctrS1_code(request.POST)

        logger.debug(f"sctr_s0.is_valid() = {sctr_s0.is_valid()}")
        logger.debug(f"sctr_s0_code.is_valid() = {sctr_s0_code.is_valid()}")
        logger.debug(f"sctr_s1.is_valid() = {sctr_s1.is_valid()}")
        logger.debug(f"sctr_s1_code.is_valid() = {sctr_s1_code.is_valid()}")


        options_text_path = confPath + "/11_octRelMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/11_octRelDefault.txt"

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

        if sctr_s0.is_valid():
            s0 = sctr_s0.cleaned_data.get('dynamic_choice_B11_1')
            s0 = options_text_map[s0]
            update_variable_in_file(savingPath, "OCT_OCT_REL_s0", s0)

        if sctr_s0_code.is_valid():
            s0_code = sctr_s0_code.cleaned_data.get('dynamic_choice_B11_2')
            s0_code = options_text_map[s0_code]
            update_variable_in_file(savingPath, "OCT_OCT_REL_s0_code", s0_code)

        if sctr_s1.is_valid():
            s1 = sctr_s1.cleaned_data.get('dynamic_choice_B11_3')
            s1 = options_text_map[s1]
            update_variable_in_file(savingPath, "OCT_OCT_REL_s1", s1)

        if sctr_s1_code.is_valid():
            s1_code = sctr_s1_code.cleaned_data.get('dynamic_choice_B11_4')
            s1_code = options_text_map[s1_code]
            update_variable_in_file(savingPath, "OCT_OCT_REL_s1_code", s1_code)


        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[8])

    else:
        logger.info(f"################ request.method == 'ELSE' ################")



        sctr_s0 = SctrS0()
        sctr_s0_code = SctrS0_code()
        sctr_s1 = SctrS1()
        sctr_s1_code = SctrS1_code()

        nextButton = NextButton1()

        openingPath = confPath + "/11_octRelDefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b11 = json.dumps(listData2)

        openingPath2 = confPath + "/11_octRelNumber.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b11 = json.dumps(listData4)

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

        index_of_x = sheetTitleshelperList.index("OCT_OCT_REL_FileName")
        csvFileName = sheetTitles[index_of_x]  # C_Log
        logger.debug(f"csvFileName = {csvFileName}")
        #End of the CSV File Name


        csvPath = dataPath + "/" + csvFileName + ".csv"
        df_OCT_REL = pd.read_csv(csvPath)
        logger.info(df_OCT_REL)
        html_OCT_REL = df_OCT_REL.to_html(classes='dataframe', index=False)



        return render(request, 'B11_csv_SctRel.html', {
            'html_OCT_REL': html_OCT_REL,
            'sctr_s0': sctr_s0,
            'sctr_s0_code': sctr_s0_code,
            'sctr_s1': sctr_s1,
            'sctr_s1_code': sctr_s1_code,
            'options_to_show_default_b11': options_to_show_default_b11,
            'button_lists_b11': button_lists_b11,
            'nextButton': nextButton
                                            }
                  )


