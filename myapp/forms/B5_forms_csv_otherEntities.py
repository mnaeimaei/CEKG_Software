from django import forms
from django.forms.widgets import Widget
from reportlab.pdfbase.pdfform import ButtonField
import json
import logging
import os
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")

userDirectory = f"./myapp/Data/registration/0_username.txt"
userPath = os.path.realpath(userDirectory)
with open(userPath, 'r') as file:
    for line in file:
        username = line
logger.info("The username=" + username)

class OenOriginForm(forms.Form):
    dynamic_choice_B5_1 = forms.ChoiceField(choices=[], label="Entities Attributes Origin")
    def __init__(self, *args,  **kwargs):
        super(OenOriginForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/5_otherEntitiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B5_1'].choices = choices

class OenIDForm(forms.Form):
    dynamic_choice_B5_2 = forms.ChoiceField(choices=[], label="Entities Attributes ID")
    def __init__(self, *args,  **kwargs):
        super(OenIDForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/5_otherEntitiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B5_2'].choices = choices


class OenNameForm(forms.Form):
    dynamic_choice_B5_3 = forms.ChoiceField(choices=[], label="Entities Attributes Name")
    def __init__(self, *args,  **kwargs):
        super(OenNameForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/5_otherEntitiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B5_3'].choices = choices


class OenValueForm(forms.Form):
    dynamic_choice_B5_4 = forms.ChoiceField(choices=[], label="Entities Attributes Value")
    def __init__(self, *args,  **kwargs):
        super(OenValueForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/5_otherEntitiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B5_4'].choices = choices


class OenCategoryForm(forms.Form):
    dynamic_choice_B5_5 = forms.ChoiceField(choices=[], label="Entities Attributes Category")
    def __init__(self, *args,  **kwargs):
        super(OenCategoryForm, self).__init__(*args, **kwargs)
        # Load the choices from a file

        import os
        confDirectory  = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)
        openingPath = confPath + "/5_otherEntitiesOption.txt"
        with open(openingPath, 'r') as file:
            import ast
            data = file.read()
            options_list = ast.literal_eval(data)
            # Create choices tuples (value, label) from the list
            choices = [(i, option) for i, option in enumerate(options_list, start=1)]
            self.fields['dynamic_choice_B5_5'].choices = choices

