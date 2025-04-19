from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, FileResponse
from django.http import HttpResponse

import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")




svgLocDir = "./myapp/Data/general/0_MultiMedia/graph_Location"
svgLoc = os.path.realpath(svgLocDir)
svgDir = svgLoc + "/" + '15_Final'
print(svgDir)


def seve_neo4jQuery_funcQ1_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ2_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ3_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ4_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ5_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ6_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ7_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ8_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ9_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ10_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ11_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ12_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
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


def seve_neo4jQuery_funcQ13_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q13.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ14_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q14.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ15_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q15.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ16_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q16.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ17_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q17.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ18_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q18.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")

def seve_neo4jQuery_funcQ19_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q19.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ20_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q20.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ21_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q21.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ22_Final(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'
    neo4jQuery_url = outDir + "/" + "Q22.txt"
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


def seve_neo4jQuery_svgQ3_Final(request):
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




def seve_neo4jQuery_svgQ4_Final(request):
    savingTxt = svgDir + "/" + "Q4_svg_location.txt"

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




def seve_neo4jQuery_svgQ5_Final(request):
    savingTxt = svgDir + "/" + "Q5_svg_location.txt"

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




def seve_neo4jQuery_svgQ6_Final(request):
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



def seve_neo4jQuery_svgQ7_Final(request):
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




def seve_neo4jQuery_svgQ8_Final(request):
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



def seve_neo4jQuery_svgQ9_Final(request):
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




def seve_neo4jQuery_svgQ10_Final(request):
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



def seve_neo4jQuery_svgQ11_Final(request):
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




def seve_neo4jQuery_svgQ12_Final(request):
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




def seve_neo4jQuery_svgQ13_Final(request):
    savingTxt = svgDir + "/" + "Q13_svg_location.txt"

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



def seve_neo4jQuery_svgQ14_Final(request):
    savingTxt = svgDir + "/" + "Q14_svg_location.txt"

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



def seve_neo4jQuery_svgQ15_Final(request):
    savingTxt = svgDir + "/" + "Q15_svg_location.txt"

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




def seve_neo4jQuery_svgQ16_Final(request):
    savingTxt = svgDir + "/" + "Q16_svg_location.txt"

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




def seve_neo4jQuery_svgQ17_Final(request):
    savingTxt = svgDir + "/" + "Q17_svg_location.txt"

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



def seve_neo4jQuery_svgQ18_Final(request):
    savingTxt = svgDir + "/" + "Q18_svg_location.txt"

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




def seve_neo4jQuery_svgQ19_Final(request):
    savingTxt = svgDir + "/" + "Q19_svg_location.txt"

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




def seve_neo4jQuery_svgQ20_Final(request):
    savingTxt = svgDir + "/" + "Q20_svg_location.txt"

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




def seve_neo4jQuery_svgQ21_Final(request):
    savingTxt = svgDir + "/" + "Q21_svg_location.txt"

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




def seve_neo4jQuery_svgQ22_Final(request):
    savingTxt = svgDir + "/" + "Q22_svg_location.txt"

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

