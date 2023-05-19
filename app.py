from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
df_tab = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode="group")
fig.update_layout(
        plot_bgcolor="#f8f8f8",
        paper_bgcolor="#f8f8f8",
        font={"color": "#555", "size": 12},
        xaxis={"tickfont": {"color": "#555"}},
        yaxis={"tickfont": {"color": "#555"}},
        xaxis_gridcolor="#e9e9e9",
        yaxis_gridcolor="#e9e9e9",
)

app.layout = html.Div(style={"backgroundColor": "#d2d1d1"},
    children=[
    html.H1(className='main-header', children = "My Dash App"),
    dcc.Graph(
        className="graph1",
        id='example-graph',
        figure=fig
    ),
    generate_table(df_tab)
    ]

)


if __name__ == '__main__':
    app.run_server(debug=True)