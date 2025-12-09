import streamlit as st
import numpy as np



st.title("Programación en finanzas - Evaluación 2")
#panel lateral
st.sidebar.title("parametros de entrada")

st.sidebar.date_input("fecha inicio", "2023-01-01", key="start")
st.sidebar.date_input("fecha fin", "2025-09-01", key="end")