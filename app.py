import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train.csv")

st.title(":blue[Titanic-Dataset] :ship:")
st.divider()
st.link_button("Accede al Dataset", "https://www.kaggle.com/competitions/titanic/data?select=train.csv")
st.dataframe(df)
st.header(":green[_Análisis por graficos_] :bar_chart:")
st.markdown("**Histogramas simples de cada columna**")


fig, axes = plt.subplots(6, 2, figsize=(12, 18))
axes = axes.flatten()

for i, column in enumerate(df.columns):
    sns.histplot(data=df, x=column, ax=axes[i], color="skyblue", bins=25)
    axes[i].set_title(column)
    
plt.tight_layout()
st.pyplot(fig)

st.divider()

st.markdown("**Vemos un gran decremento de las personas que sobrevivieron según entre mayores sean, pero al mismo tiempo vemos que la mayoria de muertes son de la gente que esta entre las edades medias**")
df_D = df[df["Survived"] == 0]
df_V = df[df["Survived"] == 1]  

fig_1, ax_1 = plt.subplots()
sns.histplot(data=df_V, x="Age", bins=10, alpha=0.7, color='blue')
sns.histplot(data=df_D, x="Age", bins=10, alpha=0.3, color='red')
plt.title("Age Distribution - Survived(Blue)/Not Survived(Red)")
plt.xlabel("Age")
st.pyplot(fig_1)

st.divider()

st.markdown("**Vemos que la mayoria de los pasajeros no pagraon precios altos**")
fig_2, ax_2 = plt.subplots()
sns.histplot(df["Fare"], bins= 20, kde = True, color= "#23c2b0")
st.pyplot(fig_2)
