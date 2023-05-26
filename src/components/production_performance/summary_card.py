from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output, State
from dash_iconify import DashIconify

from ...data.loader import ProductionDataSchema
from ...data.source import DataSource
from .. import ids

def render(app: Dash, source: DataSource) -> html.Div:
    
    
    # def update_summary_card(
    #     self
    # ):
    
    #     return
    
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
                                                    color='red',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    "11.0M",
                                                    id=ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD,
                                                    className="",
                                                    weight=600,
                                                    align='center',
                                                    color='red',
                                                    style={"fontSize":40}
                                                )
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="sm",
                                            style={},
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
                                                    color='yellow',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    "1,234.5M",
                                                    id=ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD,
                                                    className="",
                                                    weight=600,
                                                    align='center',
                                                    color='yellow',
                                                    style={"fontSize":40},
                                                )
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="sm",
                                            style={},
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
                                                    color='blue',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    "54.3M",
                                                    id=ids.TOTAL_WATER_INJECTION_AMOUNT_CARD,
                                                    className="",
                                                    weight=600,
                                                    align='center',
                                                    color='blue',
                                                    style={"fontSize":40},
                                                )
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="sm",
                                            style={},
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
                                                    color='black',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    "321K",
                                                    id=ids.ON_STREAM_TIME_AMOUNT_CARD,
                                                    className="",
                                                    weight=600,
                                                    align='center',
                                                    color='black',
                                                    style={"fontSize":40},
                                                )
                                            ],
                                            withBorder=True,
                                            shadow="sm",
                                            radius="sm",
                                            style={},
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