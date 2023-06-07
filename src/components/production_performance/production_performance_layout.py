# from datetime import datetime, date

# import pandas as pd
from dash import Dash, html
# import dash_mantine_components as dmc

from src.components import cns

from ...data.source import DataSource
from src.components.production_performance import (
    from_date_datepicker,
    to_date_datepicker,
    well_main_multiselect,
    date_rangeslider,
    
    summary_card,
    oil_rate_line_chart,
    well_stats_subplots,
    water_injection_subplots,
    water_cut_gor_line_subplots,
    oil_vs_water_subplots,
    dp_choke_size_vs_avg_dp_subplots,
)

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(

            html.Div(
                className=cns.PPD_MAIN_WRAPPER,
                children=[
                    
                    html.Div(
                        className=cns.PPD_MAIN_LEFT_GRID,
                        children=[
                            
                            html.Div(
                                className=cns.PPD_FILTER_WRAPPER,
                                children=[
                                    
                                    html.Div(
                                        className=cns.PPD_FILTER,
                                        children=[
                                            well_main_multiselect.render(app, source),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ),
                                    
                                    html.Div(
                                        className=cns.PPD_FILTER,
                                        children=[
                                            from_date_datepicker.render(app, source),
                                        ],
                                        style={'padding': 5, 'flex': 1},
                                    ),
                                    html.Div(
                                        className=cns.PPD_FILTER,
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
                                className=cns.PPD_CHARTS_LEFT_GRID,
                                children=[
                                    
                                    html.H2("Summary Card", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"}),
                                    
                                    summary_card.render(app, source),
                                    
                                    html.H2("Oil Production Rate", className=cns.PPD_H2, style={"marginTop":30, "text-align": "center"}),
                                    
                                    oil_rate_line_chart.render(app, source),
                                    
                                    html.H2("Forecasting Oil Production Rate", className=cns.PPD_H2, style={"marginTop":30, "text-align": "center"}),
                                
                                ],
                                style={'padding': 5, 'flex': 1},
                            ),
                            
                        ],
                        style={},
                        
                    ),
                    
                    html.Div(
                        className=cns.PPD_MAIN_RIGHT_GRID,
                        children=[
                            # html.H5("Rangeslider:"),
                            # date_rangeslider.render(app, source),
                            
                            html.H2("Well Stats", className=cns.PPD_H2, style={"text-align": "center"},
                                # className='text-center'
                            ),
                            
                            well_stats_subplots.render(app, source),
                            
                            html.H2("Daily Water Injection", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"},
                                # className='text-center'
                            ),
                            
                            water_injection_subplots.render(app, source),
                            
                            html.H2("Water Cut Daily and Gas Oil Ratio (GOR)", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"},
                                # className='text-center'
                            ),
                            water_cut_gor_line_subplots.render(app, source),
                            
                            html.H2("Oil and Water Total Rate on Pressure Comparison", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"},
                                # className='text-center'
                            ),
                            
                            oil_vs_water_subplots.render(app, source),
                            
                            dp_choke_size_vs_avg_dp_subplots.render(app, source),
                            
                            # html.Div(
                            #     children=[
                                    
                            #         html.Div(
                            #             children=[
                            #                 html.H2("Oil and Water Chart", style={"marginTop":15, "text-align": "center"},
                            #                     # className='text-center'
                            #                 ),
                            #                 oil_vs_water_subplots.render(app, source),
                            #             ]
                            #         ),
                                    
                            #         html.Div(
                            #             children=[
                                            
                            #                 html.H2("Pressure Comparison", style={"marginTop":15, "text-align": "center"},
                            #                     # className='text-center'
                            #                 ),
                            #                 dp_choke_size_vs_avg_dp_subplots.render(app, source),
                                            
                            #             ]
                            #         )
                                    
                                    
                            #     ],
                            #     style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'grid-template-rows': 'auto'},
                            # ),
                            
                            
                        ],
                        style={'padding': 5, 'flex': 1},
                    ),
                ],
                style={'display': 'grid', 'grid-template-columns': '1fr 1fr', 'grid-template-rows': 'auto'},
            ), 
        
    )