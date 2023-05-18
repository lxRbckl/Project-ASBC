# Project ASBC by Alex Arbuckle #


# import <
from multiprocessing import Process
from lxRbckl import jsonLoad, jsonDump
from dash.dependencies import Input, Output, State

from backend.bot import bot
from frontend.frontend import fLayout
from backend.resource import gDirectory, application, gConfigurationPath

# >


@application.callback(
        
    Output('layoutId', 'children'),
    Input('layoutId', 'children')

)
def layoutCallback(layoutChildren: list):
    '''  '''

    configuration = jsonLoad(pFile = f'{gDirectory}/{gConfigurationPath}')
    return fLayout(pConfiguration = configuration)


@application.callback(

    Output('alertId', 'is_open'),
    Input('submitId', 'n_clicks'),
    State('tokenId', 'value'),
    State('sleepId', 'value'),
    State('watchId', 'value'),
    State('onlineId', 'value'),
    State('channelId', 'value'),
    State('durationId', 'value'),
    State('thresholdId', 'value'),
    State('confidenceId', 'value')

)
def submitCallback(

    submitClick: int,
    tokenValue: str,
    sleepValue: int,
    watchValue: list,
    onlineValue: bool,
    channelValue: int,
    durationValue: int,
    thresholdValue: int,
    confidenceValue: float

):
    '''  '''

    preConfiguration = jsonLoad(pFile = f'{gDirectory}/{gConfigurationPath}')
    postConfiguration = {

        **{

            'token' : tokenValue,
            'watch' : watchValue,
            'online' : onlineValue,
            'channel' : channelValue,
            'sleep' : int(sleepValue),
            'duration' : durationValue,
            'threshold' : thresholdValue,
            'confidence' : float(confidenceValue)

        },
        'all' : preConfiguration['all']

    }

    # if (updated) <
    # else (then not updated) <
    if (preConfiguration != postConfiguration):

        jsonDump(

            pData = postConfiguration,
            pFile = f'{gDirectory}/{gConfigurationPath}'

        )
        return True

    else: return False

    # >


# main <
if (__name__ == '__main__'):

    bot.run(jsonLoad(pFile = f'{gDirectory}/{gConfigurationPath}')['token'])


    # x1 = Process(target = bot.run(jsonLoad(pFile = f'{gDirectory}/configuration.json')['token']))
    # x2 = Process(target = application.run_server(port = 8159))

    # x1.start()
    # x2.start()

# >