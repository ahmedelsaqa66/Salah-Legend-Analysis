import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# 1. Load Data
try:
    df_total = pd.read_csv('salah_total_stats.csv')
    df_pl = pd.read_csv('salah_premier_league.csv')
    df_cl = pd.read_csv('salah_champions_league.csv')
except Exception as e:
    print(f"❌ Error: Run maker.py first! Details: {e}")

app = dash.Dash(__name__)

# 2. UI Layout
app.layout = html.Div(style={'backgroundColor': '#111', 'color': '#fff', 'padding': '20px'}, children=[
    html.H1("👑 Mohamed Salah: Career Performance Dashboard", 
            style={'textAlign': 'center', 'color': '#e31b23', 'marginBottom': '30px'}),
    
    # Tournament Selection Tabs
    dcc.Tabs(id="tabs-selection", value='tab-total', children=[
        dcc.Tab(label='Overall Stats', value='tab-total', 
                style={'backgroundColor': '#222', 'color': '#fff'}, 
                selected_style={'backgroundColor': '#e31b23', 'color': '#fff'}),
        dcc.Tab(label='Premier League', value='tab-pl', 
                style={'backgroundColor': '#222', 'color': '#fff'}, 
                selected_style={'backgroundColor': '#3d195d', 'color': '#fff'}),
        dcc.Tab(label='Champions League', value='tab-cl', 
                style={'backgroundColor': '#222', 'color': '#fff'}, 
                selected_style={'backgroundColor': '#003399', 'color': '#fff'}),
    ]),

    html.Div(id='tabs-content')
])

# 3. Reactive Logic (Callback)
@app.callback(
    Output('tabs-content', 'children'),
    Input('tabs-selection', 'value')
)
def render_content(tab):
    if tab == 'tab-total':
        df = df_total
        main_color = '#e31b23'
        title_suffix = "Overall Career"
    elif tab == 'tab-pl':
        df = df_pl
        main_color = '#3d195d'
        title_suffix = "Premier League"
    else:
        df = df_cl
        main_color = '#003399'
        title_suffix = "Champions League"

    # Line Chart for Goals & Assists
    fig = px.line(df, x='Season', y=['Goals', 'Assists'], 
                  title=f'📈 Performance Trend: {title_suffix}',
                  markers=True, template='plotly_dark',
                  color_discrete_map={'Goals': main_color, 'Assists': '#ffcc00'})

    return html.Div([
        # KPI Cards
        html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'marginTop': '20px'}, children=[
            html.Div([html.P("Total Goals"), html.H2(df['Goals'].sum())], 
                     style={'textAlign': 'center', 'background': '#222', 'padding': '15px', 'borderRadius': '10px', 'width': '30%'}),
            html.Div([html.P("Total Assists"), html.H2(df['Assists'].sum())], 
                     style={'textAlign': 'center', 'background': '#222', 'padding': '15px', 'borderRadius': '10px', 'width': '30%'}),
            html.Div([html.P("Matches Played"), html.H2(df['Matches'].sum())], 
                     style={'textAlign': 'center', 'background': '#222', 'padding': '15px', 'borderRadius': '10px', 'width': '30%'}),
        ]),
        
        dcc.Graph(figure=fig),
        
        # Detailed Table
        html.H3("Detailed Season Breakdown", style={'textAlign': 'center', 'marginTop': '20px'}),
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in df.columns],
            style_header={'backgroundColor': '#333', 'color': 'white', 'fontWeight': 'bold'},
            style_cell={'backgroundColor': '#111', 'color': 'white', 'textAlign': 'center', 'padding': '10px'},
            style_table={'overflowX': 'auto'}
        )
    ])

if __name__ == '__main__':
    app.run(debug=True, port=8050)