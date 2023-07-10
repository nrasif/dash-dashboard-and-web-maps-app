from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify
from src.components.production_performance import (
    from_date_datepicker,
    to_date_datepicker,
    well_main_multiselect
    )
# from ...data.loader import ProductionDataSchema
from ...data.source import DataSource

from .. import ids, cns

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.DRAWER_FILTER, "opened"),
        [
            Input(ids.BUTTON_DRAWER_FILTER, "n_clicks"),
        ],
        prevent_initial_call=True,
    )
    
    def toggle_drawer(n_clicks):
        return True
    
    return html.Div(
        children=[
            dmc.Button("View Dashboard Details", variant="outline", color='dark', id=ids.BUTTON_DRAWER_FILTER, className=cns.PPD_DRAWER_BUTTON,radius='10px', leftIcon=DashIconify(icon='mdi:graph-pie-outline', width=25), 
                        style={
                            "transform": "rotate(270deg)",
                            "position":"absolute",
                            "top": "1000px",
                            "left": "-48px"
                            }),
            dmc.Drawer(
                id=ids.DRAWER_FILTER,
                size='630px',
                lockScroll=False,
                zIndex=999,
                overlayOpacity=0,
                className=cns.PPD_DRAWER_CONTENT,
                transition='slide-right',
                transitionDuration=300,
                
                children=[
                    well_main_multiselect.render(app, source),
                    from_date_datepicker.render(app, source),
                    to_date_datepicker.render(app, source),
                ])
        ]
    )