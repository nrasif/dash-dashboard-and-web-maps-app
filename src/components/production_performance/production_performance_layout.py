from datetime import datetime, date

import pandas as pd
from dash import Dash, html
import dash_mantine_components as dmc

from src.components.production_performance import (
    from_date_datepicker,
    to_date_datepicker,
    well_main_multiselect
)

def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(

            html.Div(
                # className=cms.PPD_MAIN_WRAPPER,
                children=[
                    
                    html.Div(
                        # className=cms.PPD_LEFT_GRID_MAIN,
                        children=[
                            
                            html.Div(
                                # className=cms.PPD_MULTISELECT,
                                children=[
                                    
                                    html.Div(
                                        # className=cms.PPD_MULTISELECT,
                                        children=[
                                            well_main_multiselect.render(app, data),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ),
                                    
                                    html.Div(
                                        # className=cms.PPD_MULTISELECT,
                                        children=[
                                            from_date_datepicker.render(app, data),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ),
                                    html.Div(
                                        # className=cms.PPD_MULTISELECT,
                                        children=[
                                            to_date_datepicker.render(app, data),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ), 
                                
                                ],
                                style={'display': 'grid', 'grid-template-columns': '1.5fr 0.75fr 0.75fr', 'grid-template-rows': 'auto'},
                                
                            ),
                            
                            # html.Div(
                            #     # className=cms.PPD_MULTISELECT,
                            #     children=[
                                    
                            #     ],
                            #     style={'padding': 5, 'flex': 1},
                            # ),
                            
                            html.Div(
                                # className=cms.PPD_MULTISELECT,
                                children=[
                                    html.H1("TESSSSSSSSSSSSSSTTtttttttttttttttttttttttttttttttttttttT")
                                ],
                                style={'padding': 5, 'flex': 1},
                            ),
                            
                        ],
                        style={},
                        
                    ),
                    
                    html.Div(
                        # className=cms.PPD_RIGHT_GRID_MAIN,
                        children=[
                            
                            
                            
                            html.H1(
                                "Testosstesorrrrrr",
                                # className='text-center'
                            ),
                            
                            
                        ],
                        style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1},
                    ),
                ],
                style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'grid-template-rows': 'auto'},
            ), 
        
    )