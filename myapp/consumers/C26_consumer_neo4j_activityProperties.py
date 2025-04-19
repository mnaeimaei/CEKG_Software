import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import os
import ast
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ScriptProgressConsumerC26(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("progress_group", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("progress_group", self.channel_name)

    async def receive(self, text_data):
        username = self.scope["user"].username

        pyDirectory = "./myapp/utils"
        script_directory = os.path.realpath(pyDirectory)

        confDirectory = f"./myapp/Data/users/{username}/0_DataConf"
        confPath = os.path.realpath(confDirectory)

        openingPath = confPath + "/3_pageSequencePart3.txt"
        with open(openingPath, 'r') as file:
            data = file.read()
            runingScripts = ast.literal_eval(data)

        message = text_data
        logger.info(f"\nmessage: {message}")

        if text_data == "run_scripts":
            scripts = [
                'E04_Step2_acProperty_importingNeo4J1.py'
            ]
            # Schedule the script execution as an asynchronous task
            asyncio.create_task(self.run_scripts(script_directory, scripts))
            # Schedule the script execution as an asynchronous task
            #asyncio.create_task(self.run_scripts(script_directory, runingScripts[3]))
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
