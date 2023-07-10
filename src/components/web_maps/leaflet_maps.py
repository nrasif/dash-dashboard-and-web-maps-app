from dash import Dash, html
import dash_leaflet as dl
import dash_mantine_components as dmc
from dash.dependencies import Input, Output
from dash_iconify import DashIconify
from dash_extensions.javascript import arrow_function, assign


from ...data.source import DataSource
from .. import ids, cns

import json
from statistics import mean

def render(app: Dash, source: DataSource) -> html.Div:
    
    @app.callback(
        Output(ids.MAP_LAYOUT,'children'),
        [
            Input(ids.BLOCK_NAME_MULTISELECT,'value'),
            Input(ids.MAP_COLOR,'value')
        ], prevent_initial_call=True
    )
    
    def plot_map(block_name_multi_value: list[str], map_color_chosen: str) -> html.Div:
        edited_blocks = source.filter_block(name_block=block_name_multi_value)
        series_geometry = edited_blocks.to_dataframe_geopandas_temp['geometry']
        
        layer_blocks = dl.GeoJSON(
                        data=json.loads(series_geometry.to_json()),
                        hoverStyle=arrow_function(dict(weight=5, fillColor='#45b6fe', fillOpacity=0.5, color='black', dashArray='')),
                        options=dict(style={
                                            'color':'black',
                                            'weight':3,
                                            'dashArray':'30 10',
                                            'dashOffset':'5',
                                            'opacity':1,
                                            'fillColor':'#3a9bdc'
                                            }))
        bounds = series_geometry.total_bounds
        x = mean([bounds[0], bounds[2]])
        y = mean([bounds[1], bounds[3]])
        location = (y, x)
        
        if series_geometry.empty:
            return dl.Map(children=[
                                    dl.TileLayer(url=map_color_chosen, attribution = '&copy; <a href="http://www.waviv.com/">Waviv Technologies</a> '),
                                    dl.GestureHandling(),
                                    dl.MeasureControl(position="topleft", primaryLengthUnit="kilometers", primaryAreaUnit="hectares",
                                                    activeColor="#C29200", completedColor="#972158")],
                                    center=[5.3, 96.3],
                                    zoom=11,
                                    style={
                                        # 'z-index':'0',
                                        'width': '100%',
                                        'height': '1400px',
                                        'marginLeft':'0px',
                                        # 'float':'right'
                                    })
        
        return dl.Map(children=[dl.GeoJSON(layer_blocks),
                                dl.TileLayer(url=map_color_chosen, attribution = '&copy; <a href="http://www.waviv.com/">Waviv Technologies</a> '),
                                dl.GestureHandling(),
                                dl.MeasureControl(position="topleft", primaryLengthUnit="kilometers", primaryAreaUnit="hectares",
                                                activeColor="#C29200", completedColor="#972158")],
                                center=[y, x],
                                zoom=11,
                                style={
                                    # 'z-index':'0',
                                    'width': '100%',
                                    'height': '1400px',
                                    'marginLeft':'0px',
                                    # 'float':'right'
                                })
    
    return html.Div(id=ids.MAP_LAYOUT)