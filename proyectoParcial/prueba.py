# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(694, 383)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 70, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 260, 141, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 300, 141, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 340, 141, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 300, 141, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 340, 141, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 150, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 260, 141, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(300, 260, 91, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(300, 300, 89, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(300, 340, 89, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 256, 192))
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(430, 40, 256, 192))
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)

        self.retranslateUi(Form)
        self.pushButton_10.clicked.connect(self.listWidget.clear)
        self.pushButton_10.clicked.connect(self.listWidget_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Navegador de Archivos"))
        self.pushButton.setText(_translate("Form", "←"))
        self.pushButton_2.setText(_translate("Form", "Agregar Directorio"))
        self.pushButton_3.setText(_translate("Form", "Agregar Archivo"))
        self.pushButton_4.setText(_translate("Form", "Eliminar Nodo"))
        self.pushButton_5.setText(_translate("Form", "Agregar Archivo"))
        self.pushButton_6.setText(_translate("Form", "Eliminar Nodo"))
        self.pushButton_7.setText(_translate("Form", "→"))
        self.pushButton_8.setText(_translate("Form", "Agregar Directorio"))
        self.pushButton_9.setText(_translate("Form", "Guardar"))
        self.pushButton_10.setText(_translate("Form", "Limpiar"))
        self.pushButton_11.setText(_translate("Form", "Salir"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "."))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "    usr"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "    home"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "    lib"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "    os"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "    debian"))
        item = self.listWidget.item(6)
        item.setText(_translate("Form", "    algo"))
        item = self.listWidget.item(7)
        item.setText(_translate("Form", ".."))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Form", "."))
        item = self.listWidget_2.item(1)
        item.setText(_translate("Form", "    usr"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("Form", "    home"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("Form", "    lib"))
        item = self.listWidget_2.item(4)
        item.setText(_translate("Form", "    os"))
        item = self.listWidget_2.item(5)
        item.setText(_translate("Form", "    debian"))
        item = self.listWidget_2.item(6)
        item.setText(_translate("Form", "    algo"))
        item = self.listWidget_2.item(7)
        item.setText(_translate("Form", ".."))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())