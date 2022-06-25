# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HeroW\PycharmProjects\untitled\count_of_faces.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Count_of_faces(object):
    def setupUi(self, Count_of_faces):
        Count_of_faces.setObjectName("Count_of_faces")
        Count_of_faces.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Count_of_faces)
        self.buttonBox.setGeometry(QtCore.QRect(180, 150, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.toolButton = QtWidgets.QToolButton(Count_of_faces)
        self.toolButton.setGeometry(QtCore.QRect(60, 150, 71, 31))
        self.toolButton.setObjectName("toolButton")
        self.textEdit = QtWidgets.QTextEdit(Count_of_faces)
        self.textEdit.setGeometry(QtCore.QRect(60, 20, 291, 111))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Count_of_faces)
        self.buttonBox.accepted.connect(Count_of_faces.accept)
        self.buttonBox.rejected.connect(Count_of_faces.reject)
        QtCore.QMetaObject.connectSlotsByName(Count_of_faces)

    def retranslateUi(self, Count_of_faces):
        _translate = QtCore.QCoreApplication.translate
        Count_of_faces.setWindowTitle(_translate("Count_of_faces", "Dialog"))
        self.toolButton.setText(_translate("Count_of_faces", "Browser"))
        self.textEdit.setHtml(_translate("Count_of_faces", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Загрузите файл подходящего формата с прмощью кнопки Browser, затем нажмите кнопку &quot;Ok&quot;. Для возвращения нажмите кнопку &quot;Cancel&quot;.</span></p></body></html>"))
