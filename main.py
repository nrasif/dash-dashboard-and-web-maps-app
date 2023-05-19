from dash import Dash, html
from src.components.layout import create_layout

def main() -> None:
    app = Dash(__name__, suppress_callback_exceptions=True, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])
    app.title = "Production Performance Dashboard"
    app.layout = create_layout(app)
    app.run_server(debug=True, port = 8000)

if __name__ == '__main__':
    main()