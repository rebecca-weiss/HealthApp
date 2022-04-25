import dash
# import dash_core_components as dcc
from dash import dcc
# import dash_html_components as html
from dash import html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv("data/workouts.csv")

fig = px.scatter(
    df,
    x="duration",
    y="totalEnergyBurned",
    size="totalEnergyBurned",
    color="workoutActivityType",
    hover_name="workoutActivityType",
    # log_x=True,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id="workout_total", figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)