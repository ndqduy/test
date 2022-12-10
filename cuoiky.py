import pandas as pd
import streamlit as st
from cau4 import cau4
from cau5 import cau5
from cau3 import cau3
from cau6 import cau6
from cau8_new import cau8
import mysql.connector
def main():
    st.header('Quản lý điểm thi')
    contact_options = ['Danh sách điểm thi tổng hợp','Danh sách học sinh khá giỏi', 'Danh sách học sinh chưa đạt', 'Danh sách thủ khoa','Tra cứu kết quả thi']
    contact_selected = st.selectbox("Chọn chức năng", options = contact_options)
    if contact_selected == "Danh sách học sinh khá giỏi":
        cau4()
    elif contact_selected == "Danh sách học sinh chưa đạt":
        cau5()
    elif contact_selected == "Danh sách điểm thi tổng hợp":
        cau3()
    elif contact_selected == "Danh sách thủ khoa":
        cau6()
    elif contact_selected == 'Tra cứu kết quả thi':
        sbd = st.text_input('Nhập số báo danh')
        if sbd != '':
            cau8(sbd)
if __name__ == "__main__":
    main()