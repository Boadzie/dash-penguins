from dash import dcc, Output, Input, State, html


import plotly.express as px
import dash

import plotly.io as pio
from siuba.data import penguins
import plotly.graph_objects as go

# pio.templates.default = "ggplot2"
# pio.templates["myname"] = go.layout.Template(layout=go.Layout(colorway=["#082255", "#061E44", "#061E44"]))
pio.templates.default = "plotly_white"


import pandas as pd

# import polars as pl
external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(__name__, requests_pathname_prefix="/", external_scripts=external_script, title="Dan Demo")


def generate_table(dataframe, max_rows=11):
    return html.Table(
        [
            html.Thead(
                html.Tr(
                    [html.Th([col], className="px-2 border-2 w-full") for col in dataframe.columns],
                    className="p-2 divide divide-x-2 border-2 bg-[#061E44] text-lg  text-white w-full text-left",
                )
            ),
            html.Tbody(
                [
                    html.Tr(
                        [
                            html.Td([dataframe.iloc[i][col]], className="p-2 border-2 w-full")
                            for col in dataframe.columns
                        ],
                        className="p-2 w-full border-2 text-sm divide-x-2",
                    )
                    for i in range(min(len(dataframe), max_rows))
                ]
            ),
        ],
        className="lg:table-auto table-fixed border-2 col-span-3 bg-[#082255] p-2 w-full",
    )


# df = df.to_pandas()

# df = pl.read_csv("https://j.mp/iriscsv")
# print(df.filter(pl.col("sepal_length") > 5)
# .groupby("species", maintain_order=True)
# .agg(pl.all().sum())
# )
print(penguins.shape)
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig = px.histogram(penguins, x="species", color="species")
fig.update_layout(title_text="Penguins", showlegend=False)
fig.update_layout(
    margin=dict(l=0, r=0, t=30, b=0),
    plot_bgcolor="rgba(0, 0, 0, 0)",
    font_color="#ffffff",
    paper_bgcolor="rgba(0, 0, 0, 0)",
)
fig.update_xaxes(mirror=True, showline=False, ticks="outside", linecolor="black", gridcolor="#007ace")
fig.update_yaxes(mirror=True, showline=False, ticks="outside", linecolor="black", gridcolor="#007ace")


# chart 1
fig1 = px.scatter(penguins, x="bill_length_mm", y="bill_depth_mm", color="species", size=penguins.body_mass_g.index)
fig1.update_layout(title_text="Penguins", showlegend=False)
fig1.update_layout(
    margin=dict(l=0, r=0, t=30, b=0),
    plot_bgcolor="rgba(0, 0, 0, 0)",
    font_color="#ffffff",
    paper_bgcolor="rgba(0, 0, 0, 0)",
)
fig1.update_xaxes(mirror=True, showline=False, ticks="outside", linecolor="black", gridcolor="#007ace")
fig1.update_yaxes(mirror=True, showline=False, ticks="outside", linecolor="black", gridcolor="#007ace")
# fig3 = ggplot(penguins, aes(x="species")) + geom_bar()

fig2 = px.box(penguins, x="sex", y="bill_length_mm", color="species")
fig2.update_layout(
    title_text="Penguins",
    showlegend=False,
    plot_bgcolor="rgba(0, 0, 0, 0)",
    font_color="#ffffff",
    paper_bgcolor="rgba(0, 0, 0, 0)",
)
fig2.update_xaxes(mirror=True, showline=False, ticks="outside", linecolor="black", gridcolor="#007ace")
fig2.update_yaxes(mirror=True, showline=False, ticks="outside", linecolor="black", gridcolor="#007ace")


app.layout = html.Div(
    children=[
        dcc.Interval(id="refresh", interval=200),
        html.H1(
            children=[
                "Hello Dash!!",
                html.H2(
                    "Dash: A web application framework for your data.",
                    className="text-sm capitalize text-white font-semibold",
                ),
            ],
            className="text-3xl uppercase my-2 text-white shadow-lg p-2",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.P(id="out", className="text-lg font-bold text-slate-500 capitalize"),
                        dcc.Input(
                            id="text",
                            required=True,
                            type="text",
                            placeholder="Name...",
                            className=" ring-2 text-slate-400 rounded-sm py-1 w-full px-4",
                        ),
                        dcc.Input(
                            id="number",
                            type="number",
                            required=True,
                            placeholder="Age...",
                            className="ring-2 text-slate-400  rounded-sm py-1 w-full px-4",
                        ),
                        dcc.Input(
                            id="sex",
                            type="text",
                            required=True,
                            placeholder="Sex...",
                            className="text-slate-400  ring-2 rounded-sm py-1 w-full px-4",
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id="columns",
                                options=[{"label": x, "value": x} for x in sorted(penguins.columns)],
                                className="text-slate-400  w-full",
                            ),
                            className="w-full",
                        ),
                        html.Button(
                            "Send",
                            id="button",
                            className="bg-red-800 hover:bg-red-600 text-white rounded-sm focus:outline-none px-4 py-2",
                        ),
                    ],
                    className="bg-[#082255] text-white p-4  flex flex-col gap-4 items-start justify-evenly",
                ),
                html.Div(
                    [dcc.Graph(id="example-graph", figure=fig)],
                    className="bg-[#082255] text-white  rounded-sm p-3 w-full",
                ),
                html.Div(
                    [dcc.Graph(id="example-graph1", figure=fig1)],
                    className="bg-[#082255] lg:col-span-2 text-white  rounded-sm p-2 w-full",
                ),
                html.Div(
                    [dcc.Graph(id="graphy", figure=fig2)],
                    className="bg-[#082255] text-white shadow-lg rounded-sm p-2 w-full h-auto",
                ),
                generate_table(penguins),
            ],
            className="grid grid-cols-1 lg:grid-cols-4 gap-4",
        ),
        html.H1(children="＠ 2023 Cool Dash", className="text-md uppercase my-2 bg-slate-800 text-white shadow-lg p-2"),
    ],
    className="container bg-[#061E44] text-white mx-auto px-4 ",
)


# callbacks
@app.callback(
    Output(component_id="out", component_property="children"),
    State("text", "value"),
    State("number", "value"),
    State("sex", "value"),
    Input("button", "n_clicks"),
    # Input("button-state", "value"),
)
def update_output_div(text_input, number_input, sex_input, n_clicks):
    return (
        f"Hello {text_input}, you are {number_input} years old and a {sex_input}!"
        if n_clicks and text_input != None and number_input != None and sex_input != None
        else ""
    )


if __name__ == "__main__":
    app.run_server()
