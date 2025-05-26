📊 TSLA Dashboard – วิเคราะห์ราคาหุ้น Tesla 6 เดือนย้อนหลัง
โปรเจกต์นี้เป็น Web Dashboard ที่พัฒนาด้วย Python + Streamlit เพื่อใช้ในการ วิเคราะห์แนวโน้มราคาหุ้นของ Tesla (TSLA80) โดยอ้างอิงข้อมูลย้อนหลัง 6 เดือน และนำเสนอในรูปแบบอินเทอร์เฟซที่ใช้งานง่าย พร้อมกราฟเส้นแนวโน้มราคาปิด

✅ ฟีเจอร์ที่แสดงผลใน Dashboard
แนวโน้มราคาปิด (Trend Chart)

แสดงกราฟราคาปิดย้อนหลัง 6 เดือน

มีการสร้างเส้นแนวโน้มด้วย Linear Regression เพื่อดูภาพรวม

เพิ่มภาพ GIF ตกแต่งด้านข้างหัวข้อแบบมีลูกเล่น

สรุปข้อมูล (Summary)

แสดงข้อมูลราคาสูงสุด ต่ำสุด เฉลี่ย ฯลฯ

วิเคราะห์สถิติพื้นฐานของราคาปิด

แสดงวันที่ราคาปิดสูงที่สุด

(มีตัวเลือกการคำนวณความสัมพันธ์กับ SET Index หากข้อมูลรองรับ)

ข้อมูลดิบ (Raw Data)

แสดงตารางข้อมูลเต็มของหุ้นทั้งหมดเรียงจากวันล่าสุด

🧱 เทคโนโลยีที่ใช้
Python (Pandas, Matplotlib, Scikit-learn)

Streamlit สำหรับสร้าง Web UI

CSS สำหรับปรับธีมให้ดูเป็นแนว Minimal Soft Tone

🔧 ปัญหาที่พบและแนวทางแก้ไข
การแปลงวันที่ไทย → ค.ศ. ต้องใช้ Mapping เดือนและแปลงปีพ.ศ.

การฝังภาพ GIF ให้แสดงผลแบบเคลื่อนไหว จำเป็นต้องใช้การเข้ารหัส base64 แทนลิงก์ทั่วไป

การแสดงผลใน Streamlit ต้องจัดลำดับ st.set_page_config ให้อยู่บนสุดเสมอ มิฉะนั้นจะ Error

ลิ้งนำเสนอ: https://www.canva.com/design/DAGoWM3VoDo/dAA3psZ6md_HcuvefC9JjQ/edit?utm_content=DAGoWM3VoDo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

📦 วิธีการใช้งาน
bash
คัดลอก
แก้ไข
streamlit run tesla80.py
🧑‍💻 จัดทำโดย
นาย รัชพล ลองซุม

รหัสนักศึกษา 2311310862

วิชา: ENG-494	Extra Curriculum Activity in Engineering 4
Python 3.11.9

