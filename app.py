import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import dash_table
import pitch_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

frame = pitch_data.compileTeamPitch()
df = pd.melt(frame, id_vars='Team')
available_indicators = df['variable'].unique()

app.layout = html.Div([


    html.Div([
        html.H1(children='MLB Dash'),
        html.Div(children='''
        An exploratory data analysis hub for team pitching during the 2020 MLB season.
    '''),
    ], style={'backgroundColor': 'rgb(102, 102, 255', 'padding': '10px 5px'}),

    #  dropdown configurations
    html.Div([

        # dropdown configuration for x-variable
        html.Div([
            dcc.Dropdown(
                id='x_axis_var',
                options=[{'label': i, 'value': i}
                         for i in available_indicators],
                value='ERA'
            )
        ],
            style={'width': '49%', 'display': 'inline-block'}),

        # dropdown configuration for y-variable
        html.Div([
            dcc.Dropdown(
                id='y_axis_var',
                options=[{'label': i, 'value': i}
                         for i in available_indicators],
                value='Win %'
            )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(102, 102, 255)',
        'padding': '10px 5px'
    }),

    # two-dimensional scatter plot configuration
    html.Div([
        dcc.Graph(
            id='two-dim-scatter'
        )
    ]),

    # histogram configurations
    html.Div([
        html.Div([
            dcc.Graph(
                id='x-var-hist',
            )
        ], style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(
                id='y-var-hist'
            )

        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})

    ])

])


@app.callback(
    dash.dependencies.Output('two-dim-scatter', 'figure'),
    [dash.dependencies.Input('x_axis_var', 'value'),
     dash.dependencies.Input('y_axis_var', 'value')])
def update_graph(x_axis_varname, y_axis_varname):
    dff = df
    fig = px.scatter(x=dff[dff['variable'] == x_axis_varname]['value'],
                     y=dff[dff['variable'] == y_axis_varname]['value'], 
                     hover_name=dff[dff['variable'] == y_axis_varname]['Team'],
                     color=dff[dff['variable'] == y_axis_varname]['Team'])

    fig.update_layout(
        margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=x_axis_varname)
    fig.update_yaxes(title=y_axis_varname)

    return fig


@app.callback(
    dash.dependencies.Output('x-var-hist', 'figure'),
    [dash.dependencies.Input('x_axis_var', 'value')])
def update_x_histogram(x_axis_varname):
    dff = df
    fig = px.histogram(x=dff[dff['variable'] == x_axis_varname]['value'], nbins=30, marginal='box',
                       labels={'x': x_axis_varname, 'y': 'Count'})

    return fig


@app.callback(
    dash.dependencies.Output('y-var-hist', 'figure'),
    [dash.dependencies.Input('y_axis_var', 'value')])
def update_y_histogram(y_axis_varname):
    dff = df
    fig = px.histogram(x=dff[dff['variable'] == y_axis_varname]['value'], nbins=30, marginal='box',
                       labels={'x': y_axis_varname, 'y': 'Count'})

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
