# main.py
import dash
from dash import dcc, html, Input, Output
from dash.dash_table import DataTable
import plotly.express as px
from styling import (
    TableContainerStyle,
    TableCellStyle,
    TableHeaderStyle,
    DropDownContainerStyle,
    ResetButtonStyle,
    FlexRowStyle,
    PieChartContainerStyle,
    TableWrapperStyle,
)

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

# Use the style classes
table_container_style = TableContainerStyle().generate()
cell_style = TableCellStyle().generate()
header_style = TableHeaderStyle().generate()
dropdown_container_style = DropDownContainerStyle().generate()
reset_button_style = ResetButtonStyle().generate()
flex_row_style = FlexRowStyle().generate()
pie_chart_style = PieChartContainerStyle().generate()
table_wrapper_style = TableWrapperStyle().generate()

PIE_CHART = px.pie(PIE_DATA, values="Count", names="City", title="City Distribution")

# Dash app initialization
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    [
        html.H1("Dashboard with Resettable Columns", style={"textAlign": "center"}),

        html.Div(
            [
                # Pie chart section
                html.Div(dcc.Graph(id="pie-chart", figure=PIE_CHART), style=pie_chart_style),

                # Table and dropdown section
                html.Div(
                    [
                        html.Div(
                            [
                                html.Label("Select Columns:", style={"fontWeight": "bold", "marginBottom": "10px"}),
                                dcc.Dropdown(
                                    id="column-selector",
                                    options=[{"label": col, "value": col} for col in ALL_COLUMNS],
                                    value=ALL_COLUMNS,
                                    multi=True,
                                    placeholder="Select columns to display",
                                    style={"width": "100%"},
                                ),
                            ],
                            style=dropdown_container_style,
                        ),
                        html.Div(
                            [
                                html.Button("Reset Columns", id="reset-button", n_clicks=0, style=reset_button_style),
                            ],
                            style={"marginBottom": "20px"},
                        ),
                        DataTable(
                            id="table",
                            columns=[{"name": col, "id": col} for col in ALL_COLUMNS],
                            data=TABLE_DATA,
                            style_table=table_container_style,
                            style_as_list_view=True,
                            style_cell=cell_style,
                            style_header=header_style,
                            hidden_columns=[],
                            filter_action="native",
                            page_size=10,
                            editable=False,
                            row_deletable=False,
                            css=[{"selector": ".dash-spreadsheet-menu", "rule": "display: none;"}],
                        ),
                    ],
                    style=table_wrapper_style,
                ),
            ],
            style=flex_row_style,
        ),
    ]
)


# Callback
@app.callback(
    [Output("table", "hidden_columns"), Output("column-selector", "value")],
    [Input("column-selector", "value"), Input("reset-button", "n_clicks")],
)
def update_hidden_columns(selected_columns, reset_clicks):
    ctx = dash.callback_context

    if ctx.triggered and ctx.triggered[0]["prop_id"] == "reset-button.n_clicks":
        return [], ALL_COLUMNS

    hidden_columns = [col for col in ALL_COLUMNS if col not in selected_columns]
    return hidden_columns, selected_columns


if __name__ == "__main__":
    app.run_server(debug=True)
