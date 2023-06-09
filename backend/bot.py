# import <
from asyncio import sleep
from lxRbckl import jsonLoad
from discord.ext import commands
from discord import Intents, Embed, File

from backend.module import module
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
    object: str,
    channel: int,
    confidence: float
    
):
    ''' send a discord notification '''

    # local <
    title = f'{object} identified.'
    f = File(f'{path}/{file}', filename = 'image.png')
    description = f'**{object}** has been identified with **{confidence:.2f}**% confidence.'

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
    ''' run functions of module on runtime '''

    # initialize object <
    iteration = 0
    obj = module()
    threshold = 300
    icon = 'Blink.png'
    await obj.load(pIcon = icon)

    # >

    # while (running) <
    while (True):

        # if (online) <
        # if (reboot needed) <
        if (obj.configuration['online']):

            # get status of footage <
            # record footage if new footage <
            # review and identify footage from recording <
            status = obj.check()
            images = await obj.monitor(status = status)
            highlights = obj.analyze(images = images)

            # >

            # if (notable observation(s)) <
            if (highlights):

                # iterate (notable footage) <
                # clear saved notable footage <
                for (k, v), i in zip(obj.get().items(), highlights):

                    await notify(

                        **v,
                        confidence = i[1],
                        channel = obj.configuration['channel']

                    )
                
                obj.clear()

                # >

            # >

        if (iteration > threshold):

            iteration = 0
            await obj.restart()
            await obj.load(pIcon = icon)

        # >

        # cycle <
        iteration += 1

        obj.update()
        await obj.refresh()
        await sleep(obj.configuration['sleep'])

        # >
        
    # >


def run(): bot.run(jsonLoad(pFile = f'{gDirectory}/{gConfigurationPath}')['token'])