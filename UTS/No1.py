# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataMahasiswa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEditDisplay = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDisplay.setGeometry(QtCore.QRect(50, 40, 261, 191))
        self.lineEditDisplay.setReadOnly(True)
        self.lineEditDisplay.setObjectName("lineEditDisplay")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(51, 251, 261, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditJurusan = QtWidgets.QLineEdit(self.widget)
        self.lineEditJurusan.setObjectName("lineEditJurusan")
        self.gridLayout.addWidget(self.lineEditJurusan, 2, 1, 1, 1)
        self.lineEditNama = QtWidgets.QLineEdit(self.widget)
        self.lineEditNama.setObjectName("lineEditNama")
        self.gridLayout.addWidget(self.lineEditNama, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditTelp = QtWidgets.QLineEdit(self.widget)
        self.lineEditTelp.setObjectName("lineEditTelp")
        self.gridLayout.addWidget(self.lineEditTelp, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEditNIM = QtWidgets.QLineEdit(self.widget)
        self.lineEditNIM.setObjectName("lineEditNIM")
        self.gridLayout.addWidget(self.lineEditNIM, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(87, 370, 221, 20))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tambah = QtWidgets.QPushButton(self.widget1)
        self.tambah.setAcceptDrops(False)
        self.tambah.setObjectName("tambah")
        self.horizontalLayout.addWidget(self.tambah)
        self.edit = QtWidgets.QPushButton(self.widget1)
        self.edit.setObjectName("edit")
        self.horizontalLayout.addWidget(self.edit)
        self.clear = QtWidgets.QPushButton(self.widget1)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.hapus = QtWidgets.QPushButton(self.widget1)
        self.hapus.setObjectName("hapus")
        self.horizontalLayout.addWidget(self.hapus)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tambah.clicked.connect(self.addItemButtonClick)
        self.edit.clicked.connect(self.editItemButtonClick)
        self.hapus.clicked.connect(self.lineEditDisplay.clear)

        self.retranslateUi(MainWindow)

        self.clear.clicked.connect(self.lineEditNIM.clear)
        self.clear.clicked.connect(self.lineEditNama.clear)
        self.clear.clicked.connect(self.lineEditJurusan.clear)
        self.clear.clicked.connect(self.lineEditTelp.clear)

    def addItemButtonClick(self):
        nama = self.lineEditNama.text()
        nim = self.lineEditNIM.text()
        jurusan = self.lineEditJurusan.text()
        noTelp = self.lineEditTelp.text()
        self.lineEditDisplay.setText("NIM : " + nim +
                                     "\nNAMA : " + nama +
                                     "\nJURUSAN : " + jurusan +
                                     "\nNO. TELP : " + noTelp)
        self.tambah.clicked.connect(self.lineEditNIM.clear)
        self.tambah.clicked.connect(self.lineEditNama.clear)
        self.tambah.clicked.connect(self.lineEditJurusan.clear)
        self.tambah.clicked.connect(self.lineEditTelp.clear)

    def editItemButtonClick(self):
        nama = self.lineEditNama.text()
        nim = self.lineEditNIM.text()
        jurusan = self.lineEditJurusan.text()
        noTelp = self.lineEditTelp.text()
        self.lineEditDisplay.setText("NIM : " + nim +
                                     "\nNAMA : " + nama +
                                     "\nJURUSAN : " + jurusan +
                                     "\nNO. TELP : " + noTelp)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Data Mahasiswa"))
        self.label.setText(_translate("MainWindow", "NIM"))
        self.label_3.setText(_translate("MainWindow", "Jurusan"))
        self.label_2.setText(_translate("MainWindow", "Nama"))
        self.label_4.setText(_translate("MainWindow", "No. Telp"))
        self.tambah.setText(_translate("MainWindow", "Tambah"))
        self.edit.setText(_translate("MainWindow", "Edit"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.hapus.setText(_translate("MainWindow", "Hapus"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

