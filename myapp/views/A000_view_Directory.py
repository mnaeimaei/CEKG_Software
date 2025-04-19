from django.conf import settings
from django.http import FileResponse, Http404, HttpResponseRedirect
from django.shortcuts import render,redirect
import os
import os
import urllib.parse
from myapp.forms import StartButton


from django.http import HttpResponse
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("myapp")



def directory(request, path=''):
    logger.info(f"********************************************************************************************************************************************************************************************")
    logger.info("This is an directory view and A000_Directory.html")

    if request.method == 'POST':
        logger.info(f"################ request.method == 'POST' ################")
        logger.debug(f"Hello23")
        logger.info("This is an info message")

        return redirect('home')

    else:
        logger.info(f"################ request.method == 'ELSE' ################")

        username = request.user.username
        base_dir = create_user_download_folder(username)
        current_path = os.path.normpath(os.path.join(base_dir, path))

        # Security check to ensure no access beyond media root
        if not current_path.startswith(base_dir):
            return HttpResponseRedirect('/directory/')

        if os.path.isfile(current_path):
            # Serve the file if it's a direct file request
            return HttpResponse(open(current_path, 'rb'), content_type="application/octet-stream")

        # List directories and files
        try:
            entries = os.listdir(current_path)
        except FileNotFoundError:
            entries = []

        files_and_dirs = []
        for entry in entries:
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                files_and_dirs.append({'name': entry, 'is_dir': True, 'path': urllib.parse.quote(os.path.relpath(full_path, base_dir))})
            else:
                files_and_dirs.append({'name': entry, 'is_dir': False, 'path': urllib.parse.quote(os.path.relpath(full_path, base_dir))})

        # Sort directories and files
        files_and_dirs.sort(key=lambda x: (not x['is_dir'], x['name'].lower()))

        # Navigation: Up one level (unless at root)
        parent_path = '/' if current_path == base_dir else urllib.parse.quote(os.path.relpath(os.path.dirname(current_path), base_dir))

        startButton = StartButton()
        return render(request, 'A000_Directory.html', {
            'files_and_dirs': files_and_dirs,
            'current_path': path,
            'parent_path': parent_path,
            'startButton': startButton
        })


def create_user_download_folder(username):
    user_folder = os.path.join(settings.MEDIA_ROOT, f"{username}")
    download_folder = os.path.join(user_folder, 'download')
    return download_folder