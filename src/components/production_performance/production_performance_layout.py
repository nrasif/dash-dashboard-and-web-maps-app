# from datetime import datetime, date

# import pandas as pd
from dash import Dash, html
# import dash_mantine_components as dmc

from ...data.source import DataSource
from src.components.production_performance import (
    from_date_datepicker,
    to_date_datepicker,
    well_main_multiselect,
    date_rangeslider,
    
    summary_card,
    oil_rate_line_chart,
    well_stats_subplots,
    water_injection_subplots
)

def create_layout(app: Dash, source: DataSource) -> html.Div:
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
                                            well_main_multiselect.render(app, source),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ),
                                    
                                    html.Div(
                                        # className=cms.PPD_MULTISELECT,
                                        children=[
                                            from_date_datepicker.render(app, source),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ),
                                    html.Div(
                                        # className=cms.PPD_MULTISELECT,
                                        children=[
                                            to_date_datepicker.render(app, source),
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
                                    
                                    html.H2("Summary Card",style={"marginTop":15, "text-align": "center"}),
                                    
                                    summary_card.render(app, source),
                                    
                                    html.H2("Oil Production Rate",style={"marginTop":30, "text-align": "center"}),
                                    
                                    oil_rate_line_chart.render(app, source),
                                    
                                    html.H2("TESTSSSSS",style={"marginTop":30, "text-align": "center"}),
                                
                                ],
                                style={'padding': 5, 'flex': 1},
                            ),
                            
                        ],
                        style={},
                        
                    ),
                    
                    html.Div(
                        # className=cms.PPD_RIGHT_GRID_MAIN,
                        children=[
                            # html.H5("Rangeslider:"),
                            # date_rangeslider.render(app, source),
                            
                            html.H2("Well Stats", style={"text-align": "center"},
                                # className='text-center'
                            ),
                            
                            well_stats_subplots.render(app, source),
                            
                            html.H2("Daily Water Injection", style={"marginTop":15, "text-align": "center"},
                                # className='text-center'
                            ),
                            
                            water_injection_subplots.render(app, source),
                            
                            
                        ],
                        style={'padding': 5, 'flex': 1},
                    ),
                ],
                style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'grid-template-rows': 'auto'},
            ), 
        
    )