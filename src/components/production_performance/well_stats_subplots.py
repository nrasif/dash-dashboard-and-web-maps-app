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
        Output(ids.WELL_STATS_SUBPLOTS, "children", allow_duplicate=True),
        [
            Input(ids.FROM_DATE_DATEPICKER,  "value"),
            Input(ids.TO_DATE_DATEPICKER,    "value"),
            Input(ids.WELL_MAIN_MULTISELECT, "value"),
        ],  prevent_inital_call=True
    )
    
    def update_subplots(from_date: str, to_date: str, wells: list[str]) -> html.Div:
        
        filtered_pt_cum_oil_date = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_date(ProductionDataSchema.BORE_OIL_VOL)
        filtered_pt_cum_oil_well = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_well(ProductionDataSchema.BORE_OIL_VOL)
        
        filtered_pt_cum_gas_date = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_date(ProductionDataSchema.BORE_GAS_VOL)
        filtered_pt_cum_gas_well = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_well(ProductionDataSchema.BORE_GAS_VOL)
        
        filtered_pt_cum_water_date = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_date(ProductionDataSchema.BORE_WAT_VOL, ProductionDataSchema.BORE_WI_VOL)
        filtered_pt_cum_water_well = source.filter(from_date=from_date, to_date=to_date, wells=wells).create_pivot_table_well(ProductionDataSchema.BORE_WAT_VOL, ProductionDataSchema.BORE_WI_VOL)
        
        # Initialize figure with subplots
        figure = make_subplots(
                    rows=3, cols=2,
                    # column_widths=[0.5, 0.5],
                    # row_heights=[0.5, 0.5],
                    specs=[
                        [{"type": "scatter"}, {"type": "pie"}],
                        [{"type": "scatter"}, {"type": "pie"}],
                        [{"type": "scatter"}, {"type": "pie"}],
                    ]
                )
        # Oil line chart and pie
        # Add Line
        figure.add_trace(
            go.Scatter(
                name="Cum Oil (m3) by Time",
                x=filtered_pt_cum_oil_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_oil_date[ProductionDataSchema.BORE_OIL_VOL],
                mode='lines',
                fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                line={'color': '#d93d04'},
                showlegend=False
                ),
                row=1, col=1
            )
        
        # Add Pie
        figure.add_trace(
            go.Pie(
                name="Cum Oil (m3) by Well",
                labels=filtered_pt_cum_oil_well[ProductionDataSchema.WELLBORE].to_list(),
                values=filtered_pt_cum_oil_well[ProductionDataSchema.BORE_OIL_VOL].to_list(),
                hole=0.5
                ),
                row=1, col=2,
            )
        
        # pt_cum_gas_well   
        # pt_cum_gas_date   
        
        # Gas line chart and pie
        # Add Line
        figure.add_trace(
            go.Scatter(
                name="Cum Gas (m3) by Time",
                x=filtered_pt_cum_gas_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_gas_date[ProductionDataSchema.BORE_GAS_VOL],
                mode='lines',
                fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                line={'color': '#f2b705'},
                showlegend=False
                ),
                row=2, col=1
            )
        
        # Add Pie
        figure.add_trace(
            go.Pie(
                name="Cum Gas (m3) by Well",
                labels=filtered_pt_cum_gas_well[ProductionDataSchema.WELLBORE].to_list(),
                values=filtered_pt_cum_gas_well[ProductionDataSchema.BORE_GAS_VOL].to_list(),
                hole=0.5
                ),
                row=2, col=2,
            )
        
        # pt_cum_water_well 
        # pt_cum_water_date 
        
        # Water line chart and pie
        # Add Line
        figure.add_trace(
            go.Scatter(
                name="Cum Water (m3) by Time",
                x=filtered_pt_cum_water_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_water_date[ProductionDataSchema.BORE_WAT_VOL],
                mode='lines',
                fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                line={'color': '#03a6a6'},
                showlegend=False
                ),
                row=3, col=1
            )
        
        figure.add_trace(
            go.Scatter(
                name="Cum Water Injection (m3) by Time",
                x=filtered_pt_cum_water_date[ProductionDataSchema.DATE],
                y=filtered_pt_cum_water_date[ProductionDataSchema.BORE_WI_VOL],
                mode='lines',
                fill='tozeroy',  # Set fill to 'tozeroy' for area below the line
                # fillcolor='rgb(3, 166, 166, 0.7)',
                line={'color': '#03a6a6', 'width':1},
                opacity=0.1,
                showlegend=False
                ),
                row=3, col=1
            )
        
        # Add Pie
        figure.add_trace(
            go.Pie(
                name="Cum Water (m3) by Well",
                labels=filtered_pt_cum_water_well[ProductionDataSchema.WELLBORE].to_list(),
                values=filtered_pt_cum_water_well[ProductionDataSchema.BORE_WAT_VOL].to_list(),
                hole=0.5
                ),
                row=3, col=2,
            )

        return html.Div(dcc.Graph(figure=figure), id=ids.WELL_STATS_SUBPLOTS, className=cns.PPD_FIRST_CHART_RIGHT_GRID)

    return html.Div(id=ids.WELL_STATS_SUBPLOTS, className=cns.PPD_FIRST_CHART_RIGHT_GRID)