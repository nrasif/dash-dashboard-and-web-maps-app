from dash import Dash, html
import dash_mantine_components as dmc

from src.components import cns

from ..data.source import DataSource
from src.components.production_performance import (
    production_performance_layout
)

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className=cns.PPD_LAYOUT,
        children=[
            html.Div(
                className=cns.PPD_HEADER,
                children=[
                    html.H1(
                        app.title,
                        className=cns.PPD_TITLE,
                        style={}
                    ),
                    dmc.Spoiler(
                        className=cns.PPD_SUMMARY,
                        showLabel='Show more',
                        hideLabel='Hide',
                        maxHeight=25,
                        # style={'marginBottom':35},
                        children=[
                            dmc.Text(
                                '''
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus elit at eros accumsan iaculis. Nulla facilisi. Morbi vitae venenatis ante. Nulla dui tellus, euismod at malesuada ac, luctus quis orci. Nullam in eros mollis, vulputate neque ut, vulputate dolor. In sed ultrices mauris. Ut vitae dolor augue. Ut ac purus eu felis scelerisque facilisis. Donec consectetur odio orci, non volutpat eros suscipit vestibulum. Quisque a fermentum massa. Sed ac nibh nibh.
                                '''
                            )
                        ]
                    ),
                    dmc.Tabs(
                        [
                            dmc.TabsList(
                                [
                                    dmc.Tab("Overview", value="1"),
                                    dmc.Tab("Web Maps", value="2"),
                                    dmc.Tab("Production Performance", value="3"),
                                    dmc.Tab("Geology & Geophysics Analysis", value="4"),
                                ],
                                className=cns.PPD_TABLIST
                            ),
                            dmc.TabsPanel("AAAAAAAA", value="1", className=cns.PPD_TABSPANEL),
                            dmc.TabsPanel("BBBB", value="2",className=cns.PPD_TABSPANEL),
                            dmc.TabsPanel(production_performance_layout.create_layout(app, source), value="3", className=cns.PPD_TABSPANEL),
                            dmc.TabsPanel("DD", value="4", className=cns.PPD_TABSPANEL),
                        ],
                        value="3",
                        className=cns.PPD_TABS
                    )
                ],
                style={"padding": 10},
            ),
        ], 
        style={},
    )
