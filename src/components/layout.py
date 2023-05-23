import pandas as pd
from dash import Dash, html

from src.components import (
    year_main_multiselect,
    month_main_multiselect,
    well_main_multiselect
)

def create_layout(app: Dash, production_data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Br(),
            html.Div(
                className="main-multiselect-container",
                children=[
                    year_main_multiselect.render(app, production_data),
                    html.Br(),
                    month_main_multiselect.render(app, production_data),
                    html.Br(),
                    well_main_multiselect.render(app, production_data),
                ],
            ),
        ]
    )
