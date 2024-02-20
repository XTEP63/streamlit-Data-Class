import streamlit as st
import pandas as pd 

st.title("Esto e un titulo")
st.header("Esto es un header")
st.markdown("*Esto es italica*")

df = pd.read_csv("train.csv")
st.dataframe(df)