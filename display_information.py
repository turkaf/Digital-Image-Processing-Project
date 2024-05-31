from PyQt5.QtWidgets import *
from display_information_python import Ui_Form
# from main_page import MainPage

class DisplayInfoPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.displayForm = Ui_Form()
        self.displayForm.setupUi(self)
        # self.openMainPage = MainPage()
        self.displayForm.pushButton_2.clicked.connect(self.DisplayMain)

    
    # def DisplayMain(self):
        # self.hide()
        # self.openMainPage.show()