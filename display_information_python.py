# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display_information_python.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 900)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 561, 152))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        self.label_original_image = QtWidgets.QLabel(Form)
        self.label_original_image.setGeometry(QtCore.QRect(20, 250, 251, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_original_image.setFont(font)
        self.label_original_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_original_image.setObjectName("label_original_image")
        self.label_result_image = QtWidgets.QLabel(Form)
        self.label_result_image.setGeometry(QtCore.QRect(330, 250, 251, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_result_image.setFont(font)
        self.label_result_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result_image.setObjectName("label_result_image")
        self.label_enhanced_image = QtWidgets.QLabel(Form)
        self.label_enhanced_image.setGeometry(QtCore.QRect(20, 590, 251, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_enhanced_image.setFont(font)
        self.label_enhanced_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_enhanced_image.setObjectName("label_enhanced_image")
        self.label_inverse_image = QtWidgets.QLabel(Form)
        self.label_inverse_image.setGeometry(QtCore.QRect(330, 590, 251, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_inverse_image.setFont(font)
        self.label_inverse_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_inverse_image.setObjectName("label_inverse_image")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(450, 10, 131, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 10, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 210, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 550, 182, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(390, 550, 131, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Identity Number"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Patient Name"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Age"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "Gender"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "Status"))
        self.label_original_image.setText(_translate("Form", "NO IMAGE"))
        self.label_result_image.setText(_translate("Form", "NO IMAGE"))
        self.label_enhanced_image.setText(_translate("Form", "NO IMAGE"))
        self.label_inverse_image.setText(_translate("Form", "NO IMAGE"))
        self.pushButton.setText(_translate("Form", "Print"))
        self.pushButton_2.setText(_translate("Form", "New Patient"))
        self.label.setText(_translate("Form", "Original Image"))
        self.label_2.setText(_translate("Form", "Result Image"))
        self.label_3.setText(_translate("Form", "Enhanced Contrast"))
        self.label_4.setText(_translate("Form", "Inverse Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
