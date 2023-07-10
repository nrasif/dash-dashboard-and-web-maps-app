
from dash import Dash, html

from src.components import cns

from ...data.source import DataSource
from src.components.production_performance import (
    
    summary_card,
    oil_rate_line_chart,
    forecasting_oil_rate_line_chart,
    well_stats_subplots,
    water_injection_subplots,
    water_cut_gor_line_subplots,
    oil_vs_water_subplots,
    dp_choke_size_vs_avg_dp_subplots,
    
    well_main_multiselect,
    from_date_datepicker,
    to_date_datepicker
)

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        
            html.Div(
                className=cns.PPD_MAIN_WRAPPER,
                children=[
                    
                    # Content left side PRODUCTION FILTER (Content(4))
                    html.Div(
                        className=cns.PPD_PRODUCTION_FILTER,
                        children=[
                            
                            well_main_multiselect.render(app, source),
                            from_date_datepicker.render(app, source),
                            to_date_datepicker.render(app, source),
                            ]
                        ),
                    
                    
                    # Content Right Side PRODUCTION GRAPH (Content(5))
                    html.Div(
                        className=cns.PPD_MAIN_GRAPHS,
                        children=[
                            
                            summary_card.render(app, source),
                                    
                            html.H2("Oil Production Rate", className=cns.PPD_H2, style={"marginTop":30, "text-align": "center"}),
                            oil_rate_line_chart.render(app, source),
                            
                            html.H2("Well Stats", className=cns.PPD_H2, style={"text-align": "center"}),
                            well_stats_subplots.render(app, source),
                            
                            html.H2("Daily Water Injection", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"}),
                            water_injection_subplots.render(app, source),
                            
                            html.H2("Water Cut Daily and Gas Oil Ratio (GOR)", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"}),
                            water_cut_gor_line_subplots.render(app, source),
                            
                            html.H2("Oil and Water Total Rate on Pressure Comparison", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"}),
                            oil_vs_water_subplots.render(app, source),
                            
                            dp_choke_size_vs_avg_dp_subplots.render(app, source),
                        ],
                        style={},
                    ),
                ],
                style={},
            ), 
        
    )