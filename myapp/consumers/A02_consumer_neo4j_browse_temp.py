import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import os
import ast
import logging

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
        username = self.scope["user"].username

        pyDirectory = "./myapp/utils"
        script_directory = os.path.realpath(pyDirectory)


        message = text_data
        logger.info(f"\nmessage: {message}")

        if text_data == "run_scripts":
            scripts = [
                'A2_FileLocation_Step2_xlsx_Step.py',
                'A2_FileLocation_Step3_sheetName_Step.py'
            ]
            asyncio.create_task(self.run_scripts(script_directory, scripts))

        else:
            await self.send(text_data="Unknown command")

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
