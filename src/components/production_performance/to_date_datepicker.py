import pandas as pd

from datetime import datetime, date

from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.loader_data import ProductionDataSchema
from .. import ids

def render(app: Dash, production_data: pd.DataFrame) -> html.Div:
    all_date: list[str] = production_data[ProductionDataSchema.DATE].tolist()
    unique_date: list[str] = sorted(set(all_date), key=str)
    
    # @app.callback(
    #     Output(ids.MONTH_MAIN_MULTISELECT, "value"),
    #     [
    #         Input(ids.YEAR_MAIN_MULTISELECT, "value"),
    #         Input(ids.SELECT_ALL_MONTHS_MAIN_BUTTON, "n_clicks")
    #     ],
    # )
    
    # def select_all_months(years: list[str], _: int) -> list[str]:
    #     filtered_data = production_data.query("YEARPRD in @years")
    #     return sorted(set(filtered_data[ProductionDataSchema.MONTH].tolist()))
    
    return html.Div(
        children=[
            html.H5("To:"),
            
            dmc.DatePicker(
                id=ids.TO_DATE_DATEPICKER,
                value=production_data[ProductionDataSchema.DATE].max(),
                style={'marginTop':'5px', "width": 175},
            ),

            dmc.Checkbox(
                id=ids.ALL_DATES_AFTER_CHECKBOX,
                label='Select the latest date',
                value=production_data[ProductionDataSchema.DATE].max(),
                color='dark',
                style={'marginTop':'5px'}
            ),
            
        ]
    )