from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, FileResponse
from django.http import HttpResponse

import os
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")




pdfDir = "./myapp/Data/general/0_MultiMedia/graph_home"
pdfLoc = os.path.realpath(pdfDir)
print(pdfLoc)



def serve_pdf_func_step1_01(request):
    pdf_url = pdfLoc + "/Step1/Step1_01.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step1_02(request):
    pdf_url = pdfLoc + "/Step1/Step1_02.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step1_03(request):
    pdf_url = pdfLoc + "/Step1/Step1_03.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step1_04(request):
    pdf_url = pdfLoc + "/Step1/Step1_04.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step1_05(request):
    pdf_url = pdfLoc + "/Step1/Step1_05.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step1_06(request):
    pdf_url = pdfLoc + "/Step1/Step1_06.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


###########################################################################################

def serve_pdf_func_step2_1(request):
    pdf_url = pdfLoc + "/Step2_1/Step2_1.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_2(request):
    pdf_url = pdfLoc + "/Step2_1/Step2_2.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_3(request):
    pdf_url = pdfLoc + "/Step2_1/Step2_3.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_4(request):
    pdf_url = pdfLoc + "/Step2_1/Step2_4.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_5(request):
    pdf_url = pdfLoc + "/Step2_1/Step2_5.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_6(request):
    pdf_url = pdfLoc + "/Step2_1/Step2_6.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_7(request):
    pdf_url = pdfLoc + "/Step2_1/Step2_7.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_8(request):
    pdf_url = pdfLoc + "/Step2_1/Step2_8.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")

###########################################################################################

def serve_pdf_func_step2_09(request):
    pdf_url = pdfLoc + "/Step2_2/Step2_09.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_10(request):
    pdf_url = pdfLoc + "/Step2_2/Step2_10.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_11(request):
    pdf_url = pdfLoc + "/Step2_2/Step2_11.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_12(request):
    pdf_url = pdfLoc + "/Step2_2/Step2_12.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")





def serve_pdf_func_step2_13(request):
    pdf_url = pdfLoc + "/Step2_2/Step2_13.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step2_14(request):
    pdf_url = pdfLoc + "/Step2_2/Step2_14.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_15(request):
    pdf_url = pdfLoc + "/Step2_2/Step2_15.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_16(request):
    pdf_url = pdfLoc + "/Step2_2/Step2_16.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")

#########################################################################


def serve_pdf_func_step2_17(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_17.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_18(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_18.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")





def serve_pdf_func_step2_19(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_19.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step2_20(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_20.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step2_21(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_21.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_22(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_22.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_23(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_23.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_24(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_24.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_25(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_25.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_26(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_26.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_27(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_27.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_28(request):
    pdf_url = pdfLoc + "/Step2_3/Step2_28.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


#################################################################################

def serve_pdf_func_step2_29(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_29.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_30(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_30.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_31(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_31.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_32(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_32.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step2_33(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_33.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_34(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_34.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_35(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_35.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_36(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_36.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")





def serve_pdf_func_step2_37(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_37.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step2_38(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_38.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_39(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_39.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_40(request):
    pdf_url = pdfLoc + "/Step2_4/Step2_40.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


########################################################################################3

def serve_pdf_func_step2_41(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_41.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_42(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_42.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")





def serve_pdf_func_step2_43(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_43.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step2_44(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_44.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step2_45(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_45.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_46(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_46.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_47(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_47.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_48(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_48.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_49(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_49.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_50(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_50.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_51(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_51.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_52(request):
    pdf_url = pdfLoc + "/Step2_5/Step2_52.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


##################################################################################

def serve_pdf_func_step2_53(request):
    pdf_url = pdfLoc + "/Step2_6/Step2_53.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step2_54(request):
    pdf_url = pdfLoc + "/Step2_6/Step2_54.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


#########################################################################################

def serve_pdf_func_step3_01(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_01.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step3_02(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_02.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step3_03(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_03.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step3_04(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_04.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step3_05(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_05.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step3_06(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_06.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")





def serve_pdf_func_step3_07(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_07.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")



def serve_pdf_func_step3_08(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_08.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step3_09(request):
    pdf_url = pdfLoc + "/Step3_1_5/Step3_09.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")

############################################################################################


def serve_pdf_func_step3_option(request):
    pdf_url = pdfLoc + "/Step3_6/Step3_option.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")

############################################################################################


def serve_pdf_func_step4_01(request):
    pdf_url = pdfLoc + "/Step4_1_5/Step4_01.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")




def serve_pdf_func_step4_02(request):
    pdf_url = pdfLoc + "/Step4_1_5/Step4_02.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")





def serve_pdf_func_step4_03(request):
    pdf_url = pdfLoc + "/Step4_1_5/Step4_03.pdf"

    if not os.path.exists(pdf_url):
        logger.error(f"File not found at {pdf_url}")
        return HttpResponseNotFound("The requested PDF was not found.")
    try:
        return FileResponse(open(pdf_url, 'rb'), content_type='application/pdf')
    except Exception as e:
        logger.error(f"Failed to read the file at {pdf_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


