
from django.http import HttpResponseNotFound, FileResponse


import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")







multiLocDir = "./myapp/Data/general/0_MultiMedia/graph_conversion"
multiLoc = os.path.realpath(multiLocDir)
print(multiLoc)




def seve_jpegCKEG16(request):

    username = request.user.username
    jpeg_url = multiLoc + "/" + "CEKG_16.jpeg"

    if not os.path.exists(jpeg_url):
        logger.error(f"File not found at {jpeg_url}")
        return HttpResponseNotFound("The requested JPEG was not found.")
    try:
        return FileResponse(open(jpeg_url, 'rb'), content_type='image/jpeg')
    except Exception as e:
        logger.error(f"Failed to read the file at {jpeg_url}: {e}")
        return HttpResponseNotFound("Error accessing the JPEG file.")




