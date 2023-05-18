# import <
from os import path
from dash import Dash, html
from dash_bootstrap_components import themes

# >


# global <
gPath = path.realpath(__file__).split('/')[:-1]
gDirectory = '/'.join(gPath[:(len(gPath) - 1)])
gConfigurationPath = 'frontend/configuration.json'
application = Dash(

    name = 'ASBC',
    title = 'ASBC',
    suppress_callback_exceptions = True,
    external_stylesheets = [

        themes.GRID,
        themes.BOOTSTRAP

    ]

)
application.layout = html.Div(id = 'layoutId')

# >