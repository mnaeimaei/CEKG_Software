from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, FileResponse
from django.http import HttpResponse

import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")



svgLocDir = "./myapp/Data/general/0_MultiMedia/graph_Location"
svgLoc = os.path.realpath(svgLocDir)
svgDir = svgLoc + "/" + '02_EntityRel'
print(svgDir)



def seve_neo4jQuery_funcQ1_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
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


def seve_neo4jQuery_funcQ2_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
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


def seve_neo4jQuery_funcQ3_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
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


def seve_neo4jQuery_funcQ4_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q4.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ5_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q5.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ6_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q6.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ7_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q7.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ8_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q8.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ9_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q9.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ10_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q10.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")
    
    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ11_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q11.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ12_entityRel(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '02_EntityRel'
    neo4jQuery_url = outDir + "/" + "Q12.txt"
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





def seve_neo4jQuery_svgQ3_entityRel(request):
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




def seve_neo4jQuery_svgQ6_entityRel(request):
    savingTxt = svgDir + "/" + "Q6_svg_location.txt"

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




def seve_neo4jQuery_svgQ7_entityRel(request):
    savingTxt = svgDir + "/" + "Q7_svg_location.txt"

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




def seve_neo4jQuery_svgQ8_entityRel(request):
    savingTxt = svgDir + "/" + "Q8_svg_location.txt"

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




def seve_neo4jQuery_svgQ9_entityRel(request):
    savingTxt = svgDir + "/" + "Q9_svg_location.txt"

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




def seve_neo4jQuery_svgQ10_entityRel(request):
    savingTxt = svgDir + "/" + "Q10_svg_location.txt"

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




def seve_neo4jQuery_svgQ11_entityRel(request):
    savingTxt = svgDir + "/" + "Q11_svg_location.txt"

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




def seve_neo4jQuery_svgQ12_entityRel(request):
    savingTxt = svgDir + "/" + "Q12_svg_location.txt"

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



