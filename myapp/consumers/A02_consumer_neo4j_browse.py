import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import os
import ast
import logging
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ScriptProgressConsumerA02(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("progress_group", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("progress_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        if data.get("action") == "upload_file":
            # Handle the file upload
            upload_success = await self.handle_file_upload(data)

            pyDirectory = "./myapp/utils"
            script_directory = os.path.realpath(pyDirectory)

            scripts = [
                'A2_FileLocation_Step2_xlsx_Step.py',
                'A2_FileLocation_Step3_sheetName_Step.py'
            ]


            if upload_success:
                # If the file upload was successful, run the scripts
                asyncio.create_task(self.run_scripts(script_directory, scripts))
            else:
                await self.send(text_data=json.dumps({"error": "File upload failed"}))

        else:
            await self.send(text_data=json.dumps({"error": "Unknown action"}))

    async def handle_file_upload(self, data):
        username = self.scope["user"].username
        file_name = data.get("file_name")
        file_content = data.get("file_content")

        if file_name and file_content:
            try:
                # Decode the file content from Base64
                file_content = ContentFile(base64.b64decode(file_content))

                # Save the file
                fs = FileSystemStorage(location=f'media/{username}/uploads/0_Data')
                fs.save(file_name, file_content)

                # Inform the client that the upload was successful
                await self.send(json.dumps({"status": "File uploaded successfully"}))
                logger.info(f"File uploaded: {file_name}")
                return True
            except Exception as e:
                logger.error(f"File upload failed: {str(e)}")
                return False
        else:
            await self.send(json.dumps({"status": "Failed to upload file"}))
            return False

    async def run_scripts(self, script_directory, scripts):
        total = len(scripts)
        channel_layer = self.channel_layer

        for i, script in enumerate(scripts):
            progress = (i + 0.5) / total * 100
            logger.info(f"Progress in Func1: {progress}")
            await channel_layer.group_send(
                'progress_group',
                {
                    'type': 'progress_message',
                    'progress': progress
                }
            )
            await asyncio.sleep(0)

            process = await asyncio.create_subprocess_exec(
                'python', script, cwd=script_directory
            )
            await process.wait()

            progress = (i + 1) / total * 100
            logger.info(f"Progress in Func 2: {progress}")
            await channel_layer.group_send(
                'progress_group',
                {
                    'type': 'progress_message',
                    'progress': progress
                }
            )
            await asyncio.sleep(0)

        # Final progress update to indicate completion
        await channel_layer.group_send(
            'progress_group',
            {
                'type': 'progress_message',
                'progress': 100  # Indicating completion
            }
        )
        await asyncio.sleep(0)

    async def progress_message(self, event):
        progress = event['progress']
        await self.send(text_data=json.dumps({
            'progress': progress
        }))
