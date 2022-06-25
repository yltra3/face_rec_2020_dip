# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HeroW\PycharmProjects\untitled\webcam.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Webcam(object):
    def setupUi(self, Webcam):
        Webcam.setObjectName("Webcam")
        Webcam.resize(400, 216)
        self.buttonBox = QtWidgets.QDialogButtonBox(Webcam)
        self.buttonBox.setGeometry(QtCore.QRect(170, 140, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.toolButton = QtWidgets.QToolButton(Webcam)
        self.toolButton.setGeometry(QtCore.QRect(50, 140, 71, 31))
        self.toolButton.setObjectName("toolButton")
        self.textEdit = QtWidgets.QTextEdit(Webcam)
        self.textEdit.setGeometry(QtCore.QRect(50, 10, 291, 111))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Webcam)
        self.buttonBox.accepted.connect(Webcam.accept)
        self.buttonBox.rejected.connect(Webcam.reject)
        QtCore.QMetaObject.connectSlotsByName(Webcam)

    def retranslateUi(self, Webcam):
        _translate = QtCore.QCoreApplication.translate
        Webcam.setWindowTitle(_translate("Webcam", "Dialog"))
        self.toolButton.setText(_translate("Webcam", "Browser"))
        self.textEdit.setHtml(_translate("Webcam", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Загрузите файл подходящего формата с прмощью кнопки Browser, затем нажмите кнопку &quot;Ok&quot;. Для возвращения нажмите кнопку &quot;Cancel&quot;.</span></p></body></html>"))
