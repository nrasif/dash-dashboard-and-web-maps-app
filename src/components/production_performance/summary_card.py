from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids

def render(app: Dash, source: DataSource) -> html.Div:
    
    # @app.callback(
    #     Output(ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD, "children", allow_duplicate=True),
    #     Output(ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD, "children", allow_duplicate=True),
    #     Output(ids.TOTAL_WATER_INJECTION_AMOUNT_CARD, "children", allow_duplicate=True),
    #     Output(ids.ON_STREAM_TIME_AMOUNT_CARD, "children", allow_duplicate=True),
    #     [
    #         Input(ids.FROM_DATE_DATEPICKER,  "value"),
    #         Input(ids.TO_DATE_DATEPICKER,    "value"),
    #         Input(ids.WELL_MAIN_MULTISELECT, "value"),
    #     ],  prevent_inital_call=True
    # )
    
    # def total_all_category(from_date: str, to_date: str, wells: str) -> float:
    #     if checked == True:
    #         return source.latest_date
    #     if checked == False:
    #         pass
    
    return html.Div(
        
        html.Div(
            children=[
                dmc.CardSection(
                    children=[
                        
                        dmc.SimpleGrid(
                            cols=4,
                            children=[
                                
                                dmc.Group(
                                    children=[
                                        dmc.Card(
                                            children=[
                                                dmc.Title(
                                                    f"Total Oil Production (Sm3)", 
                                                    order=4, 
                                                    align='center',
                                                    color='white',
                                                    # color='red',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    "11.0M",
                                                    id=ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD,
                                                    className="",
                                                    weight=600,
                                                    align='center',
                                                    color='white',
                                                    # color='red',
                                                    style={"fontSize":40}
                                                )
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="sm",
                                            style={'background-color':'#d93d04'},
                                        ),
                                    ],
                                ),
                                
                                dmc.Group(
                                    children=[
                                        dmc.Card(
                                            children=[
                                                dmc.Title(
                                                    f"Total Gas Production (Sm3)",
                                                    order=4, 
                                                    align='center',
                                                    color='white',
                                                    # color='yellow',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    "1,234.5M",
                                                    id=ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD,
                                                    className="",
                                                    weight=600,
                                                    align='center',
                                                    color='white',
                                                    # color='yellow',
                                                    style={"fontSize":40},
                                                )
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="sm",
                                            style={'background-color':'#f2b705'},
                                        ),
                                    ],
                                ),
                                
                                dmc.Group(
                                    children=[
                                        dmc.Card(
                                            children=[
                                                dmc.Title(
                                                    f"Total Water Injection (Sm3)",
                                                    order=4, 
                                                    align='center',
                                                    color='white',
                                                    # color='blue',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    "54.3M",
                                                    id=ids.TOTAL_WATER_INJECTION_AMOUNT_CARD,
                                                    className="",
                                                    weight=600,
                                                    align='center',
                                                    color='white',
                                                    # color='blue',
                                                    style={"fontSize":40},
                                                )
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="sm",
                                            style={'background-color':'#03a6a6'},
                                        ),
                                    ],
                                ),
                                
                                dmc.Group(
                                    children=[
                                        dmc.Card(
                                            children=[
                                                dmc.Title(
                                                    f"On Stream Time (Hours)",
                                                    order=4, 
                                                    align='center',
                                                    color='white',
                                                    # color='black',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    "321K",
                                                    id=ids.ON_STREAM_TIME_AMOUNT_CARD,
                                                    className="",
                                                    weight=600,
                                                    align='center',
                                                    color='white',
                                                    # color='black',
                                                    style={"fontSize":40},
                                                )
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="sm",
                                            style={'background-color':'#012226'},
                                        ),
                                    ],
                                ),
                                
                            ]
                        ),
                    ]
                )
            ]
        ),
        # style={'display': 'grid', 'grid-template-columns': '1fr 1fr 1fr 1fr', 'grid-template-rows': 'auto'},
    
    )