##This script includes the class responsible for the single sensor calibration curves

from import_modules import*

class single_cal():

    def open_file_single(self):
        global fileName,extension
        fileName = openFile(self)
        name, extension = os.path.splitext(fileName)
    def win_setup(self):
            self.window = QMainWindow()
            self.window.setWindowTitle('Single Sensor Calibration')
            screen = QDesktopWidget().screenGeometry()
            self.window.setGeometry(0, 0, screen.width() - 50, screen.height() - 50)
            self.window.setWindowIcon(QIcon('icon.jpg'))

            ######################## Setting up Tabs ##########################
            self.window.tabWidget = QTabWidget(self.window)
            self.window.tabWidget.resize(screen.width() - 100, screen.height() - 100)
            self.window.tab1 = QWidget(self.window)
            self.window.tab2 = QWidget(self.window)

            self.window.tabWidget.addTab(self.window.tab1, "Visualize Data")
            self.window.tabWidget.addTab(self.window.tab2, "Single Sensor Analytics")


            # Setting tab layouts
            self.window.tab1.layout = QGridLayout(self.window)
            self.window.tab2.layout = QGridLayout(self.window)

 ############ TAB1 #########
            import_statement = QLabel("Import a data file to visualize:")
            self.window.tab1.layout.addWidget(import_statement,0,0)
            import_statement.setAlignment(Qt.AlignRight)

            select_file_button = QPushButton("Select File")
            self.window.tab1.layout.addWidget(select_file_button,0,1)
            select_file_button.clicked.connect(self.open_file_single)
            plot_file_button = QPushButton("Plot File")
            self.window.tab1.layout.addWidget(plot_file_button,2,0)
            plot_file_button.clicked.connect(self.plot_file_single)
            save_plot_button = QPushButton("Save Plot")
            self.window.tab1.layout.addWidget(save_plot_button,2,2)
            save_plot_button.clicked.connect(self.save_plt_single)
            clear_plot_button = QPushButton('Clear Plot')
            self.window.tab1.layout.addWidget(clear_plot_button,2,1)
            clear_plot_button.clicked.connect(self.clr_plt_single)

            # Selecting File Type
            manufacturer_label = QLabel('Select Manufacturer & File Type:')
            self.window.tab1.layout.addWidget(manufacturer_label,1,0)
            manufacturer_label.setAlignment(Qt.AlignRight)

            filelist = QComboBox(self.window)
            filetype_list = ["", "HEKA (.asc)", "Biologic (.txt)", "CH (.txt)","Excel (.xlsx)"]

            filelist.addItems(filetype_list)
            self.window.tab1.layout.addWidget(filelist, 1, 1)

            self.windowcal = QMainWindow()
            self.windowcal.setWindowTitle('Single Sensor Calibration')
            screen = QDesktopWidget().screenGeometry()
            self.windowcal.setGeometry(0, 0, screen.width() - 500, screen.height() - 50)
            self.windowcal.setWindowIcon(QIcon('biosensor2.jpg'))
            self.windowcal.tabWidget = QTabWidget(self.windowcal)
            self.windowcal.tabWidget.resize(screen.width() - 600, screen.height() - 100)
            self.windowcal.tab1 = QWidget(self.windowcal)
            self.windowcal.tab1.layout = QGridLayout(self.windowcal)
            self.windowcal.tab1.setLayout(self.windowcal.tab1.layout)
            self.windowcal.tab2 = QWidget(self.windowcal)
            self.windowcal.tab2.layout = QGridLayout(self.windowcal)
            self.windowcal.tab2.setLayout(self.windowcal.tab2.layout)

            self.windowcal.tabWidget.addTab(self.windowcal.tab1, "Calibration Curve")
            self.windowcal.tabWidget.addTab(self.windowcal.tab2, "Normalized Calibration Curve")


            def filelist_selections(self):
                global df
                filetype_selection = filelist.currentText()
                if filetype_selection == "HEKA (.asc)":
                    if extension == '.asc':
                        df = pd.read_fwf(fileName, skiprows=2, delimited='/t')
                        print(df)
                        df = df[['"Time[s]"', '"Imon-1[A]"']]
                        df = df.dropna()
                        print(df)
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Please chose file with .asc extension")
                        msg.setWindowTitle("Error")
                        returnValue = msg.exec()

                elif filetype_selection == 'Biologic (.txt)':
                    if extension == '.txt':
                        df = pd.read_csv(fileName, sep='\t', skiprows=56)
                        df = df.dropna()
                        df = df.filter(regex='ime|I')
                        colname = df.columns[1]
                        df_round_time = df.iloc[:, 0]
                        df_round_time = df_round_time.round(decimals=2)
                        df.iloc[:, 0] = df_round_time
                        if 'mA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -3
                        elif 'uA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -6
                        elif 'pA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -9
                        elif 'A' in colname:
                            pass
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error processing current values")
                            msg.setWindowTitle("Error")
                            returnValue = msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Please chose file with .txt extension")
                        msg.setWindowTitle("Error")
                        returnValue = msg.exec()

                elif filetype_selection == 'CH (.txt)':
                    if extension == '.txt':
                        df = pd.read_csv(fileName, sep=r'\,|\t', skiprows=18,engine='python')
                        df = df.dropna().astype(float)
                        df = df.filter(regex='ime|Curr')
                        colname = df.columns[1]
                        df_round_time = df.iloc[:, 0]
                        df_round_time = df_round_time.round(decimals=2)
                        df.iloc[:, 0] = df_round_time
                        if 'mA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -3
                        elif 'uA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -6
                        elif 'pA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -9
                        elif 'A' in colname:
                            pass
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error processing current values")
                            msg.setWindowTitle("Error")
                            returnValue = msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Please chose file with .txt extension")
                        msg.setWindowTitle("Error")
                        returnValue = msg.exec()

                elif filetype_selection == 'Excel (.xlsx)':
                    if extension == '.xlsx':
                        df = pd.read_excel(fileName)
                        df = df.dropna()
                        df = df.filter(regex='ime|I')
                        colname = df.columns[1]
                        df_round_time = df.iloc[:, 0]
                        df_round_time = df_round_time.round(decimals=2)
                        df.iloc[:, 0] = df_round_time
                        if 'mA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -3
                        elif 'uA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -6
                        elif 'pA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -9
                        elif 'A' in colname:
                            pass
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error processing current values")
                            msg.setWindowTitle("Error")
                            returnValue = msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Please chose file with .xslx extension")
                        msg.setWindowTitle("Error")
                        returnValue = msg.exec()
                else:
                    pass
                df = df.values
                print(df)

            filelist.activated[int].connect(filelist_selections)
            #PlaceHolder
            placehold = QLabel(' ')
            self.window.tab1.layout.addWidget(placehold,4,0,8,3)

