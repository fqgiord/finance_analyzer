import sys
import os
# Adiciona diretorio src ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import streamlit as st
from src.data_fetch import fetch_data
from src.data_process import process_data
from src.visualize import plot_data
from src.config import RAW_DATA_DIR # type: ignore
from src.utils import create_dirs # type: ignore
from src.logger import logger # type: ignore


st.title("Finance Analyzer")

ticker = st.text_input("Digite o ticker:", "PETR4.SA")

if st.button("Buscar e Analisar"):
    data = fetch_data(ticker)
    df = process_data(ticker)
    st.write(df.head())
    fig = plot_data(df, ticker)
    st.plotly_chart(fig)
