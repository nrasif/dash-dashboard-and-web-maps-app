# from dash import Dash, html
# import dash_mantine_components as dmc
# from dash.dependencies import Input, Output
# from dash_iconify import DashIconify

# import plotly.express as px

# from ...data.source import DataSource
# from .. import ids


# def render(app: Dash, source: DataSource) -> html.Div:
#     @app.callback(
#         Output(ids.TOTAL_OIL_PRODUCTION_AMOUNT_CARD, "children", allow_duplicate=True),
#         Output(ids.TOTAL_GAS_PRODUCTION_AMOUNT_CARD, "children", allow_duplicate=True),
#         Output(ids.TOTAL_WATER_INJECTION_AMOUNT_CARD, "children", allow_duplicate=True),
#         Output(ids.ON_STREAM_TIME_AMOUNT_CARD, "children", allow_duplicate=True),
#         [
#             Input(ids.FROM_DATE_DATEPICKER,  "value"),
#             Input(ids.TO_DATE_DATEPICKER,    "value"),
#             Input(ids.WELL_MAIN_MULTISELECT, "value"),
#         ],  prevent_inital_call=True
#     )
    
#     def update_bar_chart(from_date: str, to_date: str, wells: str) -> html.Div:
#         pass
# #     #     years: list[str], months: list[str], categories: list[str]
# #     # ) -> html.Div:
# #     #     filtered_source = source.filter(years, months, categories)
# #     #     if not filtered_source.row_count:
# #     #         return html.Div(i18n.t("general.no_data"), id=ids.BAR_CHART)

# #         fig = px.bar(
# #             filtered_source.create_pivot_table(),
# #             x=ProductionDataSchema.CATEGORY,
# #             y=ProductionDataSchema.AMOUNT,
# #             color="category",
# #             labels={
# #                 "category": "",
# #                 "amount": "",
# #             },
# #         )

#         # return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

#     return html.Div(id=ids.BAR_CHART)