############ TAB2 #########
            import_statement = QLabel("Import a data file to visualize:")
            self.window.tab2.layout.addWidget(import_statement, 0, 0)
            import_statement.setAlignment(Qt.AlignRight)
            select_file_button = QPushButton("Select File")
            self.window.tab2.layout.addWidget(select_file_button, 0, 1)
            select_file_button.clicked.connect(self.open_file_single)
            plot_file_button = QPushButton("Plot File")
            self.window.tab2.layout.addWidget(plot_file_button,2,0)
            plot_file_button.clicked.connect(self.plot_file_single_tab2)
            global noise_filter_button
            noise_filter_button = QCheckBox("Apply Noise-Reduction Filter?", self.window)
            self.window.tab2.layout.addWidget(noise_filter_button,2,1)
            noise_filter_button.stateChanged.connect(self.apply_filter_single)

            global select_points_button
            select_points_button = QCheckBox("Select Points?", self.window)
            self.window.tab2.layout.addWidget(select_points_button, 3, 1)
            select_points_button.stateChanged.connect(self.sel_pts_single)

            def normalize_currents(self):
                global normalized_currents
                normalized_currents=[]
                currentvals = np.array(currents)
                normalized_currents = currentvals[:] - currentvals[0]

            #Input Concentrations
            input_conc_widget = QLabel("Please input all concentrations with a space in between: ", self.window)
            self.window.tab2.layout.addWidget(input_conc_widget,0,2)
            input_conc_text = QLineEdit(self.window)
            self.window.tab2.layout.addWidget(input_conc_text,0,3)

            def conc_values(self):
                global concs_values
                concs_values = np.array([int(float(i)) for i in input_conc_text.text().split()])
                concs_values = np.array([float(i) for i in input_conc_text.text().split()])

                print(concs_values)

            done_selection_button = QPushButton('Done', self.window)
            self.window.tab2.layout.addWidget(done_selection_button,0,4)
            done_selection_button.clicked.connect(conc_values)


            export_data_button = QPushButton('Export Data', self.window)
            self.window.tab2.layout.addWidget(export_data_button, 1, 2)
            export_data_button.clicked.connect(self.export_plot_single)
            ## Add the regression statistics
            global regress_data_button
            regress_data_button = QCheckBox('Regress Data?', self.window)
            self.window.tab2.layout.addWidget(regress_data_button,2,2)
            regress_data_button.stateChanged.connect(self.regress_data)

            ###Plot Calibration
            plot_calib_button = QPushButton('Plot Calibration', self.window)
            self.window.tab2.layout.addWidget(plot_calib_button,3,2)
            plot_calib_button.clicked.connect(self.plot_cal_single)

            save_plot_button = QPushButton('Save Plot', self.window)
            self.window.tab2.layout.addWidget(save_plot_button, 1, 3)
            save_plot_button.clicked.connect(self.save_plt_single)

            #Normalize Calibration
            global normalize_data_button
            normalize_data_button = QCheckBox("Normalize Plot?", self.window)
            self.window.tab2.layout.addWidget(normalize_data_button, 2, 3)

            normalize_data_button.stateChanged.connect(normalize_currents)
            plot_normalizedcal_button = QPushButton('Plot Normalized Calibration', self.window)
            self.window.tab2.layout.addWidget(plot_normalizedcal_button,3,3)
            plot_normalizedcal_button.clicked.connect(self.plot_normal_cal_single)

            clear_plot_button = QPushButton('Clear Plot', self.window)
            self.window.tab2.layout.addWidget(clear_plot_button, 1, 4)
            clear_plot_button.clicked.connect(self.clr_plt_single)

            manufacturer_label = QLabel('Select Manufacturer & File Type:')
            self.window.tab2.layout.addWidget(manufacturer_label,1,0)
            manufacturer_label.setAlignment(Qt.AlignRight)

            filelist2 = QComboBox(self.window)
            filelist2.addItems(filetype_list)
            self.window.tab2.layout.addWidget(filelist2,1, 1)

            def filelist_selections_tab2(self):
                global df
                filetype_selection = filelist2.currentText()
                if filetype_selection == "HEKA (.asc)":
                    if extension == '.asc':
                        df = pd.read_fwf(fileName, skiprows=2, delimited='/t')
                        df = df[['"Time[s]"', '"Imon-1[A]"']]
                        df = df.dropna()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Please chose file with .asc extension")
                        msg.setWindowTitle("Error")
                        returnValue = msg.exec()

                elif filetype_selection == 'Biologic (.txt)':
                    if extension == '.txt':
                        df = pd.read_csv(fileName, sep='\t', skiprows=56)
                        df = df.dropna()
                        df = df.filter(regex='ime|I')
                        colname = df.columns[1]
                        df_round_time = df.iloc[:, 0]
                        df_round_time = df_round_time.round(decimals=2)
                        df.iloc[:, 0] = df_round_time
                        if 'mA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -3
                        elif 'uA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -6
                        elif 'pA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -9
                        elif 'A' in colname:
                            pass
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error processing current values")
                            msg.setWindowTitle("Error")
                            returnValue = msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Please chose file with .txt extension")
                        msg.setWindowTitle("Error")
                        returnValue = msg.exec()
                elif filetype_selection == 'CH (.txt)':
                    if extension == '.txt':
                        df = pd.read_csv(fileName, sep=r'\,|\t', skiprows=18, engine='python')
                        df = df.dropna().astype(float)
                        df = df.filter(regex='ime|Curr')
                        colname = df.columns[1]
                        df_round_time = df.iloc[:, 0]
                        df_round_time = df_round_time.round(decimals=2)
                        df.iloc[:, 0] = df_round_time
                        if 'mA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -3
                        elif 'uA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -6
                        elif 'pA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -9
                        elif 'A' in colname:
                            pass
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error processing current values")
                            msg.setWindowTitle("Error")
                            returnValue = msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Please chose file with .txt extension")
                        msg.setWindowTitle("Error")
                        returnValue = msg.exec()
                elif filetype_selection == 'Excel (.xlsx)':
                    if extension == '.xlsx':
                        df = pd.read_excel(fileName)
                        df = df.dropna()
                        df = df.filter(regex='ime|I')
                        colname = df.columns[1]
                        df_round_time = df.iloc[:, 0]
                        df_round_time = df_round_time.round(decimals=2)
                        df.iloc[:, 0] = df_round_time
                        if 'mA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -3
                        elif 'uA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -6
                        elif 'pA' in colname:
                            df.iloc[:, 1] = df.iloc[:, 1] * 10 ** -9
                        elif 'A' in colname:
                            pass
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error processing current values")
                            msg.setWindowTitle("Error")
                            returnValue = msg.exec()
                    else:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Please chose file with .xslx extension")
                        msg.setWindowTitle("Error")
                        returnValue = msg.exec()
                else:
                    pass
                df = df.values

            filelist2.activated[int].connect(filelist_selections_tab2)
            #placeholder
            placehold = QLabel(' ')
            self.window.tab2.layout.addWidget(placehold,5, 0, 8, 4)

