import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import os
import ast
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ScriptProgressConsumerC30(AsyncWebsocketConsumer):
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
                'H04_Step18_ClinicalEntity_importingNeo4J.py'
            ]
            # Schedule the script execution as an asynchronous task
            asyncio.create_task(self.run_scripts(script_directory, scripts))
            # Schedule the script execution as an asynchronous task
            #asyncio.create_task(self.run_scripts(script_directory, runingScripts[5]))
        else:
            await self.send(text_data="Unknown command")

    async def run_scripts(self, script_directory, scripts):
        total = len(scripts)
        channel_layer = self.channel_layer
        import subprocess

        for i, script in enumerate(scripts):
            process = subprocess.Popen(['python', script], cwd=script_directory, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, universal_newlines=True)

            for line in process.stdout:
                print(line)
                if line.startswith("Completed: "):
                    # Parse the progress from the line
                    progress = float(line.split(":")[1].strip()[:-1])
                    print(f"Progress: {progress}%")

                    # Send progress to the channel group
                    await channel_layer.group_send(
                        'progress_group',  # This must match the group name used in the consumer
                        {
                            'type': 'progress_message',  # This must match the handler method name in the consumer
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
