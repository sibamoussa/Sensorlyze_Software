from import_modules import*

##################### Main Window Formatting ############################
def initUI(self):
    # Initialize
    self.setGeometry(1000, 300, 1200, 800)
    self.setWindowTitle('Sensorlyze')
    self.setWindowIcon(QIcon('biosensor.jpg'))
    icon = QIcon('biosensor.jpg')

    # Add Labels
    label_1= QLabel("Welcome to SensorLyze" ,self)
    label_1.move(25, 350)
    label_1.setFont(QFont('Calibri' ,15))
    label_1.adjustSize()
    label_2 = QLabel("A software to simplify sensor analytics", self)
    label_2.move(25, 400)
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
    button_1.move(60, 450)
    button_2 = QPushButton('Exit', self)
    button_2.resize(button_2.sizeHint())
    button_2.clicked.connect(self.exit_clicked)
    button_2.move(240, 450)

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
    self.setWindowIcon(QIcon('biosensor.jpg'))
    icon = QIcon('biosensor.jpg')
    self.selectionlist = QComboBox()
    self.selectionlist.setGeometry(1300, 700, 800, 50)
    exp_list = ["" ,"Single Sensor Calibration", "Multiple Sensor Calibration","Quantification","Data Visualization","Under Development"]
   # exp_list = ["" ,"Single Sensor Calibration", "Multiple Sensor Calibration", "Quantification",""Roughness", "Highthroughput","Under Development"]
    self.selectionlist.addItems(exp_list)
    self.selectionlist.setWindowTitle('Select Experiment')

    self.selectionlist.setStyleSheet("QComboBox"
                          "{"
                          "border : 3px solid grey;"
                          " background-color: grey;"
                          "}")
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
