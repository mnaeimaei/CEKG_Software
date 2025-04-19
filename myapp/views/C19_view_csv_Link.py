from django.shortcuts import render, redirect


from myapp.forms import LogLink
from myapp.forms import EntityRelLink
from myapp.forms import OtherEntitiesLink
from myapp.forms import ActivityPropertiesLink
from myapp.forms import DomainLink
from myapp.forms import IcdLink
from myapp.forms import OctNodeLink
from myapp.forms import OctRelLink
from myapp.forms import Dk3Link
from myapp.forms import Dk4Link
from myapp.forms import Dk5Link
from myapp.forms import Dk61Link
from myapp.forms import Dk62Link
from myapp.forms import Dk7Link
from myapp.forms import NextButton1



import subprocess

from django.http import HttpResponse
import json
import logging
import fcntl

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")


def csvLinking(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an auora_view view and A002_auora.html")
    import os
    import ast
    import os
    username = request.user.username
    userDirectory = f"./myapp/Data/registration/0_username.txt"
    userPath = os.path.realpath(userDirectory)
    with open(userPath, 'w') as file:
        fcntl.flock(file, fcntl.LOCK_EX)
        file.write(username)
        fcntl.flock(file, fcntl.LOCK_UN)

    dataConfDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    confPath = os.path.realpath(dataConfDirectory)


    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)
    if request.method == 'POST' :

        logger.info(f"################ request.method == 'POST' ################")


        logLink = LogLink(request.POST)
        entityRelLink = EntityRelLink(request.POST)
        otherEntitiesLink = OtherEntitiesLink(request.POST)
        activityPropertiesLink = ActivityPropertiesLink(request.POST)
        domainLink = DomainLink(request.POST)
        icdLink = IcdLink(request.POST)
        octNodeLink = OctNodeLink(request.POST)
        octRelLink = OctRelLink(request.POST)
        dk3Link = Dk3Link(request.POST)
        dk4Link = Dk4Link(request.POST)
        dk5Link = Dk5Link(request.POST)
        d61Link = Dk61Link(request.POST)
        dk62Link = Dk62Link(request.POST)
        dk7Link = Dk7Link(request.POST)

        logger.info(f"logLink.is_valid() = {logLink.is_valid()}")
        logger.info(f"entityRelLink.is_valid() = {entityRelLink.is_valid()}")
        logger.info(f"otherEntitiesLink.is_valid() = {otherEntitiesLink.is_valid()}")
        logger.info(f"activityPropertiesLink.is_valid() = {activityPropertiesLink.is_valid()}")
        logger.info(f"domainLink.is_valid() = {domainLink.is_valid()}")
        logger.info(f"icdLink.is_valid() = {icdLink.is_valid()}")
        logger.info(f"octNodeLink.is_valid() = {octNodeLink.is_valid()}")
        logger.info(f"octRelLink.is_valid() = {octRelLink.is_valid()}")
        logger.info(f"dk3Link.is_valid() = {dk3Link.is_valid()}")
        logger.info(f"dk4Link.is_valid() = {dk4Link.is_valid()}")
        logger.info(f"dk5Link.is_valid() = {dk5Link.is_valid()}")
        logger.info(f"d61Link.is_valid() = {d61Link.is_valid()}")
        logger.info(f"dk62Link.is_valid() = {dk62Link.is_valid()}")
        logger.info(f"dk7Link.is_valid() = {dk7Link.is_valid()}")


        if logLink.is_valid():
            logger.info(f"logLink.cleaned_data = {logLink.cleaned_data}")
            logLink_json = json.dumps(logLink.cleaned_data)
            finallogLink = logLink.cleaned_data.get('logLinkMode')
            logger.info(f"finallogLink = {finallogLink}")

        if entityRelLink.is_valid():
            logger.info(f"entityRelLink.cleaned_data = {entityRelLink.cleaned_data}")
            entityRelLink_json = json.dumps(entityRelLink.cleaned_data)
            finalentityRelLink = entityRelLink.cleaned_data.get('entityRelLinkMode')
            logger.info(f"finalentityRelLink = {finalentityRelLink}")

        if otherEntitiesLink.is_valid():
            logger.info(f"otherEntitiesLink.cleaned_data = {otherEntitiesLink.cleaned_data}")
            therEntitiesLink_json = json.dumps(otherEntitiesLink.cleaned_data)
            finalotherEntitiesLink = otherEntitiesLink.cleaned_data.get('otherEntitiesLinkMode')
            logger.info(f"finalotherEntitiesLink = {finalotherEntitiesLink}")

        if activityPropertiesLink.is_valid():
            logger.info(f"activityPropertiesLink.cleaned_data = {activityPropertiesLink.cleaned_data}")
            activityPropertiesLink_json = json.dumps(activityPropertiesLink.cleaned_data)
            finalactivityPropertiesLink = activityPropertiesLink.cleaned_data.get('activityPropertiesLinkMode')
            logger.info(f"finalactivityPropertiesLink = {finalactivityPropertiesLink}")

        if domainLink.is_valid():
            logger.info(f"domainLink.cleaned_data = {domainLink.cleaned_data}")
            domainLink_json = json.dumps(domainLink.cleaned_data)
            finaldomainLink = domainLink.cleaned_data.get('domainLinkMode')
            logger.info(f"finaldomainLink = {finaldomainLink}")

        if icdLink.is_valid():
            logger.info(f"icdLink.cleaned_data = {icdLink.cleaned_data}")
            icdLink_json = json.dumps(icdLink.cleaned_data)
            finalicdLink = icdLink.cleaned_data.get('icdLinkMode')
            logger.info(f"finalicdLink = {finalicdLink}")

        if octNodeLink.is_valid():
            logger.info(f"octNodeLink.cleaned_data = {octNodeLink.cleaned_data}")
            octNodeLink_json = json.dumps(octNodeLink.cleaned_data)
            finaloctNodeLink = octNodeLink.cleaned_data.get('octNodeLinkMode')
            logger.info(f"finaloctNodeLink = {finaloctNodeLink}")

        if octRelLink.is_valid():
            logger.info(f"octRelLink.cleaned_data = {octRelLink.cleaned_data}")
            octRelLink_json = json.dumps(octRelLink.cleaned_data)
            finaloctRelLink = octRelLink.cleaned_data.get('octRelLinkMode')
            logger.info(f"finaloctRelLink = {finaloctRelLink}")

        if dk3Link.is_valid():
            logger.info(f"dk3Link.cleaned_data = {dk3Link.cleaned_data}")
            dk3Link_json = json.dumps(dk3Link.cleaned_data)
            finaldk3Link = dk3Link.cleaned_data.get('dk3LinkMode')
            logger.info(f"finaldk3Link = {finaldk3Link}")

        if dk4Link.is_valid():
            logger.info(f"dk4Link.cleaned_data = {dk4Link.cleaned_data}")
            dk4Link_json = json.dumps(dk4Link.cleaned_data)
            finaldk4Link = dk4Link.cleaned_data.get('dk4LinkMode')
            logger.info(f"finaldk4Link = {finaldk4Link}")

        if dk5Link.is_valid():
            logger.info(f"dk5Link.cleaned_data = {dk5Link.cleaned_data}")
            dk5Link_json = json.dumps(dk5Link.cleaned_data)
            finaldk5Link = dk5Link.cleaned_data.get('dk5LinkMode')
            logger.info(f"finaldk5Link = {finaldk5Link}")

        if d61Link.is_valid():
            logger.info(f"d61Link.cleaned_data = {d61Link.cleaned_data}")
            d61Link_json = json.dumps(d61Link.cleaned_data)
            finald61Link = d61Link.cleaned_data.get('dk61LinkMode')
            logger.info(f"finald61Link = {finald61Link}")

        if dk62Link.is_valid():
            logger.info(f"dk62Link.cleaned_data = {dk62Link.cleaned_data}")
            dk62Link_json = json.dumps(dk62Link.cleaned_data)
            finaldk62Link = dk62Link.cleaned_data.get('dk62LinkMode')
            logger.info(f"finaldk62Link = {finaldk62Link}")

        if dk7Link.is_valid():
            logger.info(f"dk7Link.cleaned_data = {dk7Link.cleaned_data}")
            dk7Link_json = json.dumps(dk7Link.cleaned_data)
            finaldk7Link = dk7Link.cleaned_data.get('dk7LinkMode')
            logger.info(f"finaldk7Link = {finaldk7Link}")





        savingFile = confPath + "/" + "2_cloudLink1.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''LogLink={finallogLink}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink2.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''EntityRelLink={finalentityRelLink}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink3.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''OtherEntitiesLink={finalotherEntitiesLink}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink4.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''ActivityPropertiesLink={finalactivityPropertiesLink}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink5.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''DomainLink={finaldomainLink}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink6.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''IcdLink={finalicdLink}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink7.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''OctNodeLink={finaloctNodeLink}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink8.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''OctRelLink={finaloctRelLink}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink9.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''Dk3Link={finaldk3Link}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink10.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''Dk4Link={finaldk4Link}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink11.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''Dk5Link={finaldk5Link}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink12.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''Dk61Link={finald61Link}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink13.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''Dk62Link={finaldk62Link}''' + "\n")

        savingFile = confPath + "/" + "2_cloudLink14.txt"
        with open(savingFile, 'w') as file:
            file.write(f'''Dk7Link={finaldk7Link}''' + "\n")








        subprocess.run(['python', 'A9_csv_link_Step.py'], cwd=script_directory)


        return redirect('convertingNeo4jName')

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        logLink = LogLink()
        entityRelLink = EntityRelLink()
        otherEntitiesLink = OtherEntitiesLink()
        activityPropertiesLink = ActivityPropertiesLink()
        domainLink = DomainLink()
        icdLink = IcdLink()
        octNodeLink = OctNodeLink()
        octRelLink = OctRelLink()
        dk3Link = Dk3Link()
        dk4Link = Dk4Link()
        dk5Link = Dk5Link()
        d61Link = Dk61Link()
        dk62Link = Dk62Link()
        dk7Link = Dk7Link()






        nextButton=NextButton1()

        inputTex_FilePath1 = confPath + "/2_cloudLink1.txt"
        inputTex_FilePath2 = confPath + "/2_cloudLink2.txt"
        inputTex_FilePath3 = confPath + "/2_cloudLink3.txt"
        inputTex_FilePath4 = confPath + "/2_cloudLink4.txt"
        inputTex_FilePath5 = confPath + "/2_cloudLink5.txt"
        inputTex_FilePath6 = confPath + "/2_cloudLink6.txt"
        inputTex_FilePath7 = confPath + "/2_cloudLink7.txt"
        inputTex_FilePath8 = confPath + "/2_cloudLink8.txt"
        inputTex_FilePath9 = confPath + "/2_cloudLink9.txt"
        inputTex_FilePath10 = confPath + "/2_cloudLink10.txt"
        inputTex_FilePath11 = confPath + "/2_cloudLink11.txt"
        inputTex_FilePath12 = confPath + "/2_cloudLink12.txt"
        inputTex_FilePath13 = confPath + "/2_cloudLink13.txt"
        inputTex_FilePath14 = confPath + "/2_cloudLink14.txt"

        defaultLog, defaultEntityRel, defaultOtherEntities, defaultActivityProperties, defaultDomain, defaultIcd, defaultOctNode, defaultOctRel, defaultDk3, defaultDk4, defaultDk5, defaultDk61, defaultDk62, defaultDk7= existanceFileName(inputTex_FilePath1,inputTex_FilePath2,inputTex_FilePath3,
inputTex_FilePath4,inputTex_FilePath5,inputTex_FilePath6,
inputTex_FilePath7,inputTex_FilePath8,inputTex_FilePath9,
inputTex_FilePath10,inputTex_FilePath11,inputTex_FilePath12,
inputTex_FilePath13,inputTex_FilePath14)
        logger.info(defaultLog)
        logger.info(defaultEntityRel)
        logger.info(defaultOtherEntities)
        logger.info(defaultActivityProperties)
        logger.info(defaultDomain)
        logger.info(defaultIcd)
        logger.info(defaultOctNode)
        logger.info(defaultOctRel)
        logger.info(defaultDk3)
        logger.info(defaultDk4)
        logger.info(defaultDk5)
        logger.info(defaultDk61)
        logger.info(defaultDk62)
        logger.info(defaultDk7)

        return render(request, 'C19_csv_Link.html', {
            'logLink': logLink,
            'entityRelLink': entityRelLink,
            'otherEntitiesLink': otherEntitiesLink,
            'activityPropertiesLink': activityPropertiesLink,
            'domainLink': domainLink,
            'icdLink': icdLink,
            'octNodeLink': octNodeLink,
            'octRelLink': octRelLink,
            'dk3Link': dk3Link,
            'dk4Link': dk4Link,
            'dk5Link': dk5Link,
            'd61Link': d61Link,
            'dk62Link': dk62Link,
            'dk7Link': dk7Link,



            'defaultLog': defaultLog,
            'defaultEntityRel': defaultEntityRel,
            'defaultOtherEntities': defaultOtherEntities,
            'defaultActivityProperties': defaultActivityProperties,
            'defaultDomain': defaultDomain,
            'defaultIcd': defaultIcd,
            'defaultOctNode': defaultOctNode,
            'defaultOctRel': defaultOctRel,
            'defaultDk3': defaultDk3,
            'defaultDk4': defaultDk4,
            'defaultDk5': defaultDk5,
            'defaultDk61': defaultDk61,
            'defaultDk62': defaultDk62,
            'defaultDk7': defaultDk7,




            'nextButton': nextButton,

        }
                      )


