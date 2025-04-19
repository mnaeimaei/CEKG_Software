from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import Dk3DisordersForm
from myapp.forms import Dk3IcdCodeForm


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

def DK3(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an DK3 view and B14_csv_DK3.html")
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

        dk3_disorders_form = Dk3DisordersForm(request.POST)
        dk3_icd_code_form = Dk3IcdCodeForm(request.POST)

        logger.debug(f"dk3_disorders_form.is_valid() = {dk3_disorders_form.is_valid()}")
        logger.debug(f"dk3_icd_code_form.is_valid() = {dk3_icd_code_form.is_valid()}")

        options_text_path = confPath + "/14_dk3Mapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/14_dk3Default.txt"

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

        if dk3_disorders_form.is_valid():
            DK3_Disorders = dk3_disorders_form.cleaned_data.get('dynamic_choice_B14_1')
            DK3_Disorders = options_text_map[DK3_Disorders]
            update_variable_in_file(savingPath, "DK3_Disorders", DK3_Disorders)

        if dk3_icd_code_form.is_valid():
            DK3_icd_code = dk3_icd_code_form.cleaned_data.get('dynamic_choice_B14_2')
            DK3_icd_code = options_text_map[DK3_icd_code]
            update_variable_in_file(savingPath, "DK3_icd_code", DK3_icd_code)

        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[11])

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        dk3_disorders_form = Dk3DisordersForm()
        dk3_icd_code_form = Dk3IcdCodeForm()

        nextButton = NextButton1()

        openingPath = confPath + "/14_dk3DefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b14 = json.dumps(listData2)

        openingPath2 = confPath + "/14_dk3Number.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b14 = json.dumps(listData4)

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

        index_of_x = sheetTitleshelperList.index("DK3_Potential_DK3_FileName")
        csvFileName = sheetTitles[index_of_x]  # C_Log
        logger.debug(f"csvFileName = {csvFileName}")
        #End of the CSV File Name


        csvPath = dataPath + "/" + csvFileName + ".csv"
        df_DK3 = pd.read_csv(csvPath)
        logger.info(df_DK3)
        html_DK3 = df_DK3.to_html(classes='dataframe', index=False)



        return render(request, 'B14_csv_DK3.html', {
            'html_DK3': html_DK3,
            'dk3_disorders_form': dk3_disorders_form,
            'dk3_icd_code_form': dk3_icd_code_form,
            'options_to_show_default_b14': options_to_show_default_b14,
            'button_lists_b14': button_lists_b14,
            'nextButton': nextButton

                                            }
                  )


