from dash import Dash, html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

from src.components import ids, cns

from ..data.source import DataSource


from .production_performance import (
    summary_card,
    oil_rate_line_chart,
    forecasting_oil_rate_line_chart,
    well_stats_subplots,
    water_injection_subplots,
    water_cut_gor_line_subplots,
    oil_vs_water_subplots,
    dp_choke_size_vs_avg_dp_subplots,
    
    well_main_multiselect,
    from_date_datepicker,
    to_date_datepicker
)

from .web_maps import (
    filter_maps,
    restart_button,
    leaflet_maps
)

from.web_maps.data_color_map import colormap

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className=cns.WEB_CONTAINER,
        children=[
            # div navbar (header(1))
            html.Div(
                className = cns.NAVBAR,
                children = [
                    html.H1('Navigation Bar')
                ]
            ),
            
            # div left-side map (content(2))
            html.Div(className = cns.LEFT_SIDE_MAP,
                     children=[
                        html.Div(
                        className = cns.TITLE_SUMMARY_LAYOUT,
                        children = [
                            html.H1('Dummy Block', className=cns.TITLE_BLOCK),
                            html.H4('Summary'),
                            dmc.Spoiler(
                                className = cns.SUMMARY_BLOCK,
                                showLabel = 'Show More',
                                hideLabel = 'Hide',
                                maxHeight = 50,
                                style = {'marginBottom':35},
                                children = [
                                    dmc.Text(
                                        '''
                                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi luctus elit at eros accumsan iaculis. Nulla facilisi. Morbi vitae venenatis ante. Nulla dui tellus, euismod at malesuada ac, luctus quis orci. Nullam in eros mollis, vulputate neque ut, vulputate dolor. In sed ultrices mauris. Ut vitae dolor augue. Ut ac purus eu felis scelerisque facilisis. Donec consectetur odio orci, non volutpat eros suscipit vestibulum. Quisque a fermentum massa. Sed ac nibh nibh.
                                        '''
                                    )]
                                )]
                        ),
                    html.Div(
                        className=cns.MAP_ALL_FILTER,
                        children=[
                            # MAP COLOR FILTER
                            
                            dmc.Accordion(value='color map filter',
                                        radius=10,
                                        variant='contained',
                                        style={'marginBottom':10},
                                        children=[
                                            dmc.AccordionItem(
                                                [
                                                    dmc.AccordionControl('Map Settings', icon=DashIconify(icon='ic:twotone-map', width=25)),
                                                    dmc.AccordionPanel(
                                                        html.Div(children=[
                                                            # MAP COLOR FILTER
                                                            
                                                            html.H5('Layout Map'),
                                                            dmc.RadioGroup(
                                                                [dmc.Radio(i, value=k, color=c) for i, k, c in colormap()],
                                                                id=ids.MAP_COLOR,
                                                                value='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                                                                orientation='vertical',
                                                                spacing='xs'
                                                                )
                                                            ])
                                                        )
                                                ], value='color map filter')
                                            ]),

                            dmc.Accordion(value='block filter',
                                        radius=10,
                                        variant='contained',
                                        children=[
                                            dmc.AccordionItem(
                                                [
                                                    dmc.AccordionControl('Block Filter', icon=DashIconify(icon='mdi:surface-area',width=20)),
                                                    dmc.AccordionPanel(
                                                        html.Div(children=[
                                                            filter_maps.render(app, source),
                                                            restart_button.render(app, source)
                                                            ])
                                                        )
                                                ], value='block filter')
                                            ])
                            ]
                        )
                    ]),
            
            # div map-map (content(3))
            html.Div(
                className=cns.MAP_LEAFLET,
                children=[
                    leaflet_maps.render(app, source)
                    ]
                ),
            
            # div ppd-production filter (content{4})
            html.Div(
                className=cns.PPD_PRODUCTION_FILTER,
                children=[
                    
                    dmc.Accordion(value='production filter',
                                radius=10,
                                variant='contained',
                                className=cns.PPD_ACCORDION_FILTER,
                                children=[
                                    dmc.AccordionItem(
                                        [
                                            dmc.AccordionControl('Well Production Filter', icon=DashIconify(icon='octicon:graph-16', width=25)),
                                            dmc.AccordionPanel(
                                                html.Div(children=[
                                                    well_main_multiselect.render(app, source),
                                                    from_date_datepicker.render(app, source),
                                                    to_date_datepicker.render(app, source),
                                                    ])
                                                )
                                        ], value='production filter')
                                ])
                ]),
            
            # div ppd-main-graph (content(5))
            html.Div(
                className=cns.PPD_MAIN_GRAPHS,
                children=[
                    
                    summary_card.render(app, source),
                            
                    html.H2("Oil Production Rate", className=cns.PPD_H2, style={"marginTop":30, "text-align": "center"}),
                    oil_rate_line_chart.render(app, source),
                    
                    html.H2("Well Stats", className=cns.PPD_H2, style={"text-align": "center"}),
                    well_stats_subplots.render(app, source),
                    
                    html.H2("Daily Water Injection", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"}),
                    water_injection_subplots.render(app, source),
                    
                    html.H2("Water Cut Daily and Gas Oil Ratio (GOR)", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"}),
                    water_cut_gor_line_subplots.render(app, source),
                    
                    html.H2("Oil and Water Total Rate on Pressure Comparison", className=cns.PPD_H2, style={"marginTop":15, "text-align": "center"}),
                    oil_vs_water_subplots.render(app, source),
                    
                    dp_choke_size_vs_avg_dp_subplots.render(app, source),
                ]),

            # Div Footer (Footer(6))
            html.Div(
                className=cns.FOOTER_WEB,
                children=[
                    html.H1('Footer')
                ])
            ])


            # html.Div(
            #     className = cns.MAP_ALL,
            #     children=[
            #         web_maps_layout.create_layout_map(app, source)
            #     ]),
            # html.Div(
            #     className=cns.PPD_PRODUCTION_ALL,
            #     children=[
            #         production_performance_layout.create_layout(app, source)
            #     ]),
            