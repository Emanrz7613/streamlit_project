import streamlit as st
import pandas as pd

data = pd.read_csv("data.csv")

print(data.head(5))

data_clean = data.dropna(subset=['BOROUGH'])

print(data_clean.head(5))

