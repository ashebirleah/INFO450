
import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv('Advertising_f.csv')
st.title('Advertising Effectiveness Leah')

st.sidebar.header('Filters')
x_var=st.selectbox("X axis", ['TV', 'radio', 'newspaper'])

#show scatterplot
fig=px.scatter(
    df, 
    x=x_var, 
    y='sales', 
    labels={'TV': 'TV Ad Spend', 'radio': 'Radio Ad Spend'}
)
st.plotly_chart(fig)

#show the barplot
sales_per_city=df.groupby('City')['sales'].sum().reset_index()
sales_per_city
fig=px.bar(sales_per_city, x='City', y='sales', title='data is fun')
st.plotly_chart(fig)


#show the dataframe
st.dataframe(df)
