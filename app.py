# The web scraping and data cleaning has already been done
# You can check that work in the two notebooks titled: data_cleaning and web_scraping
# The two CSVs referred can be found in the results folder
import streamlit as st
import pandas as pd

# Getting the required data
ridge_results = pd.read_csv("results/ridge_results.csv")
rf_results = pd.read_csv("results/rf_results.csv")
del(ridge_results["Unnamed: 0"])
del(rf_results["Unnamed: 0"])

# Renaming columns for readability
ridge_results["Predicted Ranking"] = ridge_results["Predicted_Rk"]
del(ridge_results["Predicted_Rk"])
ridge_results["Actual Ranking"] = ridge_results["Rk"]
del(ridge_results["Rk"])

rf_results["Predicted Ranking"] = rf_results["Predicted_Rk"]
del(rf_results["Predicted_Rk"])
rf_results["Actual Ranking"] = rf_results["Rk"]
del(rf_results["Rk"])

ridge_accuracy = 0.711
randomforest_accuracy = 0.813

# Actual app layout
st.markdown("<h1 style='text-align: center;'><u><b>NBA MVP Predictor</b></u></h1>", unsafe_allow_html=True)

# Model accuracy and short description
st.subheader("Model Accuracy Comparison")
col1, col2 = st.columns(2)
with col1:
    st.header('Ridge Regression')
    st.write("""
    A linear regression model with L2 regularization. It adds a penalty term to the loss function, 
    reducing the impact of multicollinearity and preventing overfitting. Good for datasets with 
    many features or when features are correlated.
    """)
    st.metric('Accuracy', f'{ridge_accuracy:.2f}')

with col2:
    st.header('Random Forest')
    st.write("""
    An ensemble learning method that constructs multiple decision trees and outputs the average 
    prediction of individual trees. It reduces overfitting, handles non-linear relationships well, 
    and can capture complex interactions between features.
    """)
    st.metric('Accuracy', f'{randomforest_accuracy:.2f}')

# Prepare data for the chosen year
year = st.number_input('Year to predict MVPs(any year from 1996 - 2021)', min_value=1996, max_value=2021, value=1996)
ridge_year_data = ridge_results[ridge_results["Year"]==year][["Player", "Share", "Predicted Ranking", "Actual Ranking"]]
rf_year_data = rf_results[rf_results["Year"]==year][["Player", "Share", "Predicted Ranking", "Actual Ranking"]]
ridge_year_data = ridge_year_data.reset_index(drop=True)
rf_year_data = rf_year_data.reset_index(drop=True)

st.subheader(f"Predicted top 5 candidates for {year}")
col1, col2 = st.columns(2)

with col1:
    st.subheader('Ridge Regressor Predictions')
    st.table(ridge_year_data)

with col2:
    st.subheader('Random Forest Regressor Predictions')
    st.table(rf_year_data)