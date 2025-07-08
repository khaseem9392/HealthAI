import pandas as pd
import plotly.express as px

def generate_demo_chart():
    df = pd.DataFrame({
        "Health Metric": ["BP", "Heart Rate", "Glucose"],
        "Value": [120, 80, 95]
    })
    fig = px.bar(df, x="Health Metric", y="Value", title=" Vitals Overview")
    return fig