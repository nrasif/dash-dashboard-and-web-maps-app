from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify

# from ...data.loader import ProductionDataSchema
from ...data.source import DataSource 

from .. import ids

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.FROM_DATE_DATEPICKER, "value", allow_duplicate=True),
        [
            Input(ids.ALL_DATES_BEFORE_CHECKBOX, "checked")
        ], prevent_inital_call=True
    )
    
    def select_earliest_date(checked: bool) -> str:
        if checked == True:
            return source.earliest_date
        if checked == False:
            pass
    
    @app.callback(
        Output(ids.ALL_DATES_BEFORE_CHECKBOX, "checked"),
        Output(ids.ALL_DATES_AFTER_CHECKBOX, "checked"),
        Input(ids.ALL_DATES_MAIN_BUTTON, "n_clicks"),
        State(ids.ALL_DATES_BEFORE_CHECKBOX, "checked"),
        State(ids.ALL_DATES_AFTER_CHECKBOX, "checked")

    )
    
    def select_earliest_and_latest_date(n_clicks: int, checked1: bool, checked2: bool):
        if n_clicks:
            return True, True
        return checked1, checked2
    
    return html.Div(
        children=[
                        
            html.H5("From:"),
            
            dmc.DatePicker(
                id=ids.FROM_DATE_DATEPICKER,
                className="",
                value=source.earliest_date,
                dropdownPosition='flip',
                initialLevel='year',
                style={'marginTop':'5px', "width": 175},
            ),

            dmc.Checkbox(
                id=ids.ALL_DATES_BEFORE_CHECKBOX,
                className="",
                label='Select the earliest date',
                checked=True,
                value=source.earliest_date,
                color='dark',
                style={'marginTop':'5px'}
            ),
            
            dmc.Button(
                'Select All',
                id=ids.ALL_DATES_MAIN_BUTTON,
                className="",
                variant="outline",
                color="dark",
                radius="5px",
                leftIcon=DashIconify(icon='material-symbols:restart-alt', width=15),
                style={'height':30, 'marginTop':'10px'},
                n_clicks=0,
            ),
            
        ]
    )