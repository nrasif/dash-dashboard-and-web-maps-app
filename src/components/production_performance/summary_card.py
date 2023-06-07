from dash import Dash, html
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

from ...data.source import DataSource
from .. import ids, cns

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD, "children", allow_duplicate=True),
        Output(ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD, "children", allow_duplicate=True),
        Output(ids.TOTAL_WATER_INJECTION_AMOUNT_CARD, "children", allow_duplicate=True),
        Output(ids.ON_STREAM_TIME_AMOUNT_CARD, "children", allow_duplicate=True),
        [
            Input(ids.FROM_DATE_DATEPICKER,  "value"),
            Input(ids.TO_DATE_DATEPICKER,    "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],  prevent_inital_call=True
    )
    
    def calculate_total(from_date: str, to_date: str, wells: list[str]) -> float:
        generate_sum_oil = source.filter(from_date=from_date, to_date=to_date, wells=wells).sum_oil
        generate_sum_gas = source.filter(from_date=from_date, to_date=to_date, wells=wells).sum_gas
        generate_sum_wi = source.filter(from_date=from_date, to_date=to_date, wells=wells).sum_wi
        generate_sum_on_hours = source.filter(from_date=from_date, to_date=to_date, wells=wells).sum_on_hours
        
        abb_sum_oil = source.abbreviate_value(generate_sum_oil)
        abb_sum_gas = source.abbreviate_value(generate_sum_gas)
        abb_sum_wi = source.abbreviate_value(generate_sum_wi)
        abb_sum_on_hours = source.abbreviate_value(generate_sum_on_hours)
        
        return (
            f"{abb_sum_oil}",
            f"{abb_sum_gas}",
            f"{abb_sum_wi}",
            f"{abb_sum_on_hours}"
        )
    
    return html.Div(
        
        html.Div(
            className=cns.PPD_SUMMARY_CARD_LEFT_GRID,
            children=[
                dmc.CardSection(
                    className=cns.PPD_SC_CARD_LEFT_GRID,
                    children=[
                        
                        dmc.SimpleGrid(
                            className=cns.PPD_SC_SIMPLEGRID_LEFT_GRID,
                            cols=4,
                            children=[
                                
                                dmc.Group(
                                    className=cns.PPD_SC_GROUP_LEFT_GRID,
                                    children=[
                                        dmc.Card(
                                            className=cns.PPD_SC_CARD_LEFT_GRID,
                                            children=[
                                                dmc.Title(
                                                    f"Total Oil Production (Sm3)",
                                                    className=cns.PPD_SC_TITLE_LEFT_GRID,
                                                    order=4, 
                                                    align='center',
                                                    color='white',
                                                    # color='red',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    # "11.0M",
                                                    id=ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD,
                                                    className=cns.PPD_SC_TEXT_LEFT_GRID,
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
                                    className=cns.PPD_SC_GROUP_LEFT_GRID,
                                    children=[
                                        dmc.Card(
                                            className=cns.PPD_SC_CARD_LEFT_GRID,
                                            children=[
                                                dmc.Title(
                                                    f"Total Gas Production (Sm3)",
                                                    className=cns.PPD_SC_TITLE_LEFT_GRID,
                                                    order=4, 
                                                    align='center',
                                                    color='white',
                                                    # color='yellow',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    # "1,234.5M",
                                                    id=ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD,
                                                    className=cns.PPD_SC_TEXT_LEFT_GRID,
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
                                    className=cns.PPD_SC_GROUP_LEFT_GRID,
                                    children=[
                                        dmc.Card(
                                            className=cns.PPD_SC_CARD_LEFT_GRID,
                                            children=[
                                                dmc.Title(
                                                    f"Total Water Injection (Sm3)",
                                                    className=cns.PPD_SC_TITLE_LEFT_GRID,
                                                    order=4, 
                                                    align='center',
                                                    color='white',
                                                    # color='blue',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    # "54.3M",
                                                    id=ids.TOTAL_WATER_INJECTION_AMOUNT_CARD,
                                                    className=cns.PPD_SC_TEXT_LEFT_GRID,
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
                                    className=cns.PPD_SC_GROUP_LEFT_GRID,
                                    children=[
                                        dmc.Card(
                                            className=cns.PPD_SC_CARD_LEFT_GRID,
                                            children=[
                                                dmc.Title(
                                                    f"Total On Stream Time (Hours)",
                                                    className=cns.PPD_SC_TITLE_LEFT_GRID,
                                                    order=4, 
                                                    align='center',
                                                    color='white',
                                                    # color='black',
                                                    style={},
                                                ),
                                                dmc.Text(
                                                    # "321K",
                                                    id=ids.ON_STREAM_TIME_AMOUNT_CARD,
                                                    className=cns.PPD_SC_TEXT_LEFT_GRID,
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
                                
                            ],
                            style={"marginTop":20}
                        ),
                    ]
                )
            ]
        ),
        # style={'display': 'grid', 'grid-template-columns': '1fr 1fr 1fr 1fr', 'grid-template-rows': 'auto'},
        className=cns.PPD_SUMMARY_CARD_LEFT_GRID,
    )