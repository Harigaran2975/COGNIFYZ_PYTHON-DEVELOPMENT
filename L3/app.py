import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Visualization Tool", layout="wide")

st.title("📊 Interactive Data Visualization Tool")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    chart_type = st.selectbox("Choose Chart Type", ["Line", "Bar", "Scatter", "Histogram"])
    columns = df.columns.tolist()

    if chart_type == "Histogram":
        x_axis = st.selectbox("Select Column for Histogram", columns)
        fig = px.histogram(df, x=x_axis)
    else:
        x_axis = st.selectbox("Select X-axis", columns)
        y_axis = st.selectbox("Select Y-axis", columns)
        if chart_type == "Line":
            fig = px.line(df, x=x_axis, y=y_axis)
        elif chart_type == "Bar":
            fig = px.bar(df, x=x_axis, y=y_axis)
        elif chart_type == "Scatter":
            fig = px.scatter(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Please upload a CSV file to get started.")
