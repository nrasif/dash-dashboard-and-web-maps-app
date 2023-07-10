from dash import Dash, html

from src.components.web_layout import create_layout
from src.data.loader import load_well_production_data, load_all_blocks
from src.data.source import DataSource

PRODUCTION_DATA_PATH = "./data/csv/aceh_production_data_daily_ed.csv"
BLOCK_DATA_PATH = './data/geojson/all_blocks_ed.geojson'

def main() -> None:
    
    data = load_well_production_data(PRODUCTION_DATA_PATH)
    data2 = load_all_blocks(BLOCK_DATA_PATH)
    data = DataSource(_data=data, _geodata_blocks=data2)
    
    app = Dash(__name__, prevent_initial_callbacks='initial_duplicate', suppress_callback_exceptions=True, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ])
    app.title = "Aceh Block Information (Dummy)"
    app.layout = create_layout(app, data)
    app.run_server(debug=True, port = 8000)

if __name__ == '__main__':
    main()