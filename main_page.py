from PyQt5.QtWidgets import *
from main_page_python import Ui_Form
from display_information import DisplayInfoPage
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
import numpy as np
import os
import cv2
from utils import rescale

class MainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.mainForm = Ui_Form()
        self.mainForm.setupUi(self)
        self.openDisplayInfoPage = DisplayInfoPage()
        self.pixmap = QPixmap()
        self.inverse_pixmap = QPixmap()
        self.enhanced_pixmap = QPixmap()
        self.result_pixmap = QPixmap()
        self.mainForm.pushButton_select_image.clicked.connect(self.SelectImage)
        self.mainForm.pushButton_display_results.clicked.connect(self.DisplayInfo)


    def SelectImage(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '.', 'Image Files (*.png *.jpg *.jpeg *.bmp *.tif)')
        image_name = os.path.split(file_path)[-1]

        if file_path:
            self.mainForm.lbl_select_image.setText(image_name)

            image = Image.open(file_path)
            numpy_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_BGR2RGB)

            genislik = 251
            yükseklik = 281
            boyut = (genislik, yükseklik)

            opencv_image = cv2.resize(opencv_image, boyut)

            inverse_image = self.inverse_image(opencv_image)

            enhanced_image = self.gamma_correction(opencv_image, 1, 0.4)

            result_image = self.binary_slicing(opencv_image, 150, 200, 10, 255)

            
            #original image parts
            height, width, channel = opencv_image.shape
            bytesPerLine = 3 * width
            q_image = QImage(opencv_image.data, width, height, bytesPerLine, QImage.Format_RGB888)

            self.pixmap = QPixmap.fromImage(q_image).scaled(width, height)

            #inverse of image parts
            height, width, channel = opencv_image.shape
            bytesPerLine = 3 * width
            q_image_inverse = QImage(inverse_image.data, width, height, bytesPerLine, QImage.Format_RGB888)

            self.inverse_pixmap = QPixmap.fromImage(q_image_inverse).scaled(width, height)


            #enhanced image parts
            height, width, channel = opencv_image.shape
            bytesPerLine = 3 * width
            q_enhanced_image = QImage(enhanced_image.data, width, height, bytesPerLine, QImage.Format_RGB888)

            self.enhanced_pixmap = QPixmap.fromImage(q_enhanced_image).scaled(width, height)


            #result image parts
            height, width, channel = opencv_image.shape
            bytesPerLine = 3 * width
            q_result_image = QImage(result_image.data, width, height, bytesPerLine, QImage.Format_RGB888)

            self.result_pixmap = QPixmap.fromImage(q_result_image).scaled(width, height)
            

    def DisplayInfo(self):
        self.hide()
        self.openDisplayInfoPage.show()
        self.openDisplayInfoPage.displayForm.label_original_image.setPixmap(self.pixmap)
        self.openDisplayInfoPage.displayForm.label_inverse_image.setPixmap(self.inverse_pixmap)
        self.openDisplayInfoPage.displayForm.label_enhanced_image.setPixmap(self.enhanced_pixmap)
        self.openDisplayInfoPage.displayForm.label_result_image.setPixmap(self.result_pixmap)


    # Inverse of image function
    def inverse_image(self, img):
        L = np.max(img)
        inverse_img = L - img
        return inverse_img
    

    # Enhanced contrast function
    def gamma_correction(self, img, c, gamma):
        # img = img.dtype(float)
        s = c*img**gamma
        s = rescale(s)
        return s
    

    # Result function
    def binary_slicing(self, img, A, B, low_value, high_value):
        result_img = np.full_like(img, low_value)
        index = np.logical_and(img > A, img < B)
        result_img[index] = high_value
        return result_img