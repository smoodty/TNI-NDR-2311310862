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

# === Convert Thai Dates ===
thai_months = {
    "ม.ค.": "01", "ก.พ.": "02", "มี.ค.": "03", "เม.ย.": "04",
    "พ.ค.": "05", "มิ.ย.": "06", "ก.ค.": "07", "ส.ค.": "08",
    "ก.ย.": "09", "ต.ค.": "10", "พ.ย.": "11", "ธ.ค.": "12"
}

def convert_thai_date(thai_date_str):
    for th, num in thai_months.items():
        if th in thai_date_str:
            day, month_th, year_th = thai_date_str.replace(",", "").split()
            month = thai_months[month_th]
            year = int(year_th) - 543
            return f"{year}-{month}-{int(day):02d}"
    return None

df = df[~df["วันที่"].isna() & ~df["วันที่"].astype(str).str.contains("วันที่")]
df["วันที่"] = df["วันที่"].apply(convert_thai_date)
df["วันที่"] = pd.to_datetime(df["วันที่"])

# แปลงคอลัมน์ตัวเลข
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()
df_sorted = df.sort_values("วันที่", ascending=False)

# === Filter เฉพาะข้อมูลย้อนหลัง 6 เดือนจากวันล่าสุด
last_date = df_sorted["วันที่"].max()
six_months_ago = last_date - relativedelta(months=6)
df_6mo = df_sorted[df_sorted["วันที่"] >= six_months_ago]

# === Sidebar Menu ===
with st.sidebar:
    st.markdown("### 📌 Tesla 6-Month Dashboard")
    st.markdown("#### เลือกเมนู 👇")
    menu = st.radio("", ("📈 แนวโน้มราคาปิด", "📊 สรุปข้อมูล", "📑 ข้อมูลดิบ"))

