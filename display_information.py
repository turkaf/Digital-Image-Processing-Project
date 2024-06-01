from PyQt5.QtWidgets import *
from display_information_python import Ui_Form

from PyQt5.QtCore import Qt, QSizeF
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPixmap, QPainter, QPageSize, QImage

class DisplayInfoPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.displayForm = Ui_Form()
        self.displayForm.setupUi(self)
        self.displayForm.pushButton_print.clicked.connect(self.print_pdf)


    # def print_pdf(self):
    #     filename, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
    #     if filename:
    #         printer = QPrinter(QPrinter.HighResolution)
    #         printer.setOutputFormat(QPrinter.PdfFormat)
    #         printer.setOutputFileName(filename)

    #         page_size = QPageSize(QPageSize.A4)
    #         printer.setPageSize(page_size)

    #         painter = QPainter(printer)

    #         viewport_size = self.size()
    #         painter.setViewport(0, 0, viewport_size.width(), viewport_size.height())

    #         self.displayForm.pushButton_print.hide()
    #         self.displayForm.pushButton_2.hide()

    #         painter.setWindow(self.displayForm.label_original_image.rect())

    #         self.render(painter)

    #         painter.end()

    #         self.displayForm.pushButton_print.show()
    #         self.displayForm.pushButton_2.show()

    #         print("PDF saved successfully!")

    
    def print_pdf(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if filename:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(filename)

            page_size = QPageSize(QPageSize.A4)
            printer.setPageSize(page_size)

            painter = QPainter(printer)

            # Get the size of the page
            page_rect = printer.pageRect()

            # Set the viewport to the size of the page
            painter.setViewport(0, 0, page_rect.width(), page_rect.height())

            self.displayForm.pushButton_print.hide()
            self.displayForm.pushButton_2.hide()

            # Set the window to the size of the page
            painter.setWindow(0, 0, page_rect.width(), page_rect.height())

            # Get the size of the central widget
            widget_rect = self.rect()

            # Scale the widget to fit the page
            scale = min(page_rect.width() / widget_rect.width(), page_rect.height() / widget_rect.height())
            painter.scale(scale, scale)

            # Calculate the translation to center the image
            x_translation = (page_rect.width() / scale - widget_rect.width()) / 2
            y_translation = (page_rect.height() / scale - widget_rect.height()) / 2

            # Move the origin to the center of the page
            painter.translate(x_translation, y_translation)

            self.render(painter)

            painter.end()

            self.displayForm.pushButton_print.show()
            self.displayForm.pushButton_2.show()

            print("PDF saved successfully!")