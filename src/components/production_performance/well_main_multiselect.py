import pandas as pd
from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.loader import ProductionDataSchema
from .. import ids
    
def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_wells: list[str] = data[ProductionDataSchema.WELLBORE].tolist()
    unique_wells: list[str] = sorted(set(all_wells))
    
    # @app.callback(
    #     Output(ids.WELL_MAIN_MULTISELECT, "value"),
    #     [
    #         Input(ids.YEAR_MAIN_MULTISELECT, "value"),
    #         Input(ids.MONTH_MAIN_MULTISELECT, "value"),
    #         Input(ids.SELECT_ALL_WELLS_MAIN_BUTTON, "n_clicks")
    #     ],
    # )
    
    # def select_all_wells(years: list[str], months: list[str], _: int) -> list[str]:
    #     filtered_data = production_data.query("YEARPRD in @years and MONTHPRD in @months")
    #     return sorted(set(filtered_data[ProductionDataSchema.WELLBORE].tolist()))
    
    return html.Div(
        children=[
            html.H5("Well:"),
            dmc.MultiSelect(
                className="main-multiselect",
                id=ids.WELL_MAIN_MULTISELECT,
                data=[{"label": well, "value": well} for well in unique_wells],
                value=unique_wells,
                placeholder="Select Wells",
                searchable=True,
                clearable=True,
                nothingFound="No options available",
                style={'width':450,'marginTop':'5px'}
            ),
            dmc.Button(
                'Select All',
                className="main-multiselect-button",
                id=ids.SELECT_ALL_WELLS_MAIN_BUTTON,
                variant="outline",
                color="dark",
                radius="5px",
                leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
                style={'height':30, 'marginTop':'15px'},
                n_clicks=0,
            ),
            
        ]
    )