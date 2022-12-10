import pandas as pd
import streamlit as st
from mysql.connector import connect 
def cau8(sbd):
    query_cau_8= ("Select tmp_diem_thi_tong_hop.SBD, tmp_diem_thi_tong_hop.Ho, tmp_diem_thi_tong_hop.Ten, tmp_diem_thi_tong_hop.Phai, tmp_diem_thi_tong_hop.ngay_sinh, Toan, Van, anh_van, tong_diem,  "
                            +"IF(tong_diem >= 24 AND DTN >= 7,'Gioi', "
                            +"IF(tong_diem >= 21 AND DTN >= 6, 'Kha', "
                            +"IF(tong_diem >= 15 AND DTN >= 4, 'Trung binh', 'Chua Dat'))) As Xep_Loai, DTDT from tmp_diem_thi_tong_hop "
                            +"LEFT JOIN tbl_danh_sach ON tmp_diem_thi_tong_hop.SBD = tbl_danh_sach.SBD "
                            +"where tmp_diem_thi_tong_hop.SBD = "
                            + sbd)
    #print(query_cau_8)
    def connect_database_table():
        # Bước 1: Connect database db_quan_ly_diem_thi
        try:
            connect_database = connect(
                host="localhost",
                user="root",
                password="MinhVuong2003",
                database="db_quan_ly_diem_thi"
            )
        except:
            print('Không thể kết nối với database')
            exit()

        database_cursor = connect_database.cursor()
        # Bước 2: Xem table tbl_diem_thi_tong_hop
        query_xem_table = query_cau_8
        try:
            database_cursor.execute(query_xem_table)
        except:
            print('Không thể thực hiện query')
            exit()
                
        result = database_cursor.fetchall()
        return result
        # Lấy dữ liệu xong
        # Đóng cursor
        database_cursor.close()
        # Đóng database
        connect_database.close()

    result = connect_database_table()
    lst_SBD = []
    lst_Ho = []
    lst_Ten = []
    lst_phai = []
    lst_toan = []
    lst_van = []
    lst_anhvan = []
    lst_tongdiem = []
    lst_xeploai = []
    for row in result:
        SBD =        row[0]
        Ho =         row[1]
        Ten =        row[2]
        Phai =       row[3]
        Toan =       row[5]
        Van =        row[6]
        anh_van =    row[7]
        tong_diem =  row[8]
        xep_loai =   row[9]
        # Chuyển số và ngày thành chuỗi
        f_toan = '%.1f' %Toan 
        f_van = '%.1f' %Van 
        f_anhvan = '%.1f' %anh_van 
        f_tongdiem = '%.1f' %tong_diem 
        s_SBD = '%3d' %SBD
        s_Phai = '%1d' %Phai
        # Append elememt to list 
        lst_SBD.append(s_SBD)
        lst_Ho.append(Ho)
        lst_Ten.append(Ten)
        lst_phai.append(s_Phai)
        lst_toan.append(f_toan)
        lst_van.append(f_van)
        lst_anhvan.append(f_anhvan)
        lst_tongdiem.append(f_tongdiem)
        lst_xeploai.append(xep_loai)
    st.header('Kết quả thi')
    st.write("Số báo danh: ", lst_SBD[0])
    if lst_phai[0] == '0':
        st.write('Anh: ', str(lst_Ho[0]) + " " + str(lst_Ten[0]))
    elif lst_phai[0] == '1':
        st.write('Chị: ', str(lst_Ho[0]) + " " + str(lst_Ten[0]))
    st.write('Toán: ',lst_toan[0])
    st.write('Văn: ',lst_van[0])
    st.write('Anh Văn: ',lst_anhvan[0])
    st.write('Tổng điểm: ', lst_tongdiem[0])
    st.write('Xếp loại: ', lst_xeploai[0])


def main():
    nhap_sbd = st.text_input('Nhập số báo danh')
    if nhap_sbd != "":
        cau8(nhap_sbd)
if __name__ == "__main__":
    main()