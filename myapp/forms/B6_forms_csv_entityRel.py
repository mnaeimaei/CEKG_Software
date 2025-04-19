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
class OerOrigin1Form(forms.Form):
    dynamic_choice_B6_1 = forms.ChoiceField(choices=[], label="The First Entity Origin or the First Entity's Attribute Origin")

    def __init__(self, *args,  **kwargs):
        super(OerOrigin1Form, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/6_otherEntitiesRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B6_1'].choices = choices


class OerID1Form(forms.Form):
    dynamic_choice_B6_2 = forms.ChoiceField(choices=[], label="The First Entity ID or the First Entity's Attribute ID")

    def __init__(self, *args,  **kwargs):
        super(OerID1Form, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/6_otherEntitiesRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B6_2'].choices = choices


class OerOrigin2Form(forms.Form):
    dynamic_choice_B6_3 = forms.ChoiceField(choices=[], label="The Second Entity Origin or the Second Entity's Attribute Origin")

    def __init__(self, *args,  **kwargs):
        super(OerOrigin2Form, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/6_otherEntitiesRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B6_3'].choices = choices


class OerID2Form(forms.Form):
    dynamic_choice_B6_4 = forms.ChoiceField(choices=[], label="The Second Entity ID or the Second Entity's Attribute ID")

    def __init__(self, *args,  **kwargs):
        super(OerID2Form, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/6_otherEntitiesRelOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B6_4'].choices = choices

