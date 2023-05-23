import pandas as pd
from dash import Dash, html
import dash_bootstrap_components as dbc

from src.components import (
    year_main_multiselect,
    month_main_multiselect,
    well_main_multiselect
)

from src.components import cms

def create_layout(app: Dash, production_data: pd.DataFrame) -> html.Div:
    return html.Div(
        className=cms.PRODUCTION_PERFORMANCE_DASHBOARD_LAYOUT,
        children=[
            html.Div(
                className=cms.PPD_HEADER,
                children=[
                    html.H1(
                        app.title,
                        className=cms.PPD_TITLE,
                        style={}
                    ),
                ],
                style={},
            ),
            
            # html.Br(),
            
            html.Div(
                className=cms.PPD_MAIN_WRAPPER,
                children=[
                    html.Div(
                        className=cms.PPD_LEFT_GRID_MAIN,
                        children=[
                            
                            html.Div(
                                className=cms.PPD_MULTISELECT,
                                children=[
                                    year_main_multiselect.render(app, production_data),
                                ],
                                style={'padding': 10, 'flex': 1},
                            ),
                            html.Div(
                                className=cms.PPD_MULTISELECT,
                                children=[
                                    month_main_multiselect.render(app, production_data),
                                ],
                                style={'padding': 10, 'flex': 1},
                            ),
                            html.Div(
                                className=cms.PPD_MULTISELECT,
                                children=[
                                    well_main_multiselect.render(app, production_data),
                                ],
                                style={'padding': 10, 'flex': 1},
                            ),
                            
                        ],
                        style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1},
                    ),
                    
                    html.Div(
                        className=cms.PPD_RIGHT_GRID_MAIN,
                        children=[
                            html.H1(
                                "Test",
                                className='text-center'
                            ),
                        ],
                        style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1},
                    ),
                ],
                style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'grid-template-rows': 'auto'},
            ),  
        ], 
        
    )
