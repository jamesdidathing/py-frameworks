from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

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
    )
    ]

)


if __name__ == '__main__':
    app.run_server(debug=True)