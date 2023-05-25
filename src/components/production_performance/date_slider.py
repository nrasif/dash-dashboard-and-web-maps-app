import pandas as pd

from datetime import datetime, date

from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.loader import ProductionDataSchema
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
    #     filtered_data = data.query("YEARPRD in @years")
    #     return sorted(set(filtered_data[ProductionDataSchema.MONTH].tolist()))
    
    return html.Div(
        
        html.H5("Slide the range:"),
        
        dmc.RangeSlider(
            id=ids.DATES_RANGESLIDER,
            
        )
        
        
    )