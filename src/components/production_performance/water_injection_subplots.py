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
        Output(ids.WATER_INJECTION_SUBPLOTS, "children"),
        [
            Input(ids.FROM_DATE_DATEPICKER,  "value"),
            Input(ids.TO_DATE_DATEPICKER,    "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],  prevent_initial_call=True
    )
    
    def update_subplots(from_date: str, to_date: str, wells: list[str]) -> html.Div:
        filtered_pt_wi_well = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_well(ProductionDataSchema.MOVING_AVERAGE_WI)
        pt_wi_well_nonull = filtered_pt_wi_well[filtered_pt_wi_well[ProductionDataSchema.MOVING_AVERAGE_WI] != 0]
        
        filtered_ma_wi_date = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_date_well_ma(ProductionDataSchema.MOVING_AVERAGE_WI)
        pt_ma_wi_date_w1 = filtered_ma_wi_date[filtered_ma_wi_date[ProductionDataSchema.WELLBORE] == "Well-N2"]
        pt_ma_wi_date_w2 = filtered_ma_wi_date[filtered_ma_wi_date[ProductionDataSchema.WELLBORE] == "Well-W2"]
        
        # Initialize figure with subplots
        figure = make_subplots(
                    rows=1, cols=2,
                    column_widths=[0.25, 0.75],
                    row_heights=[0.3],
                    specs=[
                        [{"type": "pie"}, {"type": "scatter"}],
                    ]
                )

        # pie chart for MA of Water Injection

        figure.add_trace(
            go.Pie(
                name="Cum Water Injection (m3) by Well",
                title="Ratio of Daily Water Injection (Sm3) by Well",
                text=pt_wi_well_nonull[ProductionDataSchema.WELLBORE].to_list(),
                labels=pt_wi_well_nonull[ProductionDataSchema.WELLBORE].to_list(),
                values=pt_wi_well_nonull[ProductionDataSchema.MOVING_AVERAGE_WI].to_list(),
                legendrank=1,
                # legendgroup="a"
                # hole=0.5
                ),
                row=1, col=1,
            )

        # line chart for MA of Well-N2
        figure.add_trace(
            go.Scatter(
                name="BORE_WI_VOL (Sm3) by Time (Well-N2)",
                x=pt_ma_wi_date_w1[ProductionDataSchema.DATE],
                y=pt_ma_wi_date_w1[ProductionDataSchema.MOVING_AVERAGE_WI],
                mode='lines',
                # fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                line={'color': '#ef553b'},
                showlegend=True,
                legendrank=4,
                ),
                row=1, col=2
            )

        # line chart for MA of Well-W2
        figure.add_trace(
            go.Scatter(
                name="BORE_WI_VOL (Sm3) by Time (Well-W2)",
                x=pt_ma_wi_date_w2[ProductionDataSchema.DATE],
                y=pt_ma_wi_date_w2[ProductionDataSchema.MOVING_AVERAGE_WI],
                mode='lines',
                # fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                line={'color': '#636efa'},
                showlegend=True,
                legendrank=3,
                # legendgroup="b"
                ),
                row=1, col=2
            )
        
        # Update the layout to resize the figure and move the editing tools
        figure.update_yaxes(title_text="WI_VOL (Sm3)",
                            title_font_size=12,)
        figure.update_xaxes(title_text="Date")

        figure.update_layout(
            height=300,
            autosize=True,  # Allow the figure to be autosized
            margin=dict(l=10, r=10, t=10, b=10),  # Adjust the margins for the figure
            legend=dict(
                x=0.45,   # Set the x position of the legend (0.5 means centered horizontally)
                y=1.15,   # Set the y position of the legend (1.0 means at the top)
                xanchor='center',  # Anchor point for the x position ('center' for center alignment)
                yanchor='top',     # Anchor point for the y position ('top' for top alignment)
                orientation='h',   # Orientation of the legend ('h' for horizontal)
                bgcolor='rgba(255, 255, 255, 0.5)',  # Background color of the legend (with transparency)
                # bordercolor='rgba(0, 0, 0, 0.5)',     # Border color of the legend (with transparency)
                # borderwidth=1       # Border width of the legend
            ),
        )
        
        
        return html.Div(dcc.Graph(figure=figure), id=ids.WATER_INJECTION_SUBPLOTS, className=cns.PPD_SECOND_CHART_RIGHT_GRID)

    return html.Div(id=ids.WATER_INJECTION_SUBPLOTS, className=cns.PPD_SECOND_CHART_RIGHT_GRID)