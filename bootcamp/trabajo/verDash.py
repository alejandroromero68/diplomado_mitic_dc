import dash
from dash import dcc, html
from dash import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input', value='default', type='text'),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    Input('input', 'value')
)
def update_output(value):
    return f'You\'ve entered: {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
