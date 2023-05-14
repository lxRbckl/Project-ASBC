# Project Ubenyo by Alex Arbuckle #


# import <
from time import sleep
from torch.hub import load
from PIL.ImageGrab import grab
from discord.ext import commands
from os import system, path, listdir
from discord import Intents, Embed, File
from pyautogui import click, locateOnScreen

# >


# global <
gThreshold = 1
gVideoLength = 2
gWatchList = ('person')
gChannel = 1106111647057203242
gPath = path.realpath(__file__).split('/')
gModel = load('ultralytics/yolov5', 'yolov5s')
gDirectory = '/'.join(gPath[:(len(gPath) - 1)])
gApplicationPath = '/Application/BlueStacks.app'
ubenyo = commands.Bot(command_prefix = '', intents = Intents.all())

gToken = ''

# >


def start():
    '''  '''

    # start bluestack <
    # select blink application <
    system(f'open {gApplicationPath}')
    click(locateOnScreen('asset/blink.png'))

    # >


async def monitor():
    '''  '''

    # local <
    images = []

    # >

    # select clips <
    # get video state <
    click(locateOnScreen('asset/clips.png'))
    newVideo = locateOnScreen('asset/new.png')

    # >

    # if (new video) <
    # if (isNewVideo):

    # click video <
    # iterate (length) <
    click(newVideo)
    for i in range(gVideoLength):

        image = grab()
        images.append(image)
    
    # >

    # send to analyzer <
    await analyze(images = images)

    # >

    # >


async def analyze(images):
    '''  '''

    # local <
    data = {}
    threshold = 0

    # >

    # iterate (image) <
    for image in images:

        # get object <
        # get cols from object <
        result = gModel(image)
        data = result.pandas().xyxyn[0][['name', 'confidence']].to_numpy()

        # >

        # iterate (observed) <
        for name, confidence in data:

            # if ((vip classifier) and (insufficient data)) <
            if ((name in gWatchList) and (gThreshold > threshold)):

                # crop <
                # notify <
                result.crop(save_dir = f'{gDirectory}/data/')
                await notify(

                    name = name,
                    confidence = confidence

                )

                # >

                # increment <
                # clear data <
                threshold += 1
                system(f'rm -r {gDirectory}/data')

                # >

            # >

        # >

    # >


async def notify(
        
        name, 
        confidence

):
    '''  '''

    # set <
    name = name.title()
    confidence = round((confidence * 100), 2)
    image = listdir(f'{gDirectory}/data/crops/{name.lower()}')[0]
    file = File(f'{gDirectory}/data/crops/{name.lower()}/{image}', filename = 'image.png')

    # >

    # set embed <
    # add image <
    embed = Embed(

        title = f'{name} identified.',
        description = f'A **{name}** has been identified with **{confidence}%** confidence.'

    )
    embed.set_image(url = 'attachment://image.png')

    # >

    await ubenyo.get_channel(gChannel).send(file = file, embed = embed)


@ubenyo.event
async def on_ready():
    '''  '''

    await monitor()


# main <
if (__name__ == '__main__'): ubenyo.run(gToken)

# >