import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import base64

st.set_page_config(page_title="Tesla Dashboard", layout="wide")

