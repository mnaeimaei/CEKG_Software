from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import Dk4IcdCodeForm
from myapp.forms import Dk4OtcForm

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

def DK4(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an DK4 view and B15_csv_DK4.html")
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

        dk4_icd_code_form = Dk4IcdCodeForm(request.POST)
        dk4_otc_form = Dk4OtcForm(request.POST)


        logger.debug(f"dk4_icd_code_form.is_valid() = {dk4_icd_code_form.is_valid()}")
        logger.debug(f"dk4_otc_form.is_valid() = {dk4_otc_form.is_valid()}")


        options_text_path = confPath + "/15_dk4Mapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/15_dk4Default.txt"

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

        if dk4_icd_code_form.is_valid():
            DK4_icd_code = dk4_icd_code_form.cleaned_data.get('dynamic_choice_B15_1')
            DK4_icd_code = options_text_map[DK4_icd_code]
            update_variable_in_file(savingPath, "DK4_icd_code", DK4_icd_code)

        if dk4_otc_form.is_valid():
            DK4_OTC = dk4_otc_form.cleaned_data.get('dynamic_choice_B15_2')
            DK4_OTC = options_text_map[DK4_OTC]
            update_variable_in_file(savingPath, "DK4_OTC", DK4_OTC)


        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[12])

    else:
        logger.info(f"################ request.method == 'ELSE' ################")


        dk4_icd_code_form = Dk4IcdCodeForm()
        dk4_otc_form = Dk4OtcForm()

        nextButton = NextButton1()

        openingPath = confPath + "/15_dk4DefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b15 = json.dumps(listData2)

        openingPath2 = confPath + "/15_dk4Number.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b15 = json.dumps(listData4)

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

        index_of_x = sheetTitleshelperList.index("DK4_ICD_OCT_FileName")
        csvFileName = sheetTitles[index_of_x]  # C_Log
        logger.debug(f"csvFileName = {csvFileName}")
        #End of the CSV File Name


        csvPath = dataPath + "/" + csvFileName + ".csv"
        df_DK4 = pd.read_csv(csvPath)
        logger.info(df_DK4)
        html_DK4 = df_DK4.to_html(classes='dataframe', index=False)



        return render(request, 'B15_csv_DK4.html', {
            'html_DK4': html_DK4,
            'dk4_icd_code_form': dk4_icd_code_form,
            'dk4_otc_form': dk4_otc_form,
            'options_to_show_default_b15': options_to_show_default_b15,
            'button_lists_b15': button_lists_b15,
            'nextButton': nextButton

                                            }
                  )


