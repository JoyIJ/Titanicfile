import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import altair as alt


st.title("Titanic table")
def loaddata():
    df= pd.read_excel("titanic.xlsx")
    titanicsub=df[["sex", "age", "embark_town", "alive"]]
    return titanicsub

data = loaddata()

st.dataframe(data)
#Total male and female
st.write("Total Male or Female")
TotalFM = data.groupby("sex")[['sex','embark_town']].agg("count")
st.dataframe(TotalFM)
alive = data[data['alive'] == 'yes']
alivebar = alive.sex.value_counts().plot(kind='barh')
st.pyplot(alivebar.figure)

#Age distribution chart for people alive
st.write("Age distribution")
x = alive["age"]
fig10, ax10 = plt.subplots(figsize=(5,5))
ax10.hist(x, bins=5)
st.pyplot(fig10, ax10)

#Town where most people embarked from
st.write("Town where people embarked from")
df3 = data.groupby("embark_town")[['embark_town','sex']].agg("count")
fig15, ax15 = plt.subplots(figsize=(5,5))
ax15.pie(df3["sex"], labels=df3["embark_town"])
st.pyplot(fig15, ax15)
