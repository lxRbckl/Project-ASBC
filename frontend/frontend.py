# import <
from dash import html, dcc
import dash_bootstrap_components as dbc

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
                                    style = dict(margin = 0, padding = 0),
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