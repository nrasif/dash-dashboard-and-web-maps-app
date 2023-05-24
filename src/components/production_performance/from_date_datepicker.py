import pandas as pd

from datetime import datetime, date

from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.loader_data import ProductionDataSchema
from .. import ids

def render(app: Dash, production_data: pd.DataFrame) -> html.Div:
    
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
                        
            html.H5("From:"),
            
            dmc.DatePicker(
                id=ids.FROM_DATE_DATEPICKER,
                value=production_data[ProductionDataSchema.DATE].min(),
                style={'marginTop':'5px', "width": 175},
            ),

            dmc.Checkbox(
                id=ids.ALL_DATES_BEFORE_CHECKBOX,
                label='Select the earliest date',
                value=production_data[ProductionDataSchema.DATE].min(),
                color='dark',
                style={'marginTop':'5px'}
            ),
            
            dmc.Button(
                'Select All',
                className="main-multiselect-button",
                id=ids.ALL_DATES_MAIN_BUTTON,
                variant="outline",
                color="dark",
                radius="5px",
                leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
                style={'height':30, 'marginTop':'10px'},
                n_clicks=0,
            ),
            
        ]
    )