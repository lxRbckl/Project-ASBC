# import <
from asyncio import sleep
from discord.ext import commands
from discord import Intents, Embed, File

from backend.backend import backend

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
    object: str,
    channel: int,
    confidence: float
    
):
    '''  '''

    # local <
    title = f'{object} identified.'
    f = File(f'{path}/{file}', filename = 'image.png')
    description = f'**{object}** has been identified with **{confidence}**% confidence.'

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

    # start (blink) <
    # wait to load <
    obj.start(icon = 'blink.png')
    await sleep(10)

    # >

    # while (running) <
    while (True):

        # update <
        obj.update()

        # >

        # if (online) <
        # else (then sleeping) <
        if (obj.configuration['online']):

            # screen grab <
            # analyze grabs <
            images = await obj.monitor()
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

        # refresh <
        # sleep <
        await obj.refresh()
        await sleep(obj.configuration['sleep'])

        # >
    
    # >