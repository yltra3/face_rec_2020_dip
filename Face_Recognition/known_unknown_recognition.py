# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HeroW\PycharmProjects\untitled\recognition.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Recognition(object):
    def setupUi(self, Recognition):
        Recognition.setObjectName("Recognition")
        Recognition.resize(422, 246)
        self.buttonBox = QtWidgets.QDialogButtonBox(Recognition)
        self.buttonBox.setGeometry(QtCore.QRect(180, 150, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.toolButton = QtWidgets.QToolButton(Recognition)
        self.toolButton.setGeometry(QtCore.QRect(70, 150, 71, 31))
        self.toolButton.setObjectName("toolButton")
        self.textEdit = QtWidgets.QTextEdit(Recognition)
        self.textEdit.setGeometry(QtCore.QRect(70, 20, 291, 111))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Recognition)
        self.buttonBox.accepted.connect(Recognition.accept)
        self.buttonBox.rejected.connect(Recognition.reject)
        QtCore.QMetaObject.connectSlotsByName(Recognition)

    def retranslateUi(self, Recognition):
        _translate = QtCore.QCoreApplication.translate
        Recognition.setWindowTitle(_translate("Recognition", "Dialog"))
        self.toolButton.setText(_translate("Recognition", "Browser"))
        self.textEdit.setHtml(_translate("Recognition", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Загрузите файл подходящего формата с прмощью кнопки Browser, затем нажмите кнопку &quot;Ok&quot;. Для возвращения нажмите кнопку &quot;Cancel&quot;.</span></p></body></html>"))
