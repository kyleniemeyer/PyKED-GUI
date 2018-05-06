# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WelcomeScreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        MainWindow.setMinimumSize(QtCore.QSize(650, 400))
        MainWindow.setMaximumSize(QtCore.QSize(650, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../PyKED-Master/logo/pyked-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setEnabled(True)
        self.mainWidget.setObjectName("mainWidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 661, 401))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.backButton1 = QtWidgets.QPushButton(self.page1)        
        self.backButton1.setEnabled(False)
        self.backButton1.setGeometry(QtCore.QRect(410, 350, 93, 28))
        self.backButton1.setObjectName("backButton1")
        self.nextButton1 = QtWidgets.QPushButton(self.page1)
        self.nextButton1.setGeometry(QtCore.QRect(520, 350, 93, 28))
        self.nextButton1.setObjectName("nextButton1")
        self.textEdit = QtWidgets.QTextEdit(self.page1)
        self.textEdit.setGeometry(QtCore.QRect(60, 130, 391, 51))
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.backButton2 = QtWidgets.QPushButton(self.page2)
        self.backButton2.setGeometry(QtCore.QRect(410, 350, 93, 28))
        self.backButton2.setObjectName("backButton2")
        self.nextButton2 = QtWidgets.QPushButton(self.page2)
        self.nextButton2.setGeometry(QtCore.QRect(520, 350, 93, 28))
        self.nextButton2.setObjectName("nextButton2")
        self.label = QtWidgets.QLabel(self.page2)
        self.label.setGeometry(QtCore.QRect(90, 70, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page2)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page2)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 71, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.page2)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page2)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page2)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 130, 113, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.page2)
        self.textEdit_3.setGeometry(QtCore.QRect(120, 230, 391, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.stackedWidget.addWidget(self.page2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.backButton2_2 = QtWidgets.QPushButton(self.page_3)
        self.backButton2_2.setGeometry(QtCore.QRect(410, 340, 93, 28))
        self.backButton2_2.setObjectName("backButton2_2")
        self.nextButton2_2 = QtWidgets.QPushButton(self.page_3)
        self.nextButton2_2.setGeometry(QtCore.QRect(520, 340, 93, 28))
        self.nextButton2_2.setObjectName("nextButton2_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.page_3)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 150, 391, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Welcome to PyKED"))
        self.backButton1.setText(_translate("MainWindow", "Back"))
        self.nextButton1.setText(_translate("MainWindow", "Next"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to PyKED. This dialog will prompt you to enter important information in order to correctly log calculated data.</p></body></html>"))
        self.backButton2.setText(_translate("MainWindow", "Back"))
        self.nextButton2.setText(_translate("MainWindow", "Finish"))
        self.label.setText(_translate("MainWindow", "Author"))
        self.label_2.setText(_translate("MainWindow", "ORCID"))
        self.label_3.setText(_translate("MainWindow", "File Version"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click the finish button to save the previously entered information.</p></body></html>"))
        self.backButton2_2.setText(_translate("MainWindow", "Back"))
        self.nextButton2_2.setText(_translate("MainWindow", "Finish"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click the finish button to save the previously entered information.</p></body></html>"))

class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.nextButton1.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.backButton2.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.nextButton2.clicked.connect(self.SaveData)
        
        
    def SaveData(self):      
        
        global author
        global orcid
        global version  
        
        author = self.ui.lineEdit.text()
        orcid = self.ui.lineEdit_2.text()
        version = self.ui.lineEdit_3.text()
        
        self.WriteData()
        
        close()
        
        
    def WriteData(self):
            
        num = 4
        authors = ['john', 'bob', 'joe', 'mark']
        
        with open('DataWriteTest.yaml', 'a') as fileWrite:
            fileWrite.write('---\n')
            fileWrite.write('file-authors:\n')
            fileWrite.write('  - name: ' + author + '\n')
            fileWrite.write('    ORCID: ' + orcid + '\n')
            fileWrite.write('file-version: ' + version + '\n')
            fileWrite.write('chemked-version: varHere\n')
            fileWrite.write('reference:\n')
            fileWrite.write('  doi: varHere\n')
            fileWrite.write('  authors:\n')
            
            # set the number of authors to record here
            x = 0
            while x < num:    
                fileWrite.write('    - name: ')
                fileWrite.write(authors[x])
                fileWrite.write('\n')
                x = x + 1
            fileWrite.write('  journal: varHere\n')
            fileWrite.write('  year: varHere\n')
            fileWrite.write('  volume: varHere\n')
            fileWrite.write('  pages: varHere\n')
            fileWrite.write('  detail: varHere\n')
            
            # more file writing here



            

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())
    
    
    
    
    
