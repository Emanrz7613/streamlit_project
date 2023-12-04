import streamlit as st
import pandas as pd
import altair as alt 

df = pd.read_csv("data.csv")

st.dataframe(df)

st.line_chart(data=df, x="BOROUGH", y="NUMBER OF PERSONS KILLED")

