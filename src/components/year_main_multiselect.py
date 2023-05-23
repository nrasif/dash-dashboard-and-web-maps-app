import pandas as pd
from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ..data.loader_data import ProductionDataSchema
from . import ids

def render(app: Dash, production_data: pd.DataFrame) -> html.Div:
    all_years: list[str] = production_data[ProductionDataSchema.YEAR].tolist()
    unique_years: list[str] = sorted(set(all_years), key=int)
    
    @app.callback(
        Output(ids.YEAR_MAIN_MULTISELECT, "value"),
        Input(ids.SELECT_ALL_YEARS_MAIN_BUTTON, "n_clicks")
    )
    
    def select_all_years(_: int) -> list[str]:
        return unique_years
    
    return html.Div(
        children=[
            html.H5("Year"),
            dmc.MultiSelect(
                className="main-multiselect",
                id=ids.YEAR_MAIN_MULTISELECT,
                data=[{"label": year, "value": year} for year in unique_years],
                value=unique_years,
                placeholder="Select Years",
                searchable=True,
                clearable=True,
                nothingFound="No options available",
                style={'marginTop':'10px'}
            ),
            dmc.Button(
                'Select All',
                className="main-multiselect-button",
                id=ids.SELECT_ALL_YEARS_MAIN_BUTTON,
                variant="outline",
                color="dark",
                radius="5px",
                leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
                style={'height':30, 'marginTop':'10px'},
                n_clicks=0,
            ),
            
        ]
    )