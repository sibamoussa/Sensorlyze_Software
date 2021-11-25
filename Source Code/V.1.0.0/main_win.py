#This script includes the functions for the main window setup

from import_modules import*
import os, sys

#
# def resource_path(relative_path):
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.abspath("."), relative_path)
#

##################### Main Window Formatting ############################
def initUI(self):
    # Initialize
    # setGeometry(left, top, width, height)
    #to center the window
    screen = QDesktopWidget().screenGeometry()
    size = self.geometry()
    self.setGeometry((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2, 800, 500)

    self.setWindowTitle('Sensorlyze')
    self.setWindowIcon(QIcon('icon.jpg'))
    icon = QIcon(('icon.jpg'))

    # Add Labels
    label_1= QLabel("Welcome to Sensorlyze" ,self)
    label_1.move(25, 100)
    label_1.setFont(QFont('Calibri' ,15))
    label_1.adjustSize()
    label_2 = QLabel("A software to simplify sensor analytics", self)
    label_2.move(80, 200)
    label_2.setFont(QFont('Calibri', 10))
    label_2.adjustSize()
    # Add Menu Bar
    menubar_1 = self.menuBar()

    about_menu =menubar_1.addMenu('About')

    help_menu =menubar_1.addMenu('Help')

    # Add more options to the Help Button
    info_menu = QAction('Info', self)
    contact_menu = QAction('Contact', self)
    # set shortcut
    info_menu.setShortcut('Ctrl+I')
    contact_menu.setShortcut('Ctrl+E')
    help_menu.addAction(info_menu)
    help_menu.addAction(contact_menu)
    # Trigger Events
    # Create a function with a dialog box
    info_menu.triggered.connect(self.information)
    # Create a function with a dialog box
    contact_menu.triggered.connect(self.contact)

    # Add Buttons
    button_1 = QPushButton('Start',self)
    button_1.resize(button_1.sizeHint())
    button_1.clicked.connect(self.start_clicked)
    button_1.move(60, 250)
    button_2 = QPushButton('Exit', self)
    button_2.resize(button_2.sizeHint())
    button_2.clicked.connect(self.exit_clicked)
    button_2.move(240, 250)

def information(self):
    msgBox = QMessageBox()
    msgBox.setText(" This program is free software targeted at treating sensor data.")
    msgBox.setWindowTitle("Info")
    returnValue = msgBox.exec()
def contact(self):
    msgBox = QMessageBox()
    msgBox.setText(" wwww.bioelectrochemistry.ca")
    msgBox.setWindowTitle("Contact")
    returnValue = msgBox.exec()

def start_clicked(self):
    self.exp_selection_window()

# add Menu to the second window
def exp_selection_window(self):

    self.selectionlist = QComboBox()
    self.selectionlist.setGeometry(450, 450, 800, 35)
    exp_list = ["" ,"Single Sensor Calibration", "Multiple Sensor Calibration","Quantification","Data Visualization","Under Development"]
    self.selectionlist.addItems(exp_list)
    self.selectionlist.setWindowTitle('Select Experiment')

    self.selectionlist.setStyleSheet("QComboBox"
                          "{"
                          "border : 3px solid grey;"
                          " background-color: grey;"
                          "}")

    self.selectionlist.setWindowIcon(QIcon('icon.jpg'))
    self.selectionlist.show()
    self.selectionlist.activated[int].connect(self.exp_selection)
    self.selectionlist.activated[int].connect(self.windows)

def exp_selection(self):
    self.text =self.selectionlist.currentText()

def exit_clicked(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to exit?")
        msgBox.setWindowTitle("Exit Sensorlyze")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.msgButtonClick)
        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Ok:
            exit()
