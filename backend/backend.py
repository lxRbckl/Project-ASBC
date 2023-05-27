# import <
from os import system
from random import choice
from asyncio import sleep
from torch.hub import load
from lxRbckl import jsonLoad
from os import system, listdir
from PIL.ImageGrab import grab
from pyautogui import click, locateOnScreen

from backend.resource import gDirectory, gConfigurationPath

# >


class backend:

    # attribute <
    dataPath = 'backend/data'
    assetPath = 'backend/asset'
    model = load('ultralytics/yolov5', 'yolov5s')

    # >


    def __init__(self):
        '''  '''

        self.configuration = self.update()
    

    async def start(
            
        self,
        icon: str,
        pSleep: int = 15

    ):
        '''  '''

        # open application given icon <
        # wait for application to open <
        click(locateOnScreen(image = f'{gDirectory}/{self.assetPath}/{icon}'))
        await sleep(pSleep)

        # >

    
    def check(
            
            self,
            pConfidence: float = 0.8
            
        ):
        ''' find if there is new footage to view '''

        # return video status <
        return locateOnScreen(
            
            confidence = pConfidence,
            image = f'{gDirectory}/{self.assetPath}/new.png'
        
        )

        # >
    

    async def monitor(
            
            self,
            status
            
        ):
        ''' record new footage to be analyzed '''

        # local <
        images = []

        # >

        print(type(status)) # remove

        # if (new video) <
        if (status):

            # select new video <
            click(status, clicks = 2)
            await sleep(3)

            # >

            # iterate (duration) <
            for i in range(self.configuration['duration']):

                image = grab()
                images.append(image)

                await sleep(1)
            
            # >
            
        # >

        return images
    

    def analyze(
            
        self,
        images: list

    ):
        ''' review and idenitfy recording using model '''

        # local <
        data = {}
        analyzed = []

        # >

        # iterate (images) <
        for i in images:

            # analyze image <
            # yield (name, confidence) from result <
            result = self.model(i)
            data = result.pandas().xyxyn[0][['name', 'confidence']].to_numpy()

            # >

            # iterate (name, confidence) <
            for name, confidence in data:

                # condition <
                reqWatch = (name in self.configuration['watch'])
                reqConfidence = ((confidence * 100) > self.configuration['confidence'])

                # >

                # if ((priority) and (confident)) <
                if (reqWatch and reqConfidence):

                    result.crop(save_dir = f'{gDirectory}/{self.dataPath}/ultralytics')
                    analyzed.append((name, round((confidence * 100), 2)))

                # >
            
            # >
        
        # >

        return analyzed


    def get(self):
        ''' get data stored by model '''

        # local <
        data = {}
        path = f'{gDirectory}/{self.dataPath}'

        # >

        # iterate (analyzed) <
        for i in listdir(path = path)[::-1]:

            # iterate (show) <
            for j in listdir(path = f'{path}/{i}/crops'):

                # if (is watched) <
                if (j in self.configuration['watch']):

                    data[f'{i}{j.title()}'] = {

                        'object' : j.title(),
                        'path' : f'{path}/{i}/crops/{j}',
                        'count' : len(listdir(path = f'{path}/{i}/crops/{j}')),
                        'file' : choice(listdir(path = f'{path}/{i}/crops/{j}'))

                    }

                # >

            # >
            
        # >

        return data


    def update(self):
        ''' retrieve new settings from user interface '''

        # get recent configuration <
        # update instance value <
        configuration = jsonLoad(pFile = f'{gDirectory}/{gConfigurationPath}')
        self.configuration = configuration

        # >

        return configuration
    

    async def refresh(self):
        ''' retrieve new videos from Blink app '''

        # click home page <
        # click clips page <
        click(locateOnScreen(image = f'{gDirectory}/{self.assetPath}/home.png'))
        await sleep(2)
        click(locateOnScreen(image = f'{gDirectory}/{self.assetPath}/clips.png'))

        # >


    def clear(self):
        ''' remove temporary data created by ultralytics model '''

        # recursively remove files from directory <
        system(f'rm -r {gDirectory}/{self.dataPath}/')

        # >