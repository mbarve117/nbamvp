# The web scraping and data cleaning has already been done
# You can check that work in the two notebooks titled: data_cleaning and web_scraping
# Only the predictor needs to be run in the streamlit app to increase efficiency and speed of the app
import streamlit as st
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor