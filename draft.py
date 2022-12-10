#query_cau_4 = ("Select tmp_diem_thi_tong_hop.SBD, tmp_diem_thi_tong_hop.Ho, tmp_diem_thi_tong_hop.Ten, tmp_diem_thi_tong_hop.Phai, tmp_diem_thi_tong_hop.ngay_sinh, Toan, Van, anh_van, tong_diem,  "
#                            +"IF(tong_diem >= 24 AND DTN >= 7,'Gioi', "
#                            +"IF(tong_diem >= 21 AND DTN >= 6, 'Kha', "
#                            +"IF(tong_diem >= 15 AND DTN >= 4, 'Trung binh', 'Chua Dat'))) As Xep_Loai, DTDT from tmp_diem_thi_tong_hop "
#                            +"LEFT JOIN tbl_danh_sach ON tmp_diem_thi_tong_hop.SBD = tbl_danh_sach.SBD "
#                            +"where tmp_diem_thi_tong_hop.SBD = "
#                            + nhap_sbd)
# streamlit_app.py

import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")