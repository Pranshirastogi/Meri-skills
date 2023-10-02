import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px 
import streamlit as st
st.cache_data()
st.title('Diabetes App')
st.markdown('''This app predicts the probability of a person having diabetes based on their health parameters and age.
            The dataset used here is the Pima Indians Diabetes Database. It was originally collected by the National Institute of Diabetes and Digestive and Kidney Diseases.
            The objective of the dataset is to diagnostically predict whether or not a patient has diabetes, based on certain diagnostic measurements included in the dataset.
            The app will show visual representation of data and also predict the probability of a person having diabetes with other factors.''')
df = pd.read_csv('diabetes.csv')
st.subheader('Data Information:')
if st.checkbox('Show raw data'):
    st.write(df)
st.write(df.shape)
if st.sidebar.checkbox('Show columns'):
    st.write(df.columns)
if st.sidebar.checkbox('Show data types'):
    st.write(df.dtypes)
if st.sidebar.checkbox('Show Univariate Analysis'):
    fig1 = px.pie(df,'Outcome', title='Diabetes Outcome')
    st.plotly_chart(fig1)
    st.subheader('Data Analysis:')
    st.markdown('''65.1% of the patients in the dataset are non-diabetic and 34.9% are diabetic.''')
    fig2 = px.histogram(df, x='Age', title='Age distribution')
    st.plotly_chart(fig2)
    st.subheader('Data Analysis:')
    st.markdown('''The age of the patients in the dataset ranges from 21 to 81 years. The average age of the patients is 33.24 years.''')
    fig3 = px.box(df,'BloodPressure', title='Blood Pressure Distribution')
    st.plotly_chart(fig3)
    st.subheader('Data Analysis:') 
    st.markdown('''The blood pressure of the patients in the dataset ranges from 0 to 122 mm Hg. The average blood pressure of the patients is 72.4 mm Hg.''')
    fig4 =px.violin(df, 'Glucose', title='Glucose Distribution')
    st.plotly_chart(fig4)
    st.subheader('Data Analysis:')
    st.markdown('''The glucose level of the patients in the dataset ranges from 0 to 199 mg/dL. The average glucose level of the patients is 120.89 mg/dL.''')
    fig5 = px.histogram(df, x='BMI', title='BMI Distribution')
    st.plotly_chart(fig5)
    st.subheader('Data Analysis:')
    st.markdown('''The BMI of the patients in the dataset ranges from 0 to 67.1. The average BMI of the patients is 31.99.''')
if st.sidebar.checkbox('Show Bivariate Analysis'):
    fig10 = px.scatter(df, x='Age', y='Glucose', color='Outcome', title='Age vs Glucose')
    st.plotly_chart(fig10)
    st.subheader('Data Analysis:')
    st.markdown('''The scatter plot shows that the glucose level of the patients increases with age. The glucose level of the diabetic patients is higher than that of the non-diabetic patients.''')
    fig11 = px.box(df, x='Age', y='BloodPressure', color='Outcome', title='Age vs Blood Pressure')
    st.plotly_chart(fig11)
    st.subheader('Data Analysis:')  
    st.markdown('''The box plot shows that the blood pressure of the patients increases with age. The blood pressure of the diabetic patients is higher than that of the non-diabetic patients.''')
    fig12 = px.treemap(df, path=['Age','BloodPressure'], values='DiabetesPedigreeFunction', title='Diabetes by Age and Blood Pressure')
    st.plotly_chart(fig12)
    st.subheader('Data Analysis:')
    st.markdown('''The treemap shows that the number of diabetic patients increases with age and blood pressure.''')
    fig13 = px.scatter(df,'Age','Insulin', color='Outcome', title='Outcome by Age and Insulin')
    st.plotly_chart(fig13)
    st.subheader('Data Analysis:')
    st.markdown('''The scatter plot shows that the insulin level of the patients increases with age. The insulin level of the diabetic patients is higher than that of the non-diabetic patients.''')
    fig14 = px.area(df,x='Age',y='BMI', color='Outcome', title='Outcome by Age and BMI')
    st.plotly_chart(fig14)
    st.subheader('Data Analysis:')
    st.markdown('''The area plot shows that the BMI of the patients increases with age. The BMI of the diabetic patients is higher than that of the non-diabetic patients.''')