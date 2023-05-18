# import <
from asyncio import sleep
from discord.ext import commands
from discord import Intents, Embed, File

from backend.backend import backend
from backend.resource import gDirectory, gConfigurationPath

# >


# global <
bot = commands.Bot(
    
    command_prefix = '', 
    intents = Intents.all()
    
)

# >


async def notify(
        
    path: str,
    file: str,
    count: int,
    object: str,
    channel: int,
    confidence: float
):
    '''  '''

    # local <
    title = f'{object} identified.'
    f = File(f'{path}/{file}', filename = 'image.png')
    description = f'**{count} {object}**(s) have been identified with **{confidence}**% confidence.'

    # >

    # build embed <
    # add image <
    embed = Embed(

        title = title,
        description = description

    )
    embed.set_image(url = 'attachment://image.png')

    # >

    await bot.get_channel(channel).send(
        
        file = f, 
        embed = embed
    
    )


@bot.event
async def on_ready():
    '''  '''


    # local <
    obj = backend()

    # >

    # open <
    # wait to load <
    # start (blink) <
    obj.open()
    await sleep(60)
    obj.start(icon = 'blink.png')

    # >

    # while (running) <
    while (True):

        # update <
        # load videos <
        # wait to load <
        obj.update()
        obj.refresh()
        await sleep(15)

        # >

        # if (online) <
        # else (then sleeping) <
        if (obj.configuration['online']):

            # screen grab <
            # analyze grabs <
            images = obj.monitor()
            analyzed = obj.analyze(images = images)

            # >

            # if (qualifying) <
            if (analyzed): 
                
                for (k, v), i in zip(obj.get().items(), analyzed):

                    await notify(
                        
                        **v, 
                        confidence = i[1],
                        channel = obj.configuration['channel']
                    
                    )

                obj.clear()
            
            # >

        else: pass

        # >

        # sleep <
        await sleep(obj.configuration['sleep'])

        # >
    
    # >