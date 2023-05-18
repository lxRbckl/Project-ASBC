# import <
from time import sleep
from random import choice
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

    
    def open(self):
        '''  '''

        # start bluestack on desktop <
        click(locateOnScreen(f'{gDirectory}/{self.assetPath}/bluestacks.png'), clicks = 2)

        # >
    

    def start(
            
        self,
        icon: str

    ):
        '''  '''

        # open application given icon <
        click(locateOnScreen(f'{gDirectory}/{self.assetPath}/{icon}'))

        # >
    

    def monitor(self):
        '''  '''

        # local <
        images = []

        # >

        # select 'clips' <
        # get video status <
        click(locateOnScreen(f'{gDirectory}/{self.assetPath}/clips.png'))
        newVideo = locateOnScreen(f'{gDirectory}/{self.assetPath}/new.png')

        # >

        # if (new video) <
        if (newVideo):

            # select new video <
            # iterate (duration) <
            click(newVideo)
            for i in range(self.configuration['duration']):

                image = grab()
                images.append(image)

                sleep(1)
            
            # >
            
        # >

        return images
    

    def analyze(
            
        self,
        images: list

    ):
        '''  '''

        # local <
        data = {}
        analyzed = []
        threshold = 0

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
                reqThreshold = (threshold < self.configuration['threshold'])
                reqConfidence = ((confidence * 100) > self.configuration['confidence'])

                # >

                # if ((priority) and (insufficient data) and (confident)) <
                if (reqWatch and reqThreshold and reqConfidence):

                    result.crop(save_dir = f'{gDirectory}/{self.dataPath}/ultralytics')
                    analyzed.append((name, round((confidence * 100), 2)))
                    threshold += 1

                # >
            
            # >
        
        # >

        return analyzed


    def get(self):
        '''  '''

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
        '''  '''

        # get recent configuration <
        # update instance value <
        configuration = jsonLoad(pFile = f'{gDirectory}/{gConfigurationPath}')
        self.configuration = configuration

        # >

        return configuration
    

    def refresh(self):
        '''  '''

        # click home page <
        # click clips page <
        click(locateOnScreen(f'{gDirectory}/{self.assetPath}/home.png'))
        click(locateOnScreen(f'{gDirectory}/{self.assetPath}/clips.png'))

        # >


    def clear(self):
        '''  '''

        # recursively remove files from directory <
        system(f'rm -r {gDirectory}/{self.dataPath}/')

        # >