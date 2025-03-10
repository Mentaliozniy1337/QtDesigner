import random
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 533)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #0D1B2A;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 360, 191, 101))
        self.pushButton.setStyleSheet("QPushButton { background-color: #1B263B; color: #E0E1DD; border: 2px solid #415A77; border-radius: 8px; padding: 8px; } QPushButton:hover { background-color: #415A77; } QPushButton:pressed { background-color: #778DA9; }")
        self.pushButton.setObjectName("pushButton")
        
        self.checkBox_digits = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_digits.setGeometry(QtCore.QRect(270, 290, 191, 21))
        self.checkBox_digits.setStyleSheet("QCheckBox { font-size: 14px; color: #E0E1DD; }")
        self.checkBox_digits.setObjectName("checkBox_digits")
        
        self.checkBox_letters = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_letters.setGeometry(QtCore.QRect(270, 260, 191, 21))
        self.checkBox_letters.setStyleSheet("QCheckBox { font-size: 14px; color: #E0E1DD; }")
        self.checkBox_letters.setObjectName("checkBox_letters")
        
        self.checkBox_symbols = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_symbols.setGeometry(QtCore.QRect(270, 316, 191, 21))
        self.checkBox_symbols.setStyleSheet("QCheckBox { font-size: 14px; color: #E0E1DD; }")
        self.checkBox_symbols.setObjectName("checkBox_symbols")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, -10, 181, 71))
        self.label.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; color: #E0E1DD; }")
        self.label.setObjectName("label")
        
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(200, 150, 300, 31))
        self.label_result.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; color: #E0E1DD; }")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.generate_password)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор паролей"))
        self.pushButton.setText(_translate("MainWindow", "Сгенерировать"))
        self.checkBox_digits.setText(_translate("MainWindow", "Числа"))
        self.checkBox_letters.setText(_translate("MainWindow", "Буквы"))
        self.checkBox_symbols.setText(_translate("MainWindow", "Символы"))
        self.label.setText(_translate("MainWindow", "Генератор паролей"))
        self.label_result.setText(_translate("MainWindow", "Результат"))
    
    def generate_password(self):
        characters = ""
        if self.checkBox_letters.isChecked():
            characters += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.checkBox_digits.isChecked():
            characters += "0123456789"
        if self.checkBox_symbols.isChecked():
            characters += "!@#$%^&*()_+-=[]{}|;:,.<>?/"
        
        if not characters:
            self.label_result.setText("Выберите параметры!")
            return
        
        password = "".join(random.choice(characters) for _ in range(12))
        self.label_result.setText(password)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()