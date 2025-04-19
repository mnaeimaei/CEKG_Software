from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, FileResponse
from django.http import HttpResponse

import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")



# Additional view to handle the PDF serving
def serve_pdf_func(request):
    username = request.user.username
    confDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    confPath = os.path.realpath(confDirectory)
    # Path to the PDF file
    savingTxt1 = confPath + "/" + "X1_dfgGraphvizPdfLocation.txt"

    with open(savingTxt1, 'r') as file:
        pdf_url = file.read()
        logger.info(f"\nPDF URL : {pdf_url}")

    if not os.path.exists(pdf_url):

        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")

def serve_dot_func(request):
    username = request.user.username
    confDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    confPath = os.path.realpath(confDirectory)
    savingTxt2 = confPath + "/" + "X2_dfgGraphvizDotLocation.txt"

    with open(savingTxt2, 'r') as file:
        dot_url = file.read()
        logger.info(f"\nDOT URL : {dot_url}")


    if not os.path.exists(dot_url):
        logger.error(f"File not found at {dot_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(dot_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {dot_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def serve_graphvizQuery_func(request):
    username = request.user.username
    confDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    confPath = os.path.realpath(confDirectory)
    savingTxt3 = confPath + "/" + "X3_dfgGraphvizQueryLocation.txt"

    with open(savingTxt3, 'r') as file:
        graphvizQuery_url = file.read()
        logger.info(f"\ngraphviz query URL : {graphvizQuery_url}")


    if not os.path.exists(graphvizQuery_url):
        logger.error(f"File not found at {graphvizQuery_url}")
        return HttpResponseNotFound("The requested graphviz query txt file was not found.")
    try:
        return FileResponse(open(graphvizQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {graphvizQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")







def serve_neo4jQuery_func(request):
    username = request.user.username
    confDirectory = f"./myapp/Data/users/{username}/0_DataConf"
    confPath = os.path.realpath(confDirectory)
    savingTxt5 = confPath + "/" + "X5_dfgNeo4jQueryLocation.txt"


    with open(savingTxt5, 'r') as file:
        neo4jQuery_url = file.read()
        logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




