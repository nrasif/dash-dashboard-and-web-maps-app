from dash import Dash, html

from src.components.web_layout import create_layout
from src.data.loader_data import load_well_production_data

PRODUCTION_DATA_PATH = "./data/csv/aceh_production_data_daily_ed.csv"

def main() -> None:
    
    production_data = load_well_production_data(PRODUCTION_DATA_PATH)
    
    app = Dash(__name__, suppress_callback_exceptions=True, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
    app.title = "Aceh Block Information (Dummy)"
    app.layout = create_layout(app, production_data)
    app.run_server(debug=True, port = 8000)

if __name__ == '__main__':
    main()