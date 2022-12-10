import tkinter as tk
import tkinter.ttk as ttk
from mysql.connector import connect 

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý điểm thi")
        self.notebook = ttk.Notebook(self)
        # Câu 3 - Xếp loại học sinh
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text = "Câu 3 - Xếp loại học sinh", underline = 0, sticky = tk.NE + tk.SW)
        # TreeView- DanhSach sẽ nằm trong frame
        columns = ("#1", "#2", "#3", "#4", "#5", "#6")
        self.tree = ttk.Treeview(frame, show="headings", columns=columns)
        self.tree.heading("#1", text="SBD")
        self.tree.heading("#2", text="Ho")
        self.tree.heading("#3", text="Ten")
        self.tree.heading("#4", text="Phai")
        self.tree.heading("#5", text="NgaySinh")
        self.tree.heading("#6", text="DTDT")

        self.tree.column("#1", anchor=tk.E, width = 50)
        self.tree.column("#3",width = 50)
        self.tree.column("#4",anchor=tk.E ,width = 40)
        self.tree.column("#5", anchor=tk.E ,width = 80)
        self.tree.column("#6", width = 40)
        ysb = ttk.Scrollbar(frame, orient=tk.VERTICAL,
                            command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        # 1.1.Đưa vào bằng MySQL
        self.result = None
        self.connect_database_table_DanhSach()
        for row in self.result:
            SBD =        row[0]
            Ho =         row[1]
            Ten =        row[2]
            Phai =       row[3]
            ngay_sinh =  row[4]
            DTDT =       row[5]
            # Chuyển số và ngày thành chuỗi
            s_SBD = '%3d' %SBD
            s_Phai = '%1d' %Phai
            s_ngay_sinh = '%02d/%02d/%04d' %(ngay_sinh.day,ngay_sinh.month,ngay_sinh.year)
            s_DTDT = '%1d' %DTDT

            line = [s_SBD,Ho,Ten,s_Phai,s_ngay_sinh,s_DTDT]
            self.tree.insert("",tk.END, values = line)

        self.tree.grid(row=0, column=0, padx = 5, pady = 5)
        ysb.grid(row=0, column=1, padx = 5, pady = 5, sticky=tk.N + tk.S)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.tree.grid(row=0, column=0, padx = 5, pady = 5, sticky=tk.NW)
        ysb.grid(row=0, column=1, padx = 5, pady = 5, sticky = tk.N + tk.S)
        frame.columnconfigure(0, weight=1)

        
        # 2.Tạo Frame cho table_DiemThi
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text = "DiemThi", underline = 4, sticky = tk.NE + tk.SW)
        # TreeView - DiemThi sẽ nằm trong frame
        columns = ("#1", "#2", "#3", "#4")
        self.tree = ttk.Treeview(frame, show="headings", columns=columns)
        self.tree.heading("#1", text="SBD")
        self.tree.heading("#2", text="Toan")
        self.tree.heading("#3", text="Van")
        self.tree.heading("#4", text="AnhVan")

        self.tree.column("#1", anchor=tk.E, width = 50)
        self.tree.column("#2", anchor=tk.E, width = 70)
        self.tree.column("#3", anchor=tk.E, width = 70)
        self.tree.column("#4", anchor=tk.E ,width = 70)
       
        ysb = ttk.Scrollbar(frame, orient=tk.VERTICAL,
                            command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)
        
        #2.1. Đưa vào bằng MySQL
        self.result = None
        self.connect_database_table_DiemThi()
        for row in self.result:
            SBD =        row[0]
            Toan =        row[1]
            Van =        row[2]
            AnhVan =       row[3]
            # Chuyển số và ngày thành chuỗi
            s_SBD = '%3d' %SBD
            s_Toan = '%.1f' %Toan
            s_Van = '%.1f' %Van
            s_AnhVan = '%.1f' %AnhVan

            line = [s_SBD, s_Toan, s_Van, s_AnhVan]
            self.tree.insert("",tk.END, values = line)


        
        self.tree.grid(row=0, column=0, padx = 5, pady = 5, sticky=tk.NW)
        ysb.grid(row=0, column=1, padx = 5, pady = 5, sticky = tk.N + tk.S)
        frame.columnconfigure(0, weight=1)

        # 3.Tạo Frame cho table_ChiTietDT
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text = "Chi Tiet DT", underline = 0, sticky = tk.NE + tk.SW)
        # TreeView- ChiTietDT sẽ nằm trong frame
        columns = ("#1", "#2", "#3")
        self.tree = ttk.Treeview(frame, show="headings", columns=columns)
        self.tree.heading("#1", text="DTDT")
        self.tree.heading("#2", text="DienGiai")
        self.tree.heading("#3", text="DiemUT")

        self.tree.column("#1", anchor=tk.CENTER, width = 50)
        self.tree.column("#2",width = 300)
        self.tree.column("#3",anchor=tk.CENTER ,width = 50)
        ysb = ttk.Scrollbar(frame, orient=tk.VERTICAL,
                            command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        # 3.1. Đưa vào bằng MySQL
        self.result = None
        self.connect_database_table_ChiTietDT()
        for row in self.result:
            DTDT =        row[0]
            DGDT =        row[1]
            DiemUT =       row[2]
            # Chuyển số và ngày thành chuỗi
            s_DTDT = '%1d' %DTDT
            s_DiemUT = '%1d' %DiemUT

            line = [s_DTDT,DGDT,s_DiemUT]
            self.tree.insert("",tk.END, values = line)

        self.tree.grid(row=0, column=0, padx = 5, pady = 5, sticky=tk.NW)
        ysb.grid(row=0, column=1, padx = 5, pady = 5, sticky = tk.N + tk.S)
        frame.columnconfigure(0, weight=1)

        # Đưa notebook vào grid
        self.notebook.grid(row = 0, column = 0, padx = 5, pady = 5) 
    
    def connect_database_table_DanhSach(self):
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

            # Bước 2: Xem table tbl_chi_tiet_dt
            query_xem_table = "select * from tbl_danh_sach;"
            try:
                database_cursor.execute(query_xem_table)
            except:
                print('Không thể thực hiện query')
                exit()

            self.result = database_cursor.fetchall()
            
            # Quan trọng It’s crucial to call .commit() 
            # after preforming any modifications to a table.
            # Trong ví dụ này ta không thay đổi table nên không cần commit

            # Lấy dữ liệu xong
            # Đóng cursor
            database_cursor.close()
            # Đóng database
            connect_database.close()
    def connect_database_table_DiemThi(self):
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

            # Bước 2: Xem table tbl_chi_tiet_dt
            query_xem_table = "select * from tbl_diem_thi;"
            try:
                database_cursor.execute(query_xem_table)
            except:
                print('Không thể thực hiện query')
                exit()

            self.result = database_cursor.fetchall()
            
            # Quan trọng It’s crucial to call .commit() 
            # after preforming any modifications to a table.
            # Trong ví dụ này ta không thay đổi table nên không cần commit

            # Lấy dữ liệu xong
            # Đóng cursor
            database_cursor.close()
            # Đóng database
            connect_database.close()
        
    def connect_database_table_ChiTietDT(self):
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

            # Bước 2: Xem table tbl_chi_tiet_dt
            query_xem_table = "select * from tbl_chi_tiet_dt;"
            try:
                database_cursor.execute(query_xem_table)
            except:
                print('Không thể thực hiện query')
                exit()

            self.result = database_cursor.fetchall()
            
            # Quan trọng It’s crucial to call .commit() 
            # after preforming any modifications to a table.
            # Trong ví dụ này ta không thay đổi table nên không cần commit

            # Lấy dữ liệu xong
            # Đóng cursor
            database_cursor.close()
            # Đóng database
            connect_database.close()


if __name__ == "__main__":
    app = App()
    app.mainloop()
