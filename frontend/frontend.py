# import <
from dash import html, dcc
from lxRbckl import jsonLoad, jsonDump
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from backend.resource import gDirectory, application, gConfigurationPath

# >


# global <
gForegroundColor = '#111111'
gBackgroundColor = '#f8f0e3'

# >


def layout(pConfiguration: dict):
    '''  '''

    return dbc.Container(

        fluid = True,
        style = dict(
        
            padding = '5vh',
            minHeight = '100vh',
            backgroundColor = gBackgroundColor

        ),
        children = dbc.Row(
        
            justify = 'center',
            children = [

                dbc.Row(
        
                    justify = 'center',
                    style = dict(
        
                        maxWidth = '40vh',
                        padding = '10px 0px 10px 0px'

                    ),
                    children = [

                        # header <
                        # body a <
                        # body b <
                        # submit <
                        dbc.Row(
        
                            justify = 'center',
                            children = [

                                # alert <
                                dbc.Alert(
        
                                    id = 'alertId',
                                    is_open = False,
                                    duration = 3500,
                                    dismissable = True,
                                    children = 'configuration.json was updated.'

                                ),

                                # >

                                # title <
                                # spacer <
                                html.H1(
        
                                    children = 'Project ASBC',
                                    style = dict(
        
                                        padding = 0,
                                        wordSpacing = 8,
                                        margin = '-10px 0px 0px 0px'

                                    )

                                ),
                                html.Hr(style = dict(margin = '5px 0px 5px 0px'))

                                # >

                            ]

                        ),
                        dbc.Row(
        
                            children = [

                                # watch <
                                # (duration, threshold, confidence) <
                                dcc.Dropdown(
        
                                    multi = True,
                                    id = 'watchId',
                                    value = pConfiguration['watch'],
                                    options = {i : i for i in pConfiguration['all']},
                                    style = dict(
        
                                        margin = '0px 0px 0px 0px',
                                        padding = '0px 0px 2px 0px'

                                    )

                                ),
                                dbc.InputGroup(
        
                                    size = 'sm',
                                    style = dict(
        
                                        margin = '3px 0px 0px 0px',
                                        padding = '0px 0px 0px 0px'

                                    ),
                                    children = [

                                        dbc.Input(
        
                                            value = pConfiguration[i],
                                            id = f'{i}Id',
                                            placeholder = i.title()
                                        
                                        )

                                    for i in ['duration', 'threshold', 'confidence']]

                                ),

                                # >

                                # description <
                                # spacer <
                                dbc.FormText(
        
                                    children = 'Surveillance configurations.',
                                    style = dict(
        
                                        padding = 0,
                                        fontSize = 10,
                                        margin = '2px 0px 5px 0px'
                                        
                                    )

                                ),
                                html.Hr(style = dict(margin = '-2px 0px 5px 0px'))

                                # > 

                            ]
                                        
                        ),
                        dbc.Row(

                            children = [

                                # (online, token) <
                                # (channel, sleep) <
                                dbc.InputGroup(
        
                                    style = dict(
        
                                        margin = '0px 0px 5px 0px',
                                        padding = '0px 0px 0px 0px'
                                        
                                    ),
                                    children = [

                                        dbc.Switch(
        
                                            id = 'onlineId',
                                            value = pConfiguration['online'],
                                            style = dict(margin = '3px 0px 0px 0px')

                                        ),
                                        *[

                                            dbc.Input(
        
                                                size = 'sm',
                                                id = f'{i}Id',
                                                style = dict(width = j),
                                                placeholder = i.title(),
                                                value = pConfiguration[i]

                                            )

                                        for i, j in [
                                            
                                            ('channel', '10vh'), 
                                            ('sleep', '1vh')
                                            
                                        ]]

                                        # >

                                    ]

                                ),
                                dbc.Input(
        
                                    size =  'sm',
                                    id = 'tokenId',
                                    placeholder = 'Discord Token',
                                    value = pConfiguration['token']

                                ),

                                # >

                                # description <
                                # spacer <
                                dbc.FormText(
        
                                    children = 'Discord configurations.',
                                    style = dict(
        
                                        padding = 0,
                                        fontSize = 10,
                                        margin = '2px 0px -2px 0px'

                                    )

                                ),
                                html.Hr(style = dict(margin = '5px 0px 5px 0px'))

                                # >

                            ]

                        ),
                        dbc.Row(
        
                            children = dbc.Button(
        
                                size = 'sm',
                                id = 'submitId',
                                children = 'Submit'
                                
                            )

                        ),

                        # >

                        # tooltip <
                        *[

                            dbc.Tooltip(
        
                                target = f'{i}Id',
                                placement = 'top',
                                children = i.title(),
                                delay = {'show' : 500, 'hide' : 0}

                            )

                        for i in list(pConfiguration.keys())[:-1]]

                        # >

                    ]

                )

                # >

            ]

        )

    )


@application.callback(
        
    Output('layoutId', 'children'),
    Input('layoutId', 'children')

)
def layoutCallback(layoutChildren: list):
    '''  '''

    configuration = jsonLoad(pFile = f'{gDirectory}/{gConfigurationPath}')
    return layout(pConfiguration = configuration)


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


def run(): application.run_server(port = 8088)