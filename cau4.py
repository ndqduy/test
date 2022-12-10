import pandas as pd
import streamlit as st
import mysql.connector
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
query_cau_4 = ("Select tmp_diem_thi_tong_hop.SBD, tmp_diem_thi_tong_hop.Ho, tmp_diem_thi_tong_hop.Ten, tmp_diem_thi_tong_hop.Phai, tmp_diem_thi_tong_hop.ngay_sinh, Toan, Van, anh_van, tong_diem,  "
                            +"IF(tong_diem >= 24 AND DTN >= 7,'Gioi', "
                            +"IF(tong_diem >= 21 AND DTN >= 6, 'Kha', "
                            +"IF(tong_diem >= 15 AND DTN >= 4, 'Trung binh', 'Chua Dat'))) As Xep_Loai, DTDT from tmp_diem_thi_tong_hop "
                            +"LEFT JOIN tbl_danh_sach ON tmp_diem_thi_tong_hop.SBD = tbl_danh_sach.SBD "
                            +"where greatest(Toan, Van, anh_van) = 10 order by xep_loai DESC, tong_diem DESC; ")
def cau4():
    result = run_query(query_cau_4)
    lst_SBD = []
    lst_Ho = []
    lst_Ten = []
    lst_phai = []
    lst_ngaysinh = []
    lst_toan = []
    lst_van = []
    lst_anhvan = []
    lst_tongdiem = []
    lst_xeploai = []
    lst_doituongdt =[]
    for row in result:
        SBD =        row[0]
        Ho =         row[1]
        Ten =        row[2]
        Phai =       row[3]
        ngay_sinh =  row[4]
        Toan =       row[5]
        Van =        row[6]
        anh_van =    row[7]
        tong_diem =  row[8]
        xep_loai =   row[9]
        doi_tuong_dt = row[10]
        # Chuyển số và ngày thành chuỗi
        f_toan = '%.1f' %Toan 
        f_van = '%.1f' %Van 
        f_anhvan = '%.1f' %anh_van 
        f_tongdiem = '%.1f' %tong_diem 
        s_SBD = '%3d' %SBD
        s_Phai = '%1d' %Phai
        s_ngay_sinh = '%02d/%02d/%04d' %(ngay_sinh.day,ngay_sinh.month,ngay_sinh.year)
        # Append elememt to list 
        lst_SBD.append(s_SBD)
        lst_Ho.append(Ho)
        lst_Ten.append(Ten)
        lst_phai.append(s_Phai)
        lst_ngaysinh.append(s_ngay_sinh)
        lst_toan.append(f_toan)
        lst_van.append(f_van)
        lst_anhvan.append(f_anhvan)
        lst_tongdiem.append(f_tongdiem)
        lst_xeploai.append(xep_loai)
        lst_doituongdt.append(doi_tuong_dt)
                    
    # Cache the dataframe so it's only loaded once
    @st.experimental_memo
    def load_data():
        return pd.DataFrame(
            {
                "SBD": lst_SBD,
                "Họ": lst_Ho,
                "Tên": lst_Ten,
                "Phái": lst_phai,
                "Ngày sinh": lst_ngaysinh,
                "Toán": lst_toan,
                "Văn": lst_van,
                "Anh văn": lst_anhvan,
                "Tổng điểm": lst_tongdiem,
                "Xếp loại": lst_xeploai,
                "Đối tượng dự thi": lst_doituongdt,
            }
        )
    # Boolean to resize the dataframe, stored as a session state variable
    st.checkbox("Use container width", value=False, key="use_container_width")


    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    df = load_data()
    st.dataframe(df, use_container_width=st.session_state.use_container_width)

def main():
    cau4()
if __name__ == "__main__":
    main()