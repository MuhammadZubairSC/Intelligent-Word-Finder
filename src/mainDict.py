from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPixmap
import sys,os
from dictpro import Dictionary_


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        
        #load the ui file
        uic.loadUi("dictp.ui", self)
        
        #define our widgets
        self.output=''
        self.search = self.findChild(QPushButton, "SearchBox")
        self.exit = self.findChild(QPushButton, "Exit")
        self.word = self.findChild(QLineEdit, "DictWord")
        self.answer = self.findChild(QLabel, "DictAnswer")
        self.picture = self.findChild(QLabel, "image")
        
        #Function of the widget when clicked
        self.search.clicked.connect(self.dictionary)
        self.exit.clicked.connect(lambda:self.close())

        #show the appe
        filename = "bg.jpg"

        #Open the image
        self.pixmap = QPixmap(filename)
        #Add Pic to the Label
        self.picture.setPixmap(self.pixmap)
        self.show()
        
    def dictionary(self):

        if self.output != '':
            a=self.output
        else:
            a=self.word.text()
        dic=Dictionary_()
        self.output =dic.translate(a)
        var=''
        if type(self.output) == list:
            var='\n'.join(self.output[0:4])
            self.output=''
            self.answer.setText(var)
        elif "Did" in self.output:
            msg = QMessageBox()
            msg.setWindowTitle("Suggestions")
            msg.setText(self.output)
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setDefaultButton(QMessageBox.Yes)
            msg.buttonClicked.connect(self.YNconnect)
            x = msg.exec_()
        else:
            self.answer.setText('')
            msg = QMessageBox()
            msg.setWindowTitle("Information")
            msg.setText(self.output)
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            self.output=''

            
    def YNconnect(self, i):
        if "Yes" in i.text():
            self.output=self.output.replace("Did you mean ", '')
            self.output=self.output.replace(" instead?", '')
            self.word.setText(self.output)
            self.dictionary()
        elif "No" in i.text():
            self.output=''
            self.word.setText("Type your word here!")
            self.answer.setText("The word doesn't exist. Please double check it.")
        else:
            self.answer.setText("We didn't understand your entry.")
            


app = QApplication(sys.argv)
UIWindow = MainWindow()
UIWindow.setWindowTitle("Intelligent Word Finder")
app.exec_()