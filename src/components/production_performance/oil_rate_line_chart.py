from dash import Dash, html, dcc
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify

# import plotly.graph_objects as go
import plotly.express as px

from ...data.loader import ProductionDataSchema
from ...data.source import DataSource
from .. import ids


# def render(app: Dash, source: DataSource) -> html.Div:
#     @app.callback(
#         Output(ids.OIL_RATE_LINE_CHART, "children", allow_duplicate=True),
#         [
#             Input(ids.FROM_DATE_DATEPICKER,  "value"),
#             Input(ids.TO_DATE_DATEPICKER,    "value"),
#             Input(ids.WELL_MAIN_MULTISELECT, "value"),
#         ],  prevent_inital_call=True
#     )
    
#     def update_bar_chart(from_date: str, to_date: str, wells: str) -> html.Div:
#         filtered_source = source.filter(from_date, to_date, wells)
# #     #     if not filtered_source.row_count:
# #     #         return html.Div(i18n.t("general.no_data"), id=ids.BAR_CHART)

#         fig = px.line(
#                 filtered_source,
#                 x=filtered_source.all_dates,
#                 y=filtered_source.moving_average,
#                 color=filtered_source.all_wells,
#                 labels={
#                     "value":"14-days Moving Average Oil (m3)",
#                     "DATEPRD": "Year",
#                     "WELL_BORE_CODE": "Wells"
#                 }
#             )

#         return html.Div(dcc.Graph(figure=fig), id=ids.OIL_RATE_LINE_CHART)

#     return html.Div(id=ids.OIL_RATE_LINE_CHART)