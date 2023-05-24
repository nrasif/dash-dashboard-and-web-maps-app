from datetime import datetime, date

import pandas as pd
from dash import Dash, html
import dash_mantine_components as dmc

from src.components.production_performance import (
    year_main_multiselect,
    month_main_multiselect,
    well_main_multiselect
)

def create_layout(app: Dash, production_data: pd.DataFrame) -> html.Div:
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
                                    well_main_multiselect.render(app, production_data),
                                ],
                                style={'padding': 10, 'flex': 1},
                            ),
                            
                            html.Div(
                                # className="ppd-select-parameter-container",
                                children=[
                                    
                                    html.Div(
                                        # className=cms.PPD_MULTISELECT,
                                        children=[
                                            year_main_multiselect.render(app, production_data),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ),
                                    html.Div(
                                        # className=cms.PPD_MULTISELECT,
                                        children=[
                                            month_main_multiselect.render(app, production_data),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ),
                                    
                                    # html.Div(
                                    #     className=cms.PPD_MULTISELECT,
                                    #     children=[
                                    #         year_main_multiselect.render(app, production_data),
                                    #     ],
                                    #     style={'padding': 10, 'flex': 1},
                                    # ),
                                    # html.Div(
                                    #     className=cms.PPD_MULTISELECT,
                                    #     children=[
                                    #         month_main_multiselect.render(app, production_data),
                                    #     ],
                                    #     style={'padding': 10, 'flex': 1},
                                    # ),                                    
                                ],
                                style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1},
                            )
                        ],
                        
                    ),
                    
                    html.Div(
                        # className=cms.PPD_RIGHT_GRID_MAIN,
                        children=[
                            # html.H1(
                            #     "Test",
                            #     # className='text-center'
                            # ),
                            
                            dmc.DatePicker(
                                id="date-picker",
                                # value=datetime.now().date(),
                                style={"width": 200},
                            )
                            
                        ],
                        style={'display': 'flex', 'flex-direction': 'row', 'padding': 10, 'flex': 1},
                    ),
                ],
                style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'grid-template-rows': 'auto'},
            ), 
        
    )