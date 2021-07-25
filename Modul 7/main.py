# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datamhs.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from PyQt5.QtWidgets import *
from datamhs import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.koneksi()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(594, 592)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 601, 631))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(-10, 0, 601, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/ASUS/OneDrive/Pictures/Saved Pictures/Background1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 90, 511, 120))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")

        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtNim = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNim.setObjectName("txtNim")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtNim)

        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.txtNama = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNama.setObjectName("txtNama")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtNama)

        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.txtJurusan = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtJurusan.setObjectName("txtJurusan")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtJurusan)

        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.txtNo = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNo.setObjectName("txtNo")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.txtNo)

        self.btnSubmit = QtWidgets.QPushButton(self.tab)
        self.btnSubmit.setGeometry(QtCore.QRect(460, 230, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setObjectName("btnSubmit")

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(0, 5, 591, 511))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/ASUS/OneDrive/Pictures/Saved Pictures/Background1.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.btnLogin = QtWidgets.QPushButton(self.tab_2)
        self.btnLogin.setGeometry(QtCore.QRect(420, 210, 93, 28))
        self.btnLogin.setObjectName("btnLogin")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(200, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(70, 130, 441, 61))
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")

        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.txtPass = QtWidgets.QLineEdit(self.widget)
        self.txtPass.setObjectName("txtPass")
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtPass)

        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.txtUname = QtWidgets.QLineEdit(self.widget)
        self.txtUname.setObjectName("txtUname")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtUname)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnSubmit.clicked.connect(self.submit)
        self.btnLogin.clicked.connect(self.login)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Form Mahasiswa"))
        self.label_3.setText(_translate("MainWindow", "NIM"))
        self.label_4.setText(_translate("MainWindow", "Nama"))
        self.label_5.setText(_translate("MainWindow", "Jurusan"))
        self.label_6.setText(_translate("MainWindow", "No. Telp"))
        self.btnSubmit.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Form"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.label_10.setText(_translate("MainWindow", "Login Admin"))
        self.label_8.setText(_translate("MainWindow", "Username"))
        self.label_9.setText(_translate("MainWindow", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Admin"))

    def koneksi(self):
        con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if (cur):
            self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
            self.messagebox("Koneksi", "Koneksi Gagal")

    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def submit(self):
        nim = self.txtNim.text()
        nama = self.txtNama.text()
        jurusan = self.txtJurusan.text()
        no = self.txtNo.text()
        insert = (nim, nama, jurusan, no)
        print(insert)
        if self.txtNim.text() and self.txtNama.text() and self.txtJurusan.text() and self.txtNo.text():
            con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "INSERT INTO mhs(nim, nama, jurusan, no)" + "VALUES" + str(insert)
            data = cur.execute(sql)
            self.messagebox("SUKSES", "Data Berhasil di Submit")
        else:
            self.messagebox("GAGAL", "Mohon lengkapi form ")

    def login(self):
        uname = self.txtUname.text()
        pw = self.txtPass.text()
        con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "SELECT * from admin where uname=%s and pw=%s"
        data = cur.execute(sql, (uname, pw))
        if (len(cur.fetchall()) > 0):
            self.openadmin()
        else:
            self.messagebox("GAGAL", "Username atau Password Salah ! ")
        self.clearlogin()

    def edit(self):
        nim = self.datamhs.txtNim.text()
        nama = self.datamhs.txtNama.text()
        jurusan = self.datamhs.txtJurusan.text()
        no = self.datamhs.txtNo.text()
        insert = (nim, nama, jurusan, no)
        if self.datamhs.txtNim.text() and self.datamhs.txtNama.text() and self.datamhs.txtJurusan.text() and self.datamhs.txtNo.text():
            con = pymysql.connect(db='tubes_gui', user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "UPDATE mhs set nama='" + str(nama) + "', jurusan='" + str(jurusan) + "', no='" + str(no) + "' where nim='" + str(nim) + "'"
            data = cur.execute(sql)
            Ui_MainWindow.messagebox(Ui_MainWindow, "SUKSES", "Data Berhasil di Submit")
        else:
            Ui_MainWindow.messagebox(Ui_MainWindow, "GAGAL", "Mohon lengkapi form ")

    def hapus(self):
        nim = self.datamhs.txtNim.text()
        if self.datamhs.txtNim.text():
            con = pymysql.connect(db='tubes_gui', user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "DELETE from mhs where nim='" + str(nim) + "'"
            data = cur.execute(sql)
            Ui_MainWindow.messagebox(Ui_MainWindow, "SUKSES", "Data Berhasil di Hapus")
        else:
            Ui_MainWindow.messagebox(Ui_MainWindow, "GAGAL", "Mohon isi nim dengan sesuai ")

    def baca(self):
        con =  pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        result = cur.execute("SELECT * FROM mhs")
        self.datamhs.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(cur):
            self.datamhs.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.datamhs.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def clear(self):
        self.datamhs.txtNim.clear()
        self.datamhs.txtNim.setEnabled(True)
        self.datamhs.txtNama.clear()
        self.datamhs.txtJurusan.clear()
        self.datamhs.txtNo.clear()

class datamhs(QWidget):
    def __init__(self):
        super().__init__()
        self.datamhs = Ui_datamhs()
        self.datamhs.setupUi(self)
        self.datamhs.btnTambah.clicked.connect(self.submit)
        self.datamhs.btnEdit.clicked.connect(self.edit)
        self.datamhs.btnHapus.clicked.connect(self.hapus)
        self.datamhs.btnClear.clicked.connect(self.clear)
        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        self.datamhs.tableWidget.setColumnCount(4)
        self.datamhs.tableWidget.setHorizontalHeaderLabels(('nim', 'nama', 'jurusan', 'no'))
        self.timer.timeout.connect(self.baca)


    def submit(self):
        nim = self.datamhs.txtNim.text()
        nama = self.datamhs.txtNama.text()
        jurusan = self.datamhs.txtJurusan.text()
        no = self.datamhs.txtNo.text()
        insert = (nim, nama, jurusan, no)
        print(insert)
        if self.datamhs.txtNim.text() and self.datamhs.txtNama.text() and self.datamhs.txtJurusan.text() and self.datamhs.txtNo.text():
            135
            con = pymysql.connect(db='db_mhs', user='root', passwd='', host='localhost', port=3306, autocommit=True)
            cur = con.cursor()
            sql = "INSERT INTO mhs(nim, nama, jurusan, no)" + " VALUES " + str(insert)
            data = cur.execute(sql)
            Ui_MainWindow.messagebox(Ui_MainWindow, "SUKSES", "Data Berhasil di Submit")
        else:
            Ui_MainWindow.messagebox(Ui_MainWindow, "GAGAL", "Mohon lengkapi form ")

class Ui_datamhs(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

