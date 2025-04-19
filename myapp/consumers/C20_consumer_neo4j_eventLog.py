import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import os
import ast
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ScriptProgressConsumerC20(AsyncWebsocketConsumer):
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


        softwareTypeDirectory = f"./myapp/Data/general/0_GenConf/0_appType.txt"
        appTypeTxt = os.path.realpath(softwareTypeDirectory)


        openingPath = confPath + "/3_pageSequencePart3.txt"
        with open(openingPath, 'r') as file:
            data = file.read()
            runingScripts = ast.literal_eval(data)

        with open(appTypeTxt, 'r') as file:
            for line in file:
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                value = int(value.strip())
                if variable_name == 'appType':
                    appType = value

        message = text_data
        logger.info(f"\nmessage: {message}")

        if text_data == "run_scripts":
            scripts = [
                    'A3_EntryCol_Step2_logConf_Step.py',  # Converting     # Download Cloud
                    'A5_EntryCol_Step3_Step.py',  # Converting     # Download Cloud
                    'A6_Scenario_Final_Step.py',  # Converting     # Download Cloud
                    'A7_csv_generator_Step.py',  # Converting     # Download Cloud
                    'A8_csv_save_Step.py',  # Converting     # Download Cloud
                    'A9_csv_link_Step.py',  # Converting      # UploadingLink Cloud
                    'C04_Step2_Log_importingNeo4J1.py',  # Converting     # Converting Cloud
                ]




            # Schedule the script execution as an asynchronous task
            asyncio.create_task(self.run_scripts(script_directory, scripts))

            # Schedule the script execution as an asynchronous task
            #asyncio.create_task(self.run_scripts(script_directory, runingScripts[0]))
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
