# Project Ubenyo by Alex Arbuckle #


# import <
from os import system
from torch.hub import load
from PIL.ImageGrab import grab
from pyautogui import click, locateOnScreen

# >


# global <
time = 59
model = load('ultralytics/yolov5', 'yolov5s')
applicationPath = '/Application/BlueStacks.app'

# >


def start():
    '''  '''

    # start bluestack <
    # select blink application <
    system(f'open {applicationPath}')
    click(locateOnScreen('asset/blink.png'))

    # >


def monitor():
    '''  '''

    # select clips <
    # get video state <
    click(locateOnScreen('asset/clips.png'))
    isNewVideo = locateOnScreen('asset/new.png')

    # >

    # if (new video) <
    if (isNewVideo):

        # click video <
        # iterate (screenshot) <
        click(isNewVideo)


        # for i in range(time):

        #     pass

        # >
    
    # >


def analyze():
    '''  '''

    pass


# main <
if (__name__ == '__main__'):

    # img = grab()  # take a screenshot

    # # Inference
    # results = model(img)
    # results.show() # or .print(), .save(), .crop(), .pandas(), etc.

    # # Image
    # img = grab()  # take a screenshot

    # # Inference
    # results = model(img)


    monitor()

    pass


    # x = locateOnScreen('asset/got.png')

    # print('ok') if (x) else print('e')

# >