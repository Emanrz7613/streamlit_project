import streamlit as st
import pandas as pd

data = pd.readcsv("data.csv")

data.head(5)