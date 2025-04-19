from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, FileResponse
from myapp.forms import BroweserButton
import os
import logging
import fcntl

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")

def DFG(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an DFG view and E53_DFG.html")
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



    if request.method == 'POST':
        logger.info(f"################ request.method == 'POST' ################")

        return redirect('directory')

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        browseButton = BroweserButton()

        import os
        savingTxt1 = confPath + "/" + "X1_dfgGraphvizPdfLocation.txt"
        savingTxt2 = confPath + "/" + "X2_dfgGraphvizDotLocation.txt"
        savingTxt3 = confPath + "/" + "X3_dfgGraphvizQueryLocation.txt"
        savingTxt5 = confPath + "/" + "X5_dfgNeo4jQueryLocation.txt"

        with open(savingTxt1, 'r') as file:
            pdf_url = file.read()
            logger.info(f"\nPDF URL : {pdf_url}")

        with open(savingTxt2, 'r') as file:
            dot_url = file.read()
            logger.info(f"\nDOT URL : {dot_url}")

        with open(savingTxt3, 'r') as file:
            graphvizQuery_url = file.read()
            logger.info(f"\ngraphviz query URL : {graphvizQuery_url}")
        with open(graphvizQuery_url, 'r') as file:
            graphvizQuery = file.read()
            logger.info(f"\ngraphvizQuery : {graphvizQuery}")


        with open(savingTxt5, 'r') as file:
            neo4jQuery_url = file.read()
            logger.info(f"\nneo4j query URL : {neo4jQuery_url}")
        with open(neo4jQuery_url, 'r') as file:
            neo4jQuery = file.read()
            logger.info(f"\nneo4jQuery: {neo4jQuery}")


        return render(request, 'E53_DFG.html', {
            'browseButton': browseButton,
            'pdf_url': pdf_url,
            'dot_url': dot_url,
            'graphvizQuery': graphvizQuery,
            'neo4jQuery': neo4jQuery,

        })

