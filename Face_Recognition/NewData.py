# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HeroW\PycharmProjects\untitled\video_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Video_base(object):
    def setupUi(self, Video_base):
        Video_base.setObjectName("Video_base")
        Video_base.resize(400, 224)
        self.buttonBox = QtWidgets.QDialogButtonBox(Video_base)
        self.buttonBox.setGeometry(QtCore.QRect(170, 150, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit = QtWidgets.QTextEdit(Video_base)
        self.textEdit.setGeometry(QtCore.QRect(50, 20, 291, 111))
        self.textEdit.setObjectName("textEdit")
        self.toolButton = QtWidgets.QToolButton(Video_base)
        self.toolButton.setGeometry(QtCore.QRect(50, 150, 71, 31))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Video_base)
        self.buttonBox.accepted.connect(Video_base.accept)
        self.buttonBox.rejected.connect(Video_base.reject)
        QtCore.QMetaObject.connectSlotsByName(Video_base)

    def retranslateUi(self, Video_base):
        _translate = QtCore.QCoreApplication.translate
        Video_base.setWindowTitle(_translate("Video_base", "Dialog"))
        self.textEdit.setHtml(_translate("Video_base", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Загрузите файл подходящего формата с прмощью кнопки Browser, затем нажмите кнопку &quot;Ok&quot;. Для возвращения нажмите кнопку &quot;Cancel&quot;.</span></p></body></html>"))
        self.toolButton.setText(_translate("Video_base", "Browser"))
