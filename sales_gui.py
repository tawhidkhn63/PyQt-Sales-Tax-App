# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sales_tax_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pricebox = QtWidgets.QTextEdit(self.centralwidget)
        self.pricebox.setGeometry(QtCore.QRect(200, 60, 431, 51))
        self.pricebox.setObjectName("pricebox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.taxrate = QtWidgets.QSpinBox(self.centralwidget)
        self.taxrate.setGeometry(QtCore.QRect(230, 180, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.taxrate.setFont(font)
        self.taxrate.setProperty("value", 20)
        self.taxrate.setObjectName("taxrate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(114, 220, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.calc_tax_button = QtWidgets.QPushButton(self.centralwidget)
        self.calc_tax_button.setGeometry(QtCore.QRect(260, 320, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.calc_tax_button.setFont(font)
        self.calc_tax_button.setObjectName("calc_tax_button")
        self.results = QtWidgets.QTextEdit(self.centralwidget)
        self.results.setGeometry(QtCore.QRect(270, 380, 104, 64))
        self.results.setObjectName("results")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "price"))
        self.label_2.setText(_translate("MainWindow", "tax rate"))
        self.calc_tax_button.setText(_translate("MainWindow", "calculate tax"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