###Display all tabs
            self.window.tab1.setLayout(self.window.tab1.layout)
            self.window.tab2.setLayout(self.window.tab2.layout)
            self.window.show()

    ######################## BASIC FILE VISUALIZATION ##########################

    def plot_file_single(self):
        font = QFont()
        penn= pg.mkPen(color='k', width=2)
        font.setBold(False)
        font.setPixelSize(30)
        global graphWidget
        graphWidget = pg.PlotWidget(self.window)
        graphWidget.getAxis('bottom').setTextPen(penn)
        graphWidget.getAxis('left').setTextPen(penn)
        graphWidget.getAxis('bottom').setTickFont(font)
        graphWidget.getAxis('left').setTickFont(font)
        graphWidget.getAxis('bottom').setStyle(tickTextOffset=10)
        graphWidget.getAxis('left').setStyle(tickTextOffset=10,autoExpandTextSpace=True)
        graphWidget.getAxis('left').setPen(penn)
        graphWidget.getAxis('bottom').setPen(penn)
        pen = pg.mkPen(color=(147,112,219),width=3)
        graphWidget.plot(df[:,0], df[:,1],pen=pen)

        ##Setting x-tick spacing
        spacing=8

        xmax=max(df[:,0])
        xmin=min(df[:,0])
        x_values=np.arange(xmin,xmax,xmax/spacing)
        print(x_values)
        x_values=np.round(x_values)
        x_values=[int(x_value) for x_value in x_values]
        dx = [(x_value, str(x_value)) for x_value in x_values]
        x_ax = graphWidget.getAxis('bottom')  # This is the trick
        x_ax.setTicks([dx, []])

        styles = {'color': 'k', 'font-size': '30px','font-weight':'bold','font-type':'arial'}
        graphWidget.setLabel('left', 'Current / A', **styles)
        graphWidget.setLabel('bottom', 'Time / s', **styles)
        graphWidget.setBackground('w')

        graphWidget.show()
        self.window.tab1.layout.addWidget(graphWidget,4,0,8,3)

    def clr_plt_single(self):
        graphWidget.clear()

    def save_plt_single(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(graphWidget, "Save File", "",
                                           "All Files (*);; PNG (*.png);;TIFF (*.tiff)", options=options)
        exporter = pg.exporters.ImageExporter(graphWidget.plotItem)
        # exporter.parameters()['width'] = 6
        # exporter.parameters()['height'] = 6
        exporter.export(file[0])

###################################### SINGLE SENSOR DATA ANALYSIS  ##########################
    def plot_file_single_tab2(self):

        font = QFont()
        penn = pg.mkPen(color='k', width=2)
        font.setBold(False)
        font.setPixelSize(30)
        global graphWidget
        graphWidget = pg.PlotWidget(self.window)
        graphWidget.getAxis('bottom').setTextPen(penn)
        graphWidget.getAxis('left').setTextPen(penn)
        graphWidget.getAxis('bottom').setTickFont(font)
        graphWidget.getAxis('left').setTickFont(font)
        graphWidget.getAxis('bottom').setStyle(tickTextOffset=10)
        graphWidget.getAxis('left').setStyle(tickTextOffset=10, autoExpandTextSpace=True)
        graphWidget.getAxis('left').setPen(penn)
        graphWidget.getAxis('bottom').setPen(penn)
        pen = pg.mkPen(color=(147, 112, 219), width=3)
        graphWidget.plot(df[:, 0], df[:, 1], pen=pen)

        ##Setting x-tick spacing
        spacing = 8
        xmax = max(df[:, 0])
        xmin = min(df[:, 0])
        x_values = np.arange(xmin, xmax, xmax / spacing)
        print(x_values)
        x_values = np.round(x_values)
        x_values = [int(x_value) for x_value in x_values]
        dx = [(x_value, str(x_value)) for x_value in x_values]
        x_ax = graphWidget.getAxis('bottom')  # This is the trick
        x_ax.setTicks([dx, []])
        #set style
        styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold', 'font-type': 'arial'}
        graphWidget.setLabel('left', 'Current / A', **styles)
        graphWidget.setLabel('bottom', 'Time / s', **styles)
        graphWidget.setBackground('w')


        # # check this
        global currents, df_raw
        headers = ["Time (s)", "Current (A)"]
        df_raw =pd.DataFrame(df,columns=headers)
        currents = []
        graphWidget.show()
        self.window.tab2.layout.addWidget(graphWidget, 4, 0, 8, 4)

    def apply_filter_single(self, state):
        if noise_filter_button.isChecked():
            global graphWidget2
            smooth_1dg = savgol_filter(df[:, 1], window_length=5, polyorder=1)
            df[:, 1] = smooth_1dg
            font = QFont()
            penn = pg.mkPen(color='k', width=2)
            font.setBold(False)
            font.setPixelSize(30)
            graphWidget2 = pg.PlotWidget(self.window)
            graphWidget2.getAxis('bottom').setTextPen(penn)
            graphWidget2.getAxis('left').setTextPen(penn)
            graphWidget2.getAxis('bottom').setTickFont(font)
            graphWidget2.getAxis('left').setTickFont(font)
            graphWidget2.getAxis('bottom').setStyle(tickTextOffset=10)
            graphWidget2.getAxis('left').setStyle(tickTextOffset=10, autoExpandTextSpace=True)
            pen = pg.mkPen(color=(100, 200, 100),width=2)
            graphWidget2.plot(df[:, 0], df[:, 1], pen=pen)
            ##Setting x-tick spacing
            spacing = 8
            xmax = max(df[:, 0])
            xmin = min(df[:, 0])
            x_values = np.arange(xmin, xmax, xmax / spacing)
            print(x_values)
            x_values = np.round(x_values)
            x_values = [int(x_value) for x_value in x_values]
            dx = [(x_value, str(x_value)) for x_value in x_values]
            x_ax = graphWidget2.getAxis('bottom')  # This is the trick
            x_ax.setTicks([dx, []])

            ##Styles
            styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold', 'font-type': 'arial'}
            graphWidget2.setLabel('left', 'Current / A', **styles)
            graphWidget2.setLabel('bottom', 'Time /s', **styles)
            graphWidget2.setBackground('w')
            graphWidget2.setTitle('Noise Filtered', **styles)
            graphWidget2.show()

            self.window.tab2.layout.addWidget(graphWidget2, 4, 0, 8, 4)

        else:
            graphWidget2.deleteLater()

    def sel_pts_single(self):
        if select_points_button.isChecked():
            global lr
            lr = pg.LinearRegionItem(values=(0, 30), orientation=pg.LinearRegionItem.Vertical)
            lr.lines[0].label = InfLineLabel(lr.lines[0], text="{value:0.3f}")
            lr.lines[1].label = InfLineLabel(lr.lines[1], text="{value:0.3f}")
            if noise_filter_button.isChecked() and select_points_button.isChecked():
                graphWidget2.addItem(lr)
                def update_region(self):
                    region =np.array(lr.getRegion())
                    region = np.round(region, decimals=2)
                    df2 = np.array(df)
                    yminindex = np.where(df2[:, 0] == region[0])
                    ymaxindex = np.where(df2[:, 0] == region[1])
                    # finding the current
                    yminloc = np.array(yminindex)
                    yminloc = np.concatenate(yminloc)
                    yminloc = yminloc[0]
                    ymaxloc = np.array(ymaxindex)
                    ymaxloc = np.concatenate(ymaxloc)
                    ymaxloc = ymaxloc[0]
                    points = df[yminloc:ymaxloc, 1]
                    selection_avg = mean(points)
                    currents.append(selection_avg)
                lr.sigRegionChangeFinished.connect(update_region)

            elif noise_filter_button.isChecked() == False and select_points_button.isChecked():
                graphWidget.addItem(lr)

                def update_region(self):
                    region = np.array(lr.getRegion())
                    region = np.round(region, decimals=2)
                    df2 = np.array(df)

                    yminindex = np.where(df2[:, 0] == region[0])
                    ymaxindex = np.where(df2[:, 0] == region[1])

                    # finding the current
                    yminloc = np.array(yminindex)
                    yminloc = np.concatenate(yminloc)
                    yminloc = yminloc[0]
                    ymaxloc = np.array(ymaxindex)
                    ymaxloc = np.concatenate(ymaxloc)
                    ymaxloc = ymaxloc[0]
                    points = df[yminloc:ymaxloc, 1]
                    selection_avg = mean(points)
                    currents.append(selection_avg)

                lr.sigRegionChangeFinished.connect(update_region)
            else:
                pass
        elif noise_filter_button.isChecked() and select_points_button.isChecked()==False:
            graphWidget2.removeItem(lr)
        else:
            graphWidget.removeItem(lr)

    def plot_cal_single(self):
        check_same_size=len(concs_values)==len(currents)

        self.windowcal.show()

        if (check_same_size):
            global graphWidgetCal
            font = QFont()
            tickcolor = pg.mkPen(color='k', width=2)
            font.setBold(False)
            font.setPixelSize(20)
            graphWidgetCal = pg.PlotWidget()
            scattercal = pg.ScatterPlotItem(size = 10, brush = pg.mkBrush('b'))
            graphWidgetCal.getAxis('left').setPen(tickcolor)
            graphWidgetCal.getAxis('bottom').setPen(tickcolor)
            graphWidgetCal.getAxis('left').setTextPen('k')
            graphWidgetCal.getAxis('bottom').setTextPen('k')
            graphWidgetCal.getAxis('left').setTickFont(font)
            graphWidgetCal.getAxis('bottom').setTickFont(font)
            graphWidgetCal.getAxis('bottom').setStyle(tickTextOffset=10)
            graphWidgetCal.getAxis('left').setStyle(tickTextOffset=5)

            scattercal.setData(concs_values,currents)
            graphWidgetCal.addItem(scattercal)

            global calib_data
            calib_data = pd.DataFrame({'Concentration (uM)': concs_values, 'Current (A)': currents})

            styles = {'color': 'k', 'font-size': '20px', 'font-weight': 'bold', 'font-type': 'arial'}
            graphWidgetCal.setTitle('Calibration Curve', **styles)
            graphWidgetCal.setLabel('left', 'i<sub>ss</sub> / A', **styles)
            graphWidgetCal.setLabel('bottom', 'Concentration / \u03BCM', **styles)
            graphWidgetCal.setBackground('w')
            self.windowcal.tab1.layout.addWidget(graphWidgetCal,0,0,3,3)

            #PlaceHolder
            placeholder = QLabel(' ')
            self.windowcal.tab1.layout.addWidget(placeholder, 0, 10, 3, 6)
            ## Add save and clear buttons
            save_plot_button = QPushButton('Save Plot', self.windowcal)
            self.windowcal.tab1.layout.addWidget(save_plot_button, 6, 0, 6, 3)

            save_plot_button.clicked.connect(self.save_cal_single)
            export_calib_button = QPushButton('Export Calibration', self.windowcal)
            self.windowcal.tab1.layout.addWidget(export_calib_button, 7, 0, 7, 3)

            export_calib_button.clicked.connect(self.export_cal_single)

            clear_calib_button = QPushButton('Clear Calibration Plot', self.windowcal)
            self.windowcal.tab1.layout.addWidget(clear_calib_button, 8, 0,8,3)
            clear_calib_button.clicked.connect(self.clear_calib_single)

    def plot_normal_cal_single(self):
        check_same_size = len(concs_values) == len(normalized_currents)

        self.windowcal.tabWidget.setCurrentIndex(1)

        if (check_same_size):
            if normalize_data_button.isChecked()==True:

                font = QFont()
                tickcolor = pg.mkPen(color='k', width=2)
                font.setBold(False)
                font.setPixelSize(20)
                global graphWidgetNormCal
                graphWidgetNormCal = pg.PlotWidget()
                scattercal = pg.ScatterPlotItem(size=10, brush=pg.mkBrush('b'))
                graphWidgetNormCal.getAxis('left').setPen(tickcolor)
                graphWidgetNormCal.getAxis('bottom').setPen(tickcolor)
                graphWidgetNormCal.getAxis('left').setTextPen('k')
                graphWidgetNormCal.getAxis('bottom').setTextPen('k')
                graphWidgetNormCal.getAxis('bottom').setTickFont(font)
                graphWidgetNormCal.getAxis('left').setTickFont(font)
                graphWidgetNormCal.getAxis('bottom').setStyle(tickTextOffset=10)
                graphWidgetNormCal.getAxis('left').setStyle(tickTextOffset=5)
                scattercal.setData(concs_values, normalized_currents)
                graphWidgetNormCal.addItem(scattercal)

                global normalized_calib_data
                normalized_calib_data = pd.DataFrame({'Concentration (uM)': concs_values, 'Current (A)': normalized_currents})  # df_new2[2]]

                styles = {'color': 'k', 'font-size': '20px', 'font-weight': 'bold', 'font-type': 'arial'}
                graphWidgetNormCal.setTitle('Normalized Calibration Curve', **styles)
                graphWidgetNormCal.setLabel('left', 'i<sub>norm</sub>  / A', **styles)
                graphWidgetNormCal.setLabel('bottom', 'Concentration / \u03BCM', **styles)
                graphWidgetNormCal.setBackground('w')
                graphWidgetNormCal.show()
                self.windowcal.tab2.layout.addWidget(graphWidgetNormCal,0,0,3,3)
                placeholder = QLabel(' ')
                self.windowcal.tab2.layout.addWidget(placeholder, 0, 3, 10, 6)

                #########
                ## Add export, save, and  clear buttons
                save_plot_button= QPushButton('Save Plot', self.window)
                self.windowcal.tab2.layout.addWidget(save_plot_button,5, 0, 5, 3)
                save_plot_button.clicked.connect(self.save_normal_plt_single)

                clear_calib_button = QPushButton('Clear Normalized Calibration', self.window)
                self.windowcal.tab2.layout.addWidget(clear_calib_button, 6, 0,6, 3)
                clear_calib_button.clicked.connect(self.clr_normal_plt_single)

                export_norm_calib_button = QPushButton('Export Normalized Calibration', self.window)
                self.windowcal.tab2.layout.addWidget(export_norm_calib_button,7,0,7,3)
                export_norm_calib_button.clicked.connect(self.export_normal_plt_single)

                export_alldata_button = QPushButton('Export all data', self.window)
                self.windowcal.tab2.layout.addWidget(export_alldata_button, 8, 0, 8, 3)
                export_alldata_button.clicked.connect(self.export_all_data_single)

               # placeholder2 = QLabel(' ')
              #  self.windowcal.tab2.layout.addWidget(placeholder2, 7, 0, 7, 3)
            else:
                msg = QMessageBox(self.window)
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error, Please normalize data first")
                msg.setWindowTitle("Error")
                returnValue = msg.exec()
        else:
            msg = QMessageBox(self.window)
            msg.setIcon(QMessageBox.Critical)
            msg.setText(
                "Error, Please make sure equal number of concentrations are listed for the number current selections")
            msg.setWindowTitle("Error")
            returnValue = msg.exec()
    def regress_data(self):
        if regress_data_button.isChecked():
            global regress_display,calib_summary,norm_calib_summary
            regress_display = QLineEdit(self.window)
            regress_display.setAlignment(Qt.AlignCenter)

            if normalize_data_button.isChecked()==True:
                concs = concs_values.reshape(-1, 1)
                normalized_currents_values = normalized_currents.reshape(-1, 1)
                lrfit = LinearRegression().fit(concs, normalized_currents_values.reshape((-1, 1)))
                normalized_currents_pred = lrfit.predict(concs)
                r_sq = lrfit.score(concs, normalized_currents_values)
                normalized_currents_pred = normalized_currents_pred.flatten()
                penn = pg.mkPen(color='k', width=2)
                graphWidgetNormCal.plot(concs_values, normalized_currents_pred,pen=penn)
                regr_slope = lrfit.coef_[0]
                rounded_slope = list(np.round(regr_slope, 3))
                regression_statssummary = [('R_squared:', round(r_sq, 3), 'Intercept:', round(lrfit.intercept_[0], 3),'Slope:', rounded_slope)]
                regression_statssummary_str = str([tuple(str(ele) for ele in sub) for sub in regression_statssummary])
                regression_statssummary_cleaned = regression_statssummary_str.replace("'", "").replace(",", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")

                norm_calib_summary = [r_sq, lrfit.intercept_[0], regr_slope]

                regress_display.setText(regression_statssummary_cleaned)
                self.windowcal.tab2.layout.addWidget(regress_display,3,0,3,3)

            elif normalize_data_button.isChecked()==False:
                currents2=np.array(currents)
                concs = concs_values.reshape(-1, 1)
                currents_vals = currents2.reshape(-1, 1)
                lrfit = LinearRegression().fit(concs, currents_vals.reshape((-1, 1)))
                current_pred = np.array(lrfit.predict(concs))
                current_pred = current_pred.flatten()
                print(current_pred)
                penn = pg.mkPen(color='k', width=2)
                graphWidgetCal.plot(concs_values, current_pred,pen=penn)
               # self.windowcal.tab1.layout.addWidget(linearreg,0,0,3,3)

                r_sq = lrfit.score(concs, currents_vals)
                regr_slope = lrfit.coef_[0]
                rounded_slope = list(np.round(regr_slope, 3))
                regression_statssummary = [('R_squared:', round(r_sq, 3), 'Intercept:', round(lrfit.intercept_[0], 3),'Slope:', rounded_slope)]
                regression_statssummary_str = str([tuple(str(ele) for ele in sub) for sub in regression_statssummary])
                regression_statssummary_cleaned = regression_statssummary_str.replace("'", "").replace(",", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "")

                calib_summary = [r_sq, lrfit.intercept_[0], regr_slope]

                regress_display.setText(regression_statssummary_cleaned)
                self.windowcal.tab1.layout.addWidget(regress_display,3,0,3,3)
            else:
                regress_display.deleteLater()
        else:
            regress_display.deleteLater()

    def clr_plt_single(self):
            if noise_filter_button.isChecked():
                graphWidget2.clear()
            else:
                graphWidget.clear()

    def save_plt_single(self):
        if noise_filter_button.isChecked():
            # temporary fix to show the filename
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file = QFileDialog.getSaveFileName(graphWidget2, "Save File", "",
                                               "All Files (*);; PNG (*.png);;TIFF (*.tiff)", options=options)
            print(file[0])
            exporter = pg.exporters.ImageExporter(graphWidget2.plotItem)
            exporter.parameters()['width'] = 5000
            exporter.export(file[0])
        else:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file = QFileDialog.getSaveFileName(graphWidget, "Save File", "",
                                               "All Files (*);; PNG (*.png);;TIFF (*.tiff)", options=options)
            print(file[0])
            exporter = pg.exporters.ImageExporter(graphWidget.plotItem)
            exporter.parameters()['width'] = 5000
            exporter.export(file[0])
    def export_plot_single(self):
        global writer
        # create excel writer object
        writer = pd.ExcelWriter('Results.xlsx')
        # write dataframe to excel
        df_raw.to_excel(writer, sheet_name='Raw Data')
        # save the excel
        writer.save()
    def clear_calib_single(self):
            graphWidgetCal.clear()
    def save_cal_single(self):
        # temporary fix to show the filename
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(graphWidgetCal, "Save File", "",
                                           "All Files (*);; PNG (*.png);;TIFF (*.tiff)", options=options)
        print(file[0])
        exporter = pg.exporters.ImageExporter(graphWidgetCal.plotItem)
        exporter.parameters()['width'] = 5000
        exporter.export(file[0])
    def export_cal_single(self):
        if regress_data_button.isChecked():
            calib_data_summary= pd.DataFrame(calib_summary,index=['R_squared', 'Intercept','Slope'],columns=[''])
        # create excel writer object
            writer = pd.ExcelWriter('Results.xlsx')
            # write dataframe to excel
            calib_data_summary.to_excel(writer, sheet_name='Calibration Data',startcol=5 )
            calib_data.to_excel(writer, sheet_name='Calibration Data',startcol=0)
            # save the excel
            writer.save()
        else:
            writer = pd.ExcelWriter('Results.xlsx')
            # write dataframe to excel

            calib_data.to_excel(writer, sheet_name='Calibration Data', startcol=0)
            # save the excel
            writer.save()

    def clr_normal_plt_single(self):
        graphWidgetNormCal.clear()
    def save_normal_plt_single(self):
        # temporary fix to show the filename
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(graphWidgetNormCal, "Save File", "",
                                           "All Files (*);; PNG (*.png);;TIFF (*.tiff)", options=options)
        print(file[0])
        exporter = pg.exporters.ImageExporter(graphWidgetNormCal.plotItem)
        exporter.parameters()['width'] = 5000
        exporter.export(file[0])
    def export_normal_plt_single(self):
        if regress_data_button.isChecked():
            norm_calib_summary_data = pd.DataFrame(norm_calib_summary, index=['R_squared', 'Intercept', 'Slope'], columns=[''])
            # create excel writer object
            writer = pd.ExcelWriter('Results.xlsx')
            # write dataframe to excel
            norm_calib_summary_data.to_excel(writer, sheet_name='Normalized Calibration', startcol=5)
            normalized_calib_data.to_excel(writer, sheet_name='Normalized Calibration', startcol=0)
            # save the excel
            writer.save()
        else:
            writer = pd.ExcelWriter('Results.xlsx')
            # write dataframe to excel
            normalized_calib_summary.to_excel(writer, sheet_name='Normalized Calibration', startcol=0)
            # save the excel
            writer.save()

    def export_all_data_single(self):
            # define dataframes
            norm_calib_summary_data = pd.DataFrame(norm_calib_summary, index=['R_squared', 'Intercept', 'Slope'], columns=[''])
            calib_data_summary= pd.DataFrame(calib_summary,index=['R_squared', 'Intercept','Slope'],columns=[''])
#####left off here
            # create excel writer object
            writer = pd.ExcelWriter('Results.xlsx')
            # write dataframe to excel
            df_raw.to_excel(writer, sheet_name='Raw Data')
            normalized_calib_data.to_excel(writer, sheet_name='Normalized Calibration', startcol=0)
            norm_calib_summary_data.to_excel(writer, sheet_name='Normalized Calibration', startcol=5)
            calib_data.to_excel(writer, sheet_name='Calibration Data', startcol=0)
            calib_data_summary.to_excel(writer, sheet_name='Calibration Data', startcol=5)
            # save the excel
            writer.save()
            writer.close()
