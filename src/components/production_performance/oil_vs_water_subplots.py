from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# import plotly.express as px

from ...data.loader import ProductionDataSchema
from ...data.source import DataSource
from .. import ids, cns

def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.OIL_VS_WATER_SUBPLOTS, "children", allow_duplicate=True),
        [
            Input(ids.FROM_DATE_DATEPICKER,  "value"),
            Input(ids.TO_DATE_DATEPICKER,    "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],  prevent_inital_call=True
    )
    
    def update_subplots(from_date: str, to_date: str, wells: list[str]) -> html.Div:
        
        filtered_pt_oil_date = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_date(ProductionDataSchema.BORE_OIL_VOL)
        filtered_pt_wtr_date = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_date(ProductionDataSchema.BORE_WAT_VOL)

        # Initialize figure with subplots
        figure = make_subplots(
                    rows=1, cols=1,
                    # column_widths=[0.5, 0.5],
                    # row_heights=[0.5, 0.5],
                    specs=[
                        [{"type": "scatter"}],
                    ]
                )

        # line chart for BORE_OIL_VOL
        figure.add_trace(
            go.Scatter(
                name="Total Oil Volume",
                x=filtered_pt_oil_date[ProductionDataSchema.DATE],
                y=filtered_pt_oil_date[ProductionDataSchema.BORE_OIL_VOL],
                mode='lines',
                # fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                line={'color': '#f2b705'},
                showlegend=True
                ),
                row=1, col=1
            )

        # line chart for BORE_WAT_VOL
        figure.add_trace(
            go.Scatter(
                name="Total Water Volume",
                x=filtered_pt_wtr_date[ProductionDataSchema.DATE],
                y=filtered_pt_wtr_date[ProductionDataSchema.BORE_WAT_VOL],
                mode='lines',
                # fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                line={'color': '#03a6a6'},
                showlegend=True
                ),
                row=1, col=1
            )
        

        # Set theme, margin, and annotation in layout
        figure.update_layout(
            title='Oil and Water Total Rate by Time (Yearly, Monthly, Daily)',
            xaxis_title='Date'
        )
        
        # Set y-axis titles
        figure.update_yaxes(title_text="Total Volume (Sm3)")
        
        # figure.update_layout(
        #     template="plotly_dark",
        #     margin=dict(r=10, t=25, b=40, l=60),
        #     annotations=[
        #         dict(
        #             text="Source: NOAA",
        #             showarrow=False,
        #             xref="paper",
        #             yref="paper",
        #             x=0,
        #             y=0)
        #     ]
        # )

        return html.Div(dcc.Graph(figure=figure), id=ids.OIL_VS_WATER_SUBPLOTS, className=cns.PPD_FOURTH_CHART_RIGHT_GRID)

    return html.Div(id=ids.OIL_VS_WATER_SUBPLOTS, className=cns.PPD_FOURTH_CHART_RIGHT_GRID)