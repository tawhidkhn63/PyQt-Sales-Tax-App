import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from sales_gui import Ui_MainWindow as Ui_MainWindow #loading gui file


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_tax_button.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = 0
        try:
            price = int(self.pricebox.toPlainText())  # textbox is read in
        except Exception:
            print('sorry, please enter a number')
        tax = (self.taxrate.value())  # value reads from spinbox
        total_price = price + ((tax / 100) * price)
        total_price_string = "The total price with tax is: " + str(total_price)
        self.results.setText(total_price_string) #setting text in the results box


if __name__ == "__main__":    # new gui app is created and it can take in arguments argv. class myapp inherits qt libariers
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


