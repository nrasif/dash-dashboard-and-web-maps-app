import pandas as pd
from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ..data.loader_data import ProductionDataSchema
from . import ids

def render(app: Dash, production_data: pd.DataFrame) -> html.Div:
    all_months: list[str] = production_data[ProductionDataSchema.MONTH].tolist()
    unique_months: list[str] = sorted(set(all_months), key=int)
    
    @app.callback(
        Output(ids.MONTH_MAIN_MULTISELECT, "value"),
        [
            Input(ids.YEAR_MAIN_MULTISELECT, "value"),
            Input(ids.SELECT_ALL_MONTHS_MAIN_BUTTON, "n_clicks")
        ],
    )
    
    def select_all_months(years: list[str], _: int) -> list[str]:
        filtered_data = production_data.query("YEARPRD in @years")
        return sorted(set(filtered_data[ProductionDataSchema.MONTH].tolist()))
    
    return html.Div(
        children=[
            html.H5("Month"),
            dmc.MultiSelect(
                className="main-multiselect",
                id=ids.MONTH_MAIN_MULTISELECT,
                data=[{"label": month, "value": month} for month in unique_months],
                value=unique_months,
                placeholder="Select Months",
                searchable=True,
                clearable=True,
                nothingFound="No options available",
            ),
            dmc.Button(
                'Select All',
                className="main-multiselect-button",
                id=ids.SELECT_ALL_MONTHS_MAIN_BUTTON,
                variant="outline",
                color="dark",
                radius="5px",
                leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
                style={'height':30},
                n_clicks=0,
            ),
            
        ]
    )