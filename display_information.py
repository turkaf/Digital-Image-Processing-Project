from PyQt5.QtWidgets import *
from display_information_python import Ui_Form
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPainter, QPageSize

class DisplayInfoPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.displayForm = Ui_Form()
        self.displayForm.setupUi(self)
        self.displayForm.pushButton_print.clicked.connect(self.print_pdf)

    
    def print_pdf(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if filename:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(filename)

            page_size = QPageSize(QPageSize.A4)
            printer.setPageSize(page_size)

            painter = QPainter(printer)

            page_rect = printer.pageRect()

            painter.setViewport(0, 0, page_rect.width(), page_rect.height())

            self.displayForm.pushButton_print.hide()
            self.displayForm.pushButton_2.hide()

            painter.setWindow(0, 0, page_rect.width(), page_rect.height())

            widget_rect = self.rect()

            scale = min(page_rect.width() / widget_rect.width(), page_rect.height() / widget_rect.height())
            painter.scale(scale, scale)

            x_translation = (page_rect.width() / scale - widget_rect.width()) / 2
            y_translation = (page_rect.height() / scale - widget_rect.height()) / 2

            painter.translate(x_translation, y_translation)

            self.render(painter)

            painter.end()

            self.displayForm.pushButton_print.show()
            self.displayForm.pushButton_2.show()

            print("PDF saved successfully!")