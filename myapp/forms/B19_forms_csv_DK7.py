from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")
import os

userDirectory = f"./myapp/Data/registration/0_username.txt"
userPath = os.path.realpath(userDirectory)
with open(userPath, 'r') as file:
    for line in file:
        username = line

logger.info("The username=" + username)
class Dk7ActivityValueIdForm(forms.Form):
    dynamic_choice_B19_1 = forms.ChoiceField(choices=[], label="Activity Instance ID")

    def __init__(self, *args,  **kwargs):
        super(Dk7ActivityValueIdForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/19_dk7Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B19_1'].choices = choices


class Dk7DisordersForm(forms.Form):
    dynamic_choice_B19_2 = forms.ChoiceField(choices=[], label="Disorder Entity ID")

    def __init__(self, *args,  **kwargs):
        super(Dk7DisordersForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/19_dk7Option.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B19_2'].choices = choices

