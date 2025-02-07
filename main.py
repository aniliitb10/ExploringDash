import dash
from dash import dcc, html, Input, Output
from dash.dash_table import DataTable
import plotly.express as px

# Centralized data
TABLE_DATA = [
    {"Name": "Alice", "Age": 30, "City": "New York", "Occupation": "Engineer", "Salary": 90000},
    {"Name": "Bob", "Age": 25, "City": "San Francisco", "Occupation": "Designer", "Salary": 75000},
    {"Name": "Charlie", "Age": 35, "City": "Los Angeles", "Occupation": "Manager", "Salary": 105000},
    {"Name": "David", "Age": 28, "City": "Chicago", "Occupation": "Analyst", "Salary": 68000},
]

PIE_DATA = {
    "City": ["New York", "San Francisco", "Los Angeles", "Chicago"],
    "Count": [1, 1, 1, 1],
}

# Available columns
ALL_COLUMNS = ["Name", "Age", "City", "Occupation", "Salary"]

# Styling for the table
TABLE_STYLES = {
    "table_container": {
        "overflowX": "auto",
        "border": "1px solid #e7e7e7",
        "borderRadius": "8px",
        "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.1)",
    },
    "cell": {
        "textAlign": "left",
        "padding": "12px",
        "fontSize": "14px",
        "fontFamily": "Arial, sans-serif",
        "borderBottom": "1px solid #e7e7e7",
    },
    "header": {
        "backgroundColor": "#f4f4f4",
        "color": "#212529",
        "fontWeight": "600",
        "textAlign": "left",
        "borderBottom": "2px solid #007bff",
    },
}

PIE_CHART = px.pie(PIE_DATA, values="Count", names="City", title="City Distribution")

# Dash app initialization
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(
    [
        html.H1("Dashboard with Resettable Columns", style={"textAlign": "center"}),

        # Main layout: Pie chart and table
        html.Div(
            [
                # Pie chart (30%)
                html.Div(
                    dcc.Graph(id="pie-chart", figure=PIE_CHART),
                    style={"flex": "0.3", "marginRight": "20px"},
                ),

                # Data table with column control
                html.Div(
                    [
                        # Dropdown for column selection
                        html.Div(
                            [
                                html.Label(
                                    "Select Columns:",
                                    style={
                                        "fontWeight": "bold",
                                        "marginBottom": "10px",
                                    },
                                ),
                                dcc.Dropdown(
                                    id="column-selector",
                                    options=[
                                        {"label": col, "value": col}
                                        for col in ALL_COLUMNS
                                    ],
                                    value=ALL_COLUMNS,  # Default: all columns selected
                                    multi=True,
                                    placeholder="Select columns to display",
                                    style={"width": "100%"},
                                ),
                            ],
                            style={
                                "marginBottom": "10px",
                                "padding": "10px",
                                "border": "1px solid #e7e7e7",
                                "borderRadius": "8px",
                                "backgroundColor": "#f9f9f9",
                                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                            },
                        ),

                        # Reset Columns Button
                        html.Div(
                            [
                                html.Button(
                                    "Reset Columns",
                                    id="reset-button",
                                    n_clicks=0,
                                    style={
                                        "padding": "10px 20px",
                                        "backgroundColor": "#007bff",
                                        "border": "none",
                                        "color": "white",
                                        "fontWeight": "bold",
                                        "borderRadius": "5px",
                                        "cursor": "pointer",
                                        "boxShadow": "0 2px 5px rgba(0, 0, 0, 0.2)",
                                    },
                                )
                            ],
                            style={"marginBottom": "20px"},
                        ),

                        # DataTable
                        DataTable(
                            id="table",
                            columns=[
                                {"name": col, "id": col}
                                for col in ALL_COLUMNS
                            ],
                            data=TABLE_DATA,
                            style_table=TABLE_STYLES["table_container"],
                            style_as_list_view=True,  # Clean layout
                            style_cell=TABLE_STYLES["cell"],
                            style_header=TABLE_STYLES["header"],
                            hidden_columns=[],  # Dynamically updated
                            filter_action="native",
                            page_size=10,
                            # Disable any user interaction in the table
                            editable=False,  # Turn off table editing
                            row_deletable=False,  # Disable row deletion
                            css=[{"selector": ".dash-spreadsheet-menu", "rule": "display: none;"}],
                            # Remove default menu
                        ),
                    ],
                    style={"flex": "0.7"},
                ),
            ],
            style={
                "display": "flex",
                "flexDirection": "row",
                "alignItems": "flex-start",
                "gap": "20px",
            },
        ),
    ]
)


# Callback to update visible columns based on dropdown or reset button
@app.callback(
    Output("table", "hidden_columns"),
    Output("column-selector", "value"),
    Input("column-selector", "value"),
    Input("reset-button", "n_clicks"),
)
def update_hidden_columns(selected_columns, reset_clicks):
    """Hides columns in the table based on dropdown selection."""
    ctx = dash.callback_context

    # If Reset Columns button is clicked
    if ctx.triggered and ctx.triggered[0]["prop_id"] == "reset-button.n_clicks":
        return [], ALL_COLUMNS

    # Calculate hidden columns (columns not selected)
    hidden_columns = [col for col in ALL_COLUMNS if col not in selected_columns]
    return hidden_columns, selected_columns


if __name__ == "__main__":
    app.run_server(debug=True)