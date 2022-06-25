import sys
from PyQt5 import QtWidgets
from main import Ui_MainWindow
from pull_faces import Ui_Many_Faces
from known_unknown_recognition import Ui_Recognition
from count_of_faces import  Ui_Count_of_faces
from webcam import Ui_Webcam
from NewData import Ui_Video_base
from compare import Ui_Compare
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Many = Many_Faces(self)
        self.ui.pushButton.clicked.connect(lambda: self.Many.show())

        self.Rec = Recognition(self)
        self.ui.pushButton_2.clicked.connect(lambda: self.Rec.show())

        self.Count = Count_of_faces(self)
        self.ui.pushButton_3.clicked.connect(lambda: self.Count.show())

        self.Web = Webcam(self)
        self.ui.pushButton_4.clicked.connect(lambda: self.Web.show())

        self.Video = Video_base(self)
        self.ui.pushButton_5.clicked.connect(lambda: self.Video.show())

        self.Comp = Compare(self)
        self.ui.pushButton_6.clicked.connect(lambda: self.Comp.show())
class Compare(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Compare()
        self.ui.setupUi(self)
class Recognition(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Recognition()
        self.ui.setupUi(self)
class Video_base(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Video_base()
        self.ui.setupUi(self)
class Webcam(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Webcam()
        self.ui.setupUi(self)

class Count_of_faces(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Count_of_faces()
        self.ui.setupUi(self)

class Many_Faces(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Many_Faces()
        self.ui.setupUi(self)
def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()