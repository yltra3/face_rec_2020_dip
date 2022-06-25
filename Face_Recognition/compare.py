# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compare.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Compare(object):
    def setupUi(self, Compare):
        Compare.setObjectName("Compare")
        Compare.resize(408, 253)
        self.buttonBox = QtWidgets.QDialogButtonBox(Compare)
        self.buttonBox.setGeometry(QtCore.QRect(190, 160, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Compare)
        self.textEdit.setGeometry(QtCore.QRect(70, 30, 291, 111))
        self.textEdit.setObjectName("textEdit")
        self.toolButton = QtWidgets.QToolButton(Compare)
        self.toolButton.setGeometry(QtCore.QRect(70, 160, 71, 31))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Compare)
        self.buttonBox.accepted.connect(Compare.accept)
        self.buttonBox.rejected.connect(Compare.reject)
        QtCore.QMetaObject.connectSlotsByName(Compare)

    def retranslateUi(self, Compare):
        _translate = QtCore.QCoreApplication.translate
        Compare.setWindowTitle(_translate("Compare", "Dialog"))
        self.textEdit.setHtml(_translate("Compare", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Загрузите файл подходящего формата с прмощью кнопки Browser, затем нажмите кнопку &quot;Ok&quot;. Для возвращения нажмите кнопку &quot;Cancel&quot;.</span></p></body></html>"))
        self.toolButton.setText(_translate("Compare", "Browser"))
