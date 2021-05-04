# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayData.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# Komponen
# Main Windows
# centralwidget
# verticalLayout
# gridLayout
# QlistView
# horizontalLayout
# QLabel
# QPushButton
# QLineEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(315, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 274, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.layoutWidget)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.NIMEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.NIMEdit.setObjectName("NIMEdit")
        self.gridLayout.addWidget(self.NIMEdit, 0, 1, 1, 1)
        self.NoTelp = QtWidgets.QLabel(self.layoutWidget)
        self.NoTelp.setObjectName("NoTelp")
        self.gridLayout.addWidget(self.NoTelp, 3, 0, 1, 1)
        self.NIM = QtWidgets.QLabel(self.layoutWidget)
        self.NIM.setObjectName("NIM")
        self.gridLayout.addWidget(self.NIM, 0, 0, 1, 1)
        self.Nama = QtWidgets.QLabel(self.layoutWidget)
        self.Nama.setObjectName("Nama")
        self.gridLayout.addWidget(self.Nama, 1, 0, 1, 1)
        self.NamaEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.NamaEdit.setObjectName("NamaEdit")
        self.gridLayout.addWidget(self.NamaEdit, 1, 1, 1, 1)
        self.Jurusan = QtWidgets.QLabel(self.layoutWidget)
        self.Jurusan.setObjectName("Jurusan")
        self.gridLayout.addWidget(self.Jurusan, 2, 0, 1, 1)
        self.JurusanEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.JurusanEdit.setObjectName("JurusanEdit")
        self.gridLayout.addWidget(self.JurusanEdit, 2, 1, 1, 1)
        self.NoTelpEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.NoTelpEdit.setObjectName("NoTelpEdit")
        self.gridLayout.addWidget(self.NoTelpEdit, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TAMBAH = QtWidgets.QPushButton(self.layoutWidget)
        self.TAMBAH.setObjectName("TAMBAH")
        self.horizontalLayout.addWidget(self.TAMBAH)
        self.EDIT = QtWidgets.QPushButton(self.layoutWidget)
        self.EDIT.setObjectName("EDIT")
        self.horizontalLayout.addWidget(self.EDIT)
        self.CLEAR = QtWidgets.QPushButton(self.layoutWidget)
        self.CLEAR.setObjectName("CLEAR")
        self.horizontalLayout.addWidget(self.CLEAR)
        self.HAPUS = QtWidgets.QPushButton(self.layoutWidget)
        self.HAPUS.setObjectName("HAPUS")
        self.horizontalLayout.addWidget(self.HAPUS)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 315, 18))
        self.menubar.setObjectName("menubar")
        self.menuMainWindows = QtWidgets.QMenu(self.menubar)
        self.menuMainWindows.setObjectName("menuMainWindows")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMainWindows.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DATA MAHASISWA"))
        self.NoTelp.setText(_translate("MainWindow", "No.Telp"))
        self.NIM.setText(_translate("MainWindow", "NIM"))
        self.Nama.setText(_translate("MainWindow", "Nama"))
        self.Jurusan.setText(_translate("MainWindow", "Jurusan"))
        self.TAMBAH.setText(_translate("MainWindow", "TAMBAH"))
        self.EDIT.setText(_translate("MainWindow", "EDIT"))
        self.CLEAR.setText(_translate("MainWindow", "CLEAR"))
        self.HAPUS.setText(_translate("MainWindow", "HAPUS"))
        self.menuMainWindows.setTitle(_translate("MainWindow", "MainWindows"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

