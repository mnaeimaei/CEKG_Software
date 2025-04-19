from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, FileResponse
from django.http import HttpResponse

import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")



svgLocDir = "./myapp/Data/general/0_MultiMedia/graph_Location"
svgLoc = os.path.realpath(svgLocDir)
svgDir = svgLoc + "/" + '07_OCT_REL'
print(svgDir)

def seve_neo4jQuery_funcQ1_sctRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '07_OCT_REL'
    neo4jQuery_url = outDir + "/" + "Q1.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ2_sctRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '07_OCT_REL'
    neo4jQuery_url = outDir + "/" + "Q2.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ3_sctRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '07_OCT_REL'
    neo4jQuery_url = outDir + "/" + "Q3.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


################################################################################



def seve_neo4jQuery_svgQ2_sctRel(request):
    savingTxt = svgDir + "/" + "Q2_svg_location.txt"

    try:
        with open(savingTxt, 'r') as file:
            svg_url = file.read().strip()  # Read and strip any extra whitespace
            svg_url = os.path.realpath(svg_url)
        logger.info(f"SVG URL: {svg_url}")

        if not os.path.exists(svg_url):
            logger.error(f"File not found at {svg_url}")
            return HttpResponseNotFound("The requested SVG was not found.")

        return FileResponse(open(svg_url, 'rb'), content_type='image/svg+xml')
    except Exception as e:
        logger.error(f"Failed to read the file at {svg_url}: {e}")
        return HttpResponseNotFound("Error accessing the SVg file.")




def seve_neo4jQuery_svgQ3_sctRel(request):
    savingTxt = svgDir + "/" + "Q3_svg_location.txt"

    try:
        with open(savingTxt, 'r') as file:
            svg_url = file.read().strip()  # Read and strip any extra whitespace
            svg_url = os.path.realpath(svg_url)
        logger.info(f"SVG URL: {svg_url}")

        if not os.path.exists(svg_url):
            logger.error(f"File not found at {svg_url}")
            return HttpResponseNotFound("The requested SVG was not found.")

        return FileResponse(open(svg_url, 'rb'), content_type='image/svg+xml')
    except Exception as e:
        logger.error(f"Failed to read the file at {svg_url}: {e}")
        return HttpResponseNotFound("Error accessing the SVg file.")





