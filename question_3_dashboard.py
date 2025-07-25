import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px


df = pd.read_csv(r"C:\Users\User\Desktop\Data_visualization\question_3\clean_african_healthcare_data.csv")


numeric_cols = df.select_dtypes(include='number').columns.tolist()
# Remove irrelevant columns if needed
if 'Year' in numeric_cols:  # if dataset has years, ignore
    numeric_cols.remove('Year')

app = Dash(__name__)

app.layout = html.Div([
    html.H1("🌍 African Healthcare Access & Disease Burden Dashboard", style={'textAlign':'center'}),
    
    html.Div([
        html.Label("Select Health Indicator (X-axis):"),
        dcc.Dropdown(
            id='x_indicator',
            options=[{'label': col, 'value': col} for col in numeric_cols],
            value=numeric_cols[0]
        ),
    ], style={'width':'45%', 'display':'inline-block', 'padding':'10px'}),

    html.Div([
        html.Label("Select Health Indicator (Y-axis):"),
        dcc.Dropdown(
            id='y_indicator',
            options=[{'label': col, 'value': col} for col in numeric_cols],
            value=numeric_cols[1]
        ),
    ], style={'width':'45%', 'display':'inline-block', 'padding':'10px'}),

    dcc.Graph(id='indicator_scatter'),

    html.H2("Country-level Indicator Distribution", style={'textAlign':'center', 'marginTop':'40px'}),
    html.Div([
        html.Label("Select Indicator for Distribution:"),
        dcc.Dropdown(
            id='hist_indicator',
            options=[{'label': col, 'value': col} for col in numeric_cols],
            value=numeric_cols[0]
        ),
    ], style={'width':'50%', 'margin':'auto'}),
    dcc.Graph(id='indicator_hist')
])

@app.callback(
    Output('indicator_scatter', 'figure'),
    Input('x_indicator', 'value'),
    Input('y_indicator', 'value')
)
def update_scatter(x_col, y_col):
    fig = px.scatter(df, x=x_col, y=y_col, text='Country', color=y_col,
                     hover_name='Country', size=y_col, size_max=20,
                     title=f"{y_col} vs {x_col} by Country")
    fig.update_traces(textposition='top center')
    fig.update_layout(margin=dict(l=40, r=40, t=60, b=40))
    return fig

@app.callback(
    Output('indicator_hist', 'figure'),
    Input('hist_indicator', 'value')
)
def update_hist(indicator):
    fig = px.histogram(df, x=indicator, nbins=20, title=f"Distribution of {indicator}")
    fig.update_layout(margin=dict(l=40, r=40, t=60, b=40))
    return fig

if __name__ == '__main__':
    app.run(debug=True)
