# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HeroW\PycharmProjects\untitled\many_faces.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Many_Faces(object):
    def setupUi(self, Many_Faces):
        Many_Faces.setObjectName("Many_Faces")
        Many_Faces.resize(404, 230)
        self.buttonBox = QtWidgets.QDialogButtonBox(Many_Faces)
        self.buttonBox.setGeometry(QtCore.QRect(180, 140, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Many_Faces)
        self.textEdit.setGeometry(QtCore.QRect(50, 10, 291, 111))
        self.textEdit.setObjectName("textEdit")
        self.toolButton = QtWidgets.QToolButton(Many_Faces)
        self.toolButton.setGeometry(QtCore.QRect(50, 140, 71, 31))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Many_Faces)
        self.buttonBox.accepted.connect(Many_Faces.accept)
        self.buttonBox.rejected.connect(Many_Faces.reject)
        QtCore.QMetaObject.connectSlotsByName(Many_Faces)

    def retranslateUi(self, Many_Faces):
        _translate = QtCore.QCoreApplication.translate
        Many_Faces.setWindowTitle(_translate("Many_Faces", "Dialog"))
        self.textEdit.setHtml(_translate("Many_Faces", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Загрузите файл подходящего формата с прмощью кнопки Browser, затем нажмите кнопку &quot;Ok&quot;. Для возвращения нажмите кнопку &quot;Cancel&quot;.</span></p></body></html>"))
        self.toolButton.setText(_translate("Many_Faces", "Browser"))
