import plotly.graph_objects as go

def plot_data(df, ticker):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name = "Preço"))
    fig.add_trace(go.Scatter(x=df.index, y=df["MA20"], name = "Média 20 dias"))
    fig.add_trace(go.Scatter(x=df.index, y=df["MA50"], name = "Média 50 dias"))
    fig.update_layout(title=f"Análise de {ticker}")
    
    return fig

