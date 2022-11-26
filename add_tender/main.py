import sys
import sqlite3
import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem, QListWidgetItem, QHeaderView
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5 import QtCore, uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('main_window.ui', self)
        self.setWindowTitle('Добавить тендер')
        self.ok_button.clicked.connect(self.submit_data)
        self.tenders_db_con = sqlite3.connect("../data/tenders_db.db")
    
    def validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%d.%m.%Y')
        except ValueError:
            return False
        else:
            return True
    
    def validate_weights(self, weights_text):
        w_list = weights_text.split(', ')
        print(w_list)
        return all([i.isdigit() for i in w_list])
    
    def submit_data(self):
        name = self.name_line.text()
        description = self.description_line.toPlainText()
        short_description = self.short_description_line.text()
        exp_date = self.exp_date_line.text()
        weights = self.weights_line.text()
        # print(self.validate_date(exp_date))
        # print(self.validate_weights(weights))
        if self.validate_date(exp_date) and self.validate_weights(weights):
            # print(exp_date, '\n', weights)
            cur = self.tenders_db_con.cursor()
            que = ''' INSERT INTO tenders_table(name,description,short_description,exp_date,weights)
                  VALUES(?,?,?,?,?) '''
            cur = self.tenders_db_con.cursor()
            cur.execute(que, (name, description, short_description, exp_date, weights))
            self.tenders_db_con.commit()


def main():
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()