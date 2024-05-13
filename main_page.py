from PyQt5.QtWidgets import *
from main_page_python import Ui_Form
from display_information import DisplayInfoPage
import cv2

class MainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        self.openDisplayInfoPage = DisplayInfoPage()
        self.mainForm.pushButton_select_image.clicked.connect(self.SelectImage)
        self.mainForm.pushButton_display_results.clicked.connect(self.DisplayInfo)

    def SelectImage(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp)")
        
        if filename:
            image = cv2.imread(filename)

            if image is not None:
                self.mainForm.lbl_select_image.setText("Seçilen Resim: " + filename.split('/')[-1])

    def DisplayInfo(self):
        self.hide()
        self.openDisplayInfoPage.show()