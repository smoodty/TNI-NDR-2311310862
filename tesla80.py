import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime
from dateutil.relativedelta import relativedelta
import time
import base64

st.set_page_config(page_title="Tesla Dashboard", layout="wide")

# === โหลด CSS ภายนอก ===
with open("custom_minimal_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# === ฟังก์ชันโหลด GIF เป็น base64 ===
def get_base64_of_gif(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
        return f"data:image/gif;base64,{encoded}"
    
    # === Load Excel Data ===
df = pd.read_excel("tesla 007 (1) new.xlsx", sheet_name="tesla", skiprows=1)
df.columns = [
    "วันที่", "ราคาเปิด", "ราคาสูงสุด", "ราคาต่ำสุด", "ราคาเฉลี่ย", "ราคาปิด",
    "เปลี่ยนแปลง", "เปลี่ยนแปลง(%)", "ปริมาณ(พันหุ้น)", "มูลค่า(ล้านบาท)"
]

