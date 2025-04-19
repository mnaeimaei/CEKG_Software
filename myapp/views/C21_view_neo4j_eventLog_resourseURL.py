
from django.http import HttpResponseNotFound, FileResponse


import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")


multiLocDir = "./myapp/Data/general/0_MultiMedia"
multiLoc = os.path.realpath(multiLocDir)
print(multiLoc)

svgLocDir = "./myapp/Data/general/0_MultiMedia/graph_Location"
svgLoc = os.path.realpath(svgLocDir)
svgDir = svgLoc + "/" + '01_EventLog'
print(svgDir)


def seve_neo4jQuery_funcQ1_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ2_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ3_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ4_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ5_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ6_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ7_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ8_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ9_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ10_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ11_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_funcQ12_EventLog(request):
    username = request.user.username
    downloadDir = f'../../media/{username}/download/dfgTool'
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'
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


def seve_neo4jQuery_svgQ4_EventLog(request):
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


def seve_neo4jQuery_svgQ5_EventLog(request):
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

def seve_neo4jQuery_svgQ6_EventLog(request):
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


def seve_neo4jQuery_svgQ7_EventLog(request):
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

def seve_neo4jQuery_svgQ8_EventLog(request):
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


def seve_neo4jQuery_svgQ9_EventLog(request):
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


def seve_neo4jQuery_svgQ10_EventLog(request):
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


def seve_neo4jQuery_svgQ11_EventLog(request):
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


def seve_neo4jQuery_svgQ12_EventLog(request):
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



