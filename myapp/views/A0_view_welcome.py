from django.shortcuts import render, redirect

from myapp.forms import StartButton


import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")


def welcome_view(request):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an welcome view and A0_welcome.html")


    if request.method == 'POST' :
        logger.info(f"################ request.method == 'POST' ################")



        return redirect('sign')

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        stButton = StartButton()
        return render(request, 'A0_welcome.html', {
            'stButton': stButton,


        }
                      )