def existanceFileName(inputTex_FilePath1,inputTex_FilePath2,inputTex_FilePath3,
inputTex_FilePath4,inputTex_FilePath5,inputTex_FilePath6,
inputTex_FilePath7,inputTex_FilePath8,inputTex_FilePath9,
inputTex_FilePath10,inputTex_FilePath11,inputTex_FilePath12,
inputTex_FilePath13,inputTex_FilePath14):
    value1 = ""
    value2 = ""
    value3 = ""
    value4 = ""
    value5 = ""
    value6 = ""
    value7 = ""
    value8 = ""
    value9 = ""
    value10 = ""
    value11 = ""
    value12 = ""
    value13 = ""
    value14 = ""



    import os

    if os.path.exists(inputTex_FilePath1):
        with open(inputTex_FilePath1, 'r') as file:
            for line in file:
                variable_name, value1 = line.split('=')
                value1 = value1.strip()
    else:
        with open(inputTex_FilePath1, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath2):
        with open(inputTex_FilePath2, 'r') as file:
            for line in file:
                variable_name, value2 = line.split('=')
                value2 = value2.strip()
    else:
        with open(inputTex_FilePath2, 'w') as file:
            file.write('')

    if os.path.exists(inputTex_FilePath3):
        with open(inputTex_FilePath3, 'r') as file:
            for line in file:
                variable_name, value3 = line.split('=')
                value3 = value3.strip()
    else:
        with open(inputTex_FilePath3, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath4):
        with open(inputTex_FilePath4, 'r') as file:
            for line in file:
                variable_name, value4 = line.split('=')
                value4 = value4.strip()
    else:
        with open(inputTex_FilePath4, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath5):
        with open(inputTex_FilePath5, 'r') as file:
            for line in file:
                variable_name, value5 = line.split('=')
                value5 = value5.strip()
    else:
        with open(inputTex_FilePath5, 'w') as file:
            file.write('')

    if os.path.exists(inputTex_FilePath6):
        with open(inputTex_FilePath6, 'r') as file:
            for line in file:
                variable_name, value6 = line.split('=')
                value6 = value6.strip()
    else:
        with open(inputTex_FilePath6, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath7):
        with open(inputTex_FilePath7, 'r') as file:
            for line in file:
                variable_name, value7 = line.split('=')
                value7 = value7.strip()
    else:
        with open(inputTex_FilePath7, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath8):
        with open(inputTex_FilePath8, 'r') as file:
            for line in file:
                variable_name, value8 = line.split('=')
                value8 = value8.strip()
    else:
        with open(inputTex_FilePath8, 'w') as file:
            file.write('')

    if os.path.exists(inputTex_FilePath9):
        with open(inputTex_FilePath9, 'r') as file:
            for line in file:
                variable_name, value9 = line.split('=')
                value9 = value9.strip()
    else:
        with open(inputTex_FilePath9, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath10):
        with open(inputTex_FilePath10, 'r') as file:
            for line in file:
                variable_name, value10 = line.split('=')
                value10 = value10.strip()
    else:
        with open(inputTex_FilePath10, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath11):
        with open(inputTex_FilePath11, 'r') as file:
            for line in file:
                variable_name, value11 = line.split('=')
                value11 = value11.strip()
    else:
        with open(inputTex_FilePath11, 'w') as file:
            file.write('')

    if os.path.exists(inputTex_FilePath12):
        with open(inputTex_FilePath12, 'r') as file:
            for line in file:
                variable_name, value12 = line.split('=')
                value12 = value12.strip()
    else:
        with open(inputTex_FilePath12, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath13):
        with open(inputTex_FilePath13, 'r') as file:
            for line in file:
                variable_name, value13 = line.split('=')
                value13 = value13.strip()
    else:
        with open(inputTex_FilePath13, 'w') as file:
            file.write('')


    if os.path.exists(inputTex_FilePath14):
        with open(inputTex_FilePath14, 'r') as file:
            for line in file:
                variable_name, value14 = line.split('=')
                value14 = value14.strip()
    else:
        with open(inputTex_FilePath14, 'w') as file:
            file.write('')







    return value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14
