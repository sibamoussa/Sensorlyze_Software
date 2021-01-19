from import_modules import*
##This class is responsible for the calibration curve data analysis
class multiple_cal():

    def open_file_mult(self):
        global fileName, extension
        fileName = openFile(self)
        name, extension = os.path.splitext(fileName)
    def win_setup(self):
            self.window = QMainWindow()
            self.window.setWindowTitle('Multiple Sensor Calibration')
            self.window.setGeometry(0, 0, 3000, 1500)
            ######################## Setting up Tabs ##########################
            self.window.tabWidget = QTabWidget(self.window)
            self.window.tabWidget.resize(2500, 1500)
            self.window.tab1 = QWidget(self.window)
            self.window.tab2 = QWidget(self.window)
            self.window.tab3 = QWidget(self.window)
            self.window.tab4 = QWidget(self.window)
            #Name Tabs
            self.window.tabWidget.addTab(self.window.tab1, "Visualize Data")
            self.window.tabWidget.addTab(self.window.tab2, "Analytics - Calibration Point Selection")
            self.window.tabWidget.addTab(self.window.tab3, "Analytics - Calibration Statistics")
            #self.window.tabWidget.addTab(self.window.tab4, "Formatting")

            #Set content layout in each tabbed window
            self.window.tab1.layout = QGridLayout(self.window)
            self.window.tab2.layout = QGridLayout(self.window)
            self.window.tab3.layout = QGridLayout(self.window)
            #self.window.tab4.layout = QVBoxLayout(self.window)

##### Add Buttons to Tabs #####
############ TAB1 ########
            import_statement = QLabel("Import a data file to visualize (max=5): ", self.window)
            self.window.tab1.layout.addWidget(import_statement,0,0)

            select_file_button = QPushButton("Select File", self.window)
            self.window.tab1.layout.addWidget(select_file_button,0,1)
            select_file_button.clicked.connect(self.open_file_mult)

            plot_file_button = QPushButton("Plot File", self.window)
            self.window.tab1.layout.addWidget(plot_file_button,0,2)
            plot_file_button.clicked.connect(self.plot_file_mult)

            clear_plot_button = QPushButton('Clear Last Plot')
            self.window.tab1.layout.addWidget(clear_plot_button,0,4)
            clear_plot_button.clicked.connect(self.clr_plt)

            # Selecting File Type
            manufacturer_label = QLabel('Select Manufacturer & File Type:')
            self.window.tab1.layout.addWidget(manufacturer_label, 1, 0)
            manufacturer_label.setAlignment(Qt.AlignRight)

            filelist = QComboBox(self.window)
            filetype_list = ["", "HEKA (.asc)", "Biologic (.txt)", "CH (.txt)","Excel (.xlsx)"]
            filelist.addItems(filetype_list)
            self.window.tab1.layout.addWidget(filelist, 1, 1)
            def filelist_selections(self):
                global df
                filetype_selection = filelist.currentText()
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
            filelist.activated[int].connect(filelist_selections)

            #Add PlaceHolder
            placehold = QLabel(' ')
            self.window.tab1.layout.addWidget(placehold,2,0,2,20)

            #set-up counter for plots
            global value
            value = 0
            def plot_counter(self):
                global value
                value += 1

            next_plot_button = QPushButton('Next', self.window)
            self.window.tab1.layout.addWidget(next_plot_button, 0, 3)
            next_plot_button.clicked.connect(plot_counter)
############ TAB2 #########
            import_statement = QLabel("Import a data file to visualize:", self.window)
            self.window.tab2.layout.addWidget(import_statement,0,0)
            import_statement.setAlignment(Qt.AlignRight)

            select_file_button = QPushButton("Select File", self.window)
            self.window.tab2.layout.addWidget(select_file_button,0,1)
            select_file_button.clicked.connect(self.open_file_mult)

            plot_file_button = QPushButton("Plot File", self.window)
            self.window.tab2.layout.addWidget(plot_file_button,0,2)
            plot_file_button.clicked.connect(self.plot_file_mult_tab2)

            global noise_filter_button
            noise_filter_button = QCheckBox("Apply Noise-Reduction Filter?", self.window)
            self.window.tab2.layout.addWidget(noise_filter_button, 0, 3)
            noise_filter_button.stateChanged.connect(self.apply_filter)

            next_plot_button = QPushButton("Next", self.window)
            self.window.tab2.layout.addWidget(next_plot_button,0,4)
            next_plot_button.clicked.connect(self.append_currents)

            done_selection_button = QPushButton("Done", self.window)
            self.window.tab2.layout.addWidget(done_selection_button,0,5)
            done_selection_button.clicked.connect(self.mean_curr_checkequalarr)

            manufacturer_label = QLabel('Select Manufacturer & File Type:')
            self.window.tab2.layout.addWidget(manufacturer_label, 1, 0)
            manufacturer_label.setAlignment(Qt.AlignRight)

            filelist2 = QComboBox(self.window)
            filelist2.addItems(filetype_list)
            self.window.tab2.layout.addWidget(filelist2, 1, 1)

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
                        df_round_time=df.iloc[:,0]
                        df_round_time=df_round_time.round(decimals=2)
                        df.iloc[:,0]=df_round_time
                        if 'mA' in colname:
                            df.iloc[:,1] = df.iloc[:,1] * 10 ** -3
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


            input_conc_widget = QLabel("Please input all concentrations with a space in between: ", self.window)
            self.window.tab2.layout.addWidget(input_conc_widget, 2,0)

            input_conc_text= QLineEdit(self.window)
            self.window.tab2.layout.addWidget(input_conc_text,2,1)

            done_conc_input_button = QPushButton('Done', self.window)
            self.window.tab2.layout.addWidget(done_conc_input_button,2,2)

            def conc_values(self):
                global concs_values #previously Concs2
                concs_values = np.array([int(i) for i in input_conc_text.text().split()])

            done_conc_input_button.clicked.connect(conc_values)

            export_points_button= QPushButton('Export Selected Points', self.window)
            self.window.tab2.layout.addWidget(export_points_button, 2,3)
            export_points_button.clicked.connect(self.export_points)

            calib_tab_button = QPushButton('Go to Calibrations', self.window)
            self.window.tab2.layout.addWidget(calib_tab_button, 2,4)
            calib_tab_button.clicked.connect(lambda: self.window.tabWidget.setCurrentIndex(2))

            #### PlaceHolder
            placehold_tab2 = QLabel(' ')
            self.window.tab2.layout.addWidget(placehold_tab2, 3, 0, 3, 4)

            ############# TAB3 #########
            ###Plot Calibration
            placehold3 = QLabel(' ')
            self.window.tab3.layout.addWidget(placehold3, 4, 3, 28, 3)
            plot_calib_button = QPushButton('Plot Calibration', self.window)
            self.window.tab3.layout.addWidget(plot_calib_button,1,1,1,2)
            plot_calib_button.clicked.connect(self.plot_average_cal)

            save_calib_button = QPushButton('Save Plot', self.window)
            self.window.tab3.layout.addWidget(save_calib_button,2,1,2,2)
            save_calib_button.clicked.connect(self.save_calib)

            export_plot_button = QPushButton('Export Data', self.window)
            self.window.tab3.layout.addWidget(export_plot_button, 3, 1,3,2)
            export_plot_button.clicked.connect(self.export_plot)

            plot_normalcalib_button = QPushButton('Plot Normalized Cal', self.window)
            self.window.tab3.layout.addWidget(plot_normalcalib_button,1,3,1,4)
            plot_normalcalib_button.clicked.connect(self.plot_normalized_calib)

            save_normalcalib_button = QPushButton('Save Plot', self.window)
            self.window.tab3.layout.addWidget(save_normalcalib_button, 2,3,2,4)
            save_normalcalib_button.clicked.connect(self.save_normalized_calib)

            export_normalcalib_button = QPushButton('Export Data', self.window)
            self.window.tab3.layout.addWidget(export_normalcalib_button,3,3,3,4)
            export_normalcalib_button.clicked.connect(self.export_normalized_plot)

    ###Display all tabs
            self.window.tab1.setLayout(self.window.tab1.layout)
            self.window.tab2.setLayout(self.window.tab2.layout)
            self.window.tab3.setLayout(self.window.tab3.layout)
            self.window.show()

    ######################## BASIC FILE VISUALIZATION ##########################
    def plot_file_mult(self):
        font = QFont()
        penn= pg.mkPen(color='k', width=2)
        font.setBold(False)
        font.setPixelSize(25)
        global graphWidget
        graphWidget = pg.PlotWidget(self.window)
        graphWidget.getAxis('bottom').setTickFont(font)
        graphWidget.getAxis('left').setTickFont(font)
        graphWidget.getAxis('bottom').setStyle(tickTextOffset=10)
        graphWidget.getAxis('left').setStyle(tickTextOffset=5)
        graphWidget.getAxis('left').setPen(penn)
        graphWidget.getAxis('bottom').setPen(penn)
        pen = pg.mkPen(color=(255, 0, 0)) #,width=2)
        graphWidget.plot(df[:,0],df[:,1], pen=pen)
        styles = {'color': 'k', 'font-size': '30px','font-weight':'bold','font-type':'arial'}
        graphWidget.setLabel('left', 'Current / A', **styles)
        graphWidget.setLabel('bottom', 'Time / s', **styles)
        graphWidget.setBackground('w')
        graphWidget.show()
        global save_plot_button
        save_plot_button = QPushButton("Save File", self.window)
        self.window.tab1.layout.addWidget(save_plot_button,1,value)
        save_plot_button.clicked.connect(self.save_file)

        #self.window.tab1.layout.addWidget(Valz, 1, 0, 2, 30)
        self.window.tab1.layout.addWidget(graphWidget) #,2,value*2+1,3,value*2+1)

    def clr_plt(self):
        graphWidget.deleteLater()
        save_plot_button.deleteLater()

    def save_file(self):
        # temporary fix to show the filename
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(graphWidget, "Save File", "",
                                           "All Files (*);; PNG (*.png);;TIFF (*.tiff);; JPEG(*.JPEG)", options=options)
        print(file[0])
        exporter = pg.exporters.ImageExporter(graphWidget.plotItem)
        exporter.parameters()['width'] = 5000
        exporter.export(file[0])

    ######################## TAB 2 - POINT SELECTION  ##########################
    def plot_file_mult_tab2(self):
        global graphWidgetm
        font = QFont()
        penn = pg.mkPen(color='k', width=2)
        font.setBold(False)
        font.setPixelSize(25)
        graphWidgetm = pg.PlotWidget(self.window)
        graphWidgetm.getAxis('bottom').setTickFont(font)
        graphWidgetm.getAxis('left').setTickFont(font)
        graphWidgetm.getAxis('bottom').setStyle(tickTextOffset=10)
        graphWidgetm.getAxis('left').setStyle(tickTextOffset=5)
        graphWidgetm.getAxis('left').setPen(penn)
        graphWidgetm.getAxis('bottom').setPen(penn)
        pen = pg.mkPen(color=(255, 0, 0))
        graphWidgetm.plot(df[:,0], df[:,1],pen=pen)
        styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold', 'font-type': 'arial'}
        graphWidgetm.setLabel('left', 'Current /A', **styles)
        graphWidgetm.setLabel('bottom', 'Time /s', **styles)
        graphWidgetm.setBackground('w')
        graphWidgetm.show()
        global curr_sel
        curr_sel=[]

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
            curr_sel.append(selection_avg)

        lr= pg.LinearRegionItem(values=(0,30),orientation=pg.LinearRegionItem.Vertical)
        lr.lines[0].label = InfLineLabel(lr.lines[0], text="{value:0.3f}")
        lr.lines[1].label = InfLineLabel(lr.lines[1], text="{value:0.3f}")
        graphWidgetm.addItem(lr)
        self.window.tab2.layout.addWidget(graphWidgetm,4,0,10,5)
        lr.sigRegionChangeFinished.connect(update_region)

    def apply_filter(self, state):
        if noise_filter_button.isChecked():
            global graphWidget2
            smooth_1dg = savgol_filter(df[:,1], window_length=5, polyorder=1)
            df[:,1] = smooth_1dg
            plt.plot(df[:,0], df[:,1])  # , label='2nd order') #, kind = 'line',legend=False)
            font = QFont()
            penn = pg.mkPen(color='k', width=2)
            graphWidget2 = pg.PlotWidget(self.window)
            pen = pg.mkPen(color=(100, 200, 100))
            font.setBold(False)
            font.setPixelSize(25)
            graphWidget2.getAxis('bottom').setTickFont(font)
            graphWidget2.getAxis('left').setTickFont(font)
            graphWidget2.getAxis('bottom').setStyle(tickTextOffset=10)
            graphWidget2.getAxis('left').setStyle(tickTextOffset=5)
            graphWidget2.getAxis('left').setPen(penn)
            graphWidget2.getAxis('bottom').setPen(penn)
            graphWidget2.plot(df[:,0], df[:,1], pen=pen)
            styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold', 'font-type': 'arial'}
            graphWidget2.setLabel('left', 'Current /pA', **styles)
            graphWidget2.setLabel('bottom', 'Time /s', **styles)
            graphWidget2.setBackground('w')
            graphWidget2.setTitle('Noise Filtered', **styles)
            graphWidget2.show()
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
                curr_sel.append(selection_avg)

            lr = pg.LinearRegionItem(values=(0, 30), orientation=pg.LinearRegionItem.Vertical)
            lr.lines[0].label = InfLineLabel(lr.lines[0], text="{value:0.3f}")
            lr.lines[1].label = InfLineLabel(lr.lines[1], text="{value:0.3f}")
            graphWidget2.addItem(lr)
            lr.sigRegionChangeFinished.connect(update_region)
            self.window.tab2.layout.addWidget(graphWidget2,4,0,10,5)

        else:
            graphWidget2.deleteLater()

    global curr_sel2
    curr_sel2 = []
    def append_currents(self):
        curr_sel3 = (curr_sel)
        curr_sel2.append(curr_sel3)
        subs=iter(curr_sel2)
        len_=len(next(subs))
        eqlmat=all(len(sub)==len_ for sub in subs)
        if eqlmat==False:
            msg = QMessageBox(self.window)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error, Please make sure equal number of selections are made for each file, all previous selections were cleared")
            msg.setWindowTitle("Error")
            returnValue = msg.exec()
            curr_sel2.clear()
        else:
            pass

        if noise_filter_button.isChecked():
           graphWidget2.clear()
           graphWidgetm.clear()
           noise_filter_button.setChecked(False)
        else:
           graphWidgetm.clear()

    def mean_curr_checkequalarr(self):
        global current_selections #previously currentsm3
        current_selections = []
        global mean_curr
        current_selections =np.array(curr_sel2)
        mean_curr=np.mean(curr_sel2,axis=0)
        same = len(mean_curr) == len(concs_values)
        if same:
            pass
        else:
            msg = QMessageBox(self.window)
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error, Please make sure equal number of concentrations are listed for the number current selections, reinput concentrations")
            msg.setWindowTitle("Error")
            returnValue = msg.exec()

    def export_points(self):
        selected_pts = pd.DataFrame({'Concentration (uM)': concs_values,'PointsMean':mean_curr})
        selected_pts_2 = pd.DataFrame(current_selections)
        selected_pts_2.columns = pd.MultiIndex.from_product([['Points'], selected_pts_2.columns])
        selected_pts_2.index = pd.MultiIndex.from_product([['Trials'], selected_pts_2.index])
        # create excel writer object
        writer = pd.ExcelWriter('Results.xlsx')
        # write dataframe to excel
        selected_pts.to_excel(writer, sheet_name='Point Selection Data', startcol=0)
        selected_pts_2.to_excel(writer, sheet_name='Point Selection Data2', startcol=0)
        # save the excel
        writer.save()
    ######################## TAB 3- RESULTS VISUALIZATION ##########################

    def plot_average_cal(self):
        sem_currents = stats.sem(current_selections, axis=0)
        std_currents = np.std(current_selections, axis=0)
        concs = (np.array(concs_values)).reshape(-1, 1)
        mean_currents = (np.array(mean_curr)).reshape(-1, 1)
        global calib_points
        calib_points = pd.DataFrame({'Concentration (uM)': concs_values, 'Currents (pA)': mean_curr,'Standard Deviation': std_currents,'SEM': sem_currents})

        #build and obtain regression model
        lrfit = LinearRegression().fit(concs, mean_currents.reshape((-1, 1)))
        current_pred = lrfit.predict(concs)
        r_sq = lrfit.score(concs,mean_currents)
        regr_slope=lrfit.coef_[0]
        sensor_lod =(3 * std_currents[0] / regr_slope)
        sensor_loq= (10* std_currents[0] / regr_slope)

        #round values to 3 sig figs
        rounded_slope = list(np.round(regr_slope, 3))
        regression_statssummary = [('R_squared:', round(r_sq, 3), 'Intercept:', round(lrfit.intercept_[0], 3), 'Slope:', rounded_slope,'LOD', round(sensor_lod[0],3),'LOQ', round(sensor_loq[0],3))]
        regression_statssummary_str = str([tuple(str(ele) for ele in sub) for sub in regression_statssummary])
        regression_statssummary_cleaned = regression_statssummary_str.replace("'", "").replace(",", "").replace("]", "").replace("[", "").replace(")","").replace("(","")

        global calib_summary
        calib_summary = [r_sq, lrfit.intercept_[0],regr_slope,sensor_lod[0],sensor_loq[0]]

        regress_display = QLineEdit(self.window)
        regress_display.setAlignment(Qt.AlignCenter)
        regress_display.setText(str(regression_statssummary_cleaned))
        self.window.tab3.layout.addWidget(regress_display,19,1,19,2)

        global fig_cal
        fig_cal = (plt.figure(figsize=(2, 2), dpi=300))
        fig= FigureCanvas(fig_cal)
        plt.errorbar(concs_values, mean_curr, yerr=sem_currents, fmt='.k', color='black', ecolor='black', elinewidth=1, capsize=2)
        plt.plot(concs, current_pred, color='black', linewidth=2)
        plt.ylabel('i$_{ss}$ / A', fontsize=10)
        plt.xlabel('[Concentration] / $\mu$M', fontsize=10)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()
        self.window.tab3.layout.addWidget(fig,10,1,12,2)

    def save_calib(self):
        # temporary fix to show the filename
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file,_ = QFileDialog.getSaveFileName(self,"Save Image", "", "All Files (*);; PNG (*.png);;TIFF (*.tiff);; JPEG(*.JPEG)", options=options)
        fig_cal.savefig(file)

    def export_plot(self):
            cal_summary= pd.DataFrame(calib_summary,index=['R_squared', 'Intercept','Slope','LOD','LOQ'],columns=[''])
            # create excel writer object
            writer = pd.ExcelWriter('Results.xlsx')
            # write dataframe to excel
            cal_summary.to_excel(writer, sheet_name='Calibration Data',startcol=10)
            calib_points.to_excel(writer, sheet_name='Calibration Data',startcol=0)
            # save the excel
            writer.save()

    def plot_normalized_calib(self):
        currents_blank=current_selections[:,0]
        std_blank = np.array(np.std(currents_blank, axis=0))
        normalized_currents=current_selections

        #normalize currents
        for i in range(normalized_currents.shape[0]):  # iterate over rows
            normalized_currents[i] = current_selections[i] - np.transpose(currents_blank[i])

        mean_currents = np.mean(normalized_currents, axis=0)
        sem_currents = stats.sem(normalized_currents, axis=0)

        #reshape x and y, build regression model
        concs = (np.array(concs_values)).reshape(-1, 1)
        currents = (np.array(mean_currents)).reshape(-1, 1)
        lrfit = LinearRegression().fit(concs, currents.reshape((-1, 1)))
        global calib_norm_selectedpts
        calib_norm_selectedpts = pd.DataFrame({'Concentration (uM)': concs_values, 'Currents (pA)': mean_currents, 'Standard Deviation': std_blank, 'SEM': sem_currents})
        current_pred = lrfit.predict(concs)
        r_sq = lrfit.score(concs, currents)
        regr_slope=lrfit.coef_[0]
        sensor_lod = 3 * std_blank / regr_slope
        sensor_loq = 10 * std_blank / regr_slope

        #round values to 3 sig figs
        rounded_slope = list(np.round(regr_slope, 3))
        regression_statssummary = [('R_squared:', round(r_sq, 3), 'Intercept:', round(lrfit.intercept_[0], 3), 'Slope:', rounded_slope,'LOD', round(sensor_lod[0], 3), 'LOQ', round(sensor_loq[0], 3))]
        regression_statssummary_str =str([tuple(str(ele) for ele in sub) for sub in regression_statssummary])
        regression_statssummary_cleaned = regression_statssummary_str.replace("'", "").replace(",", "").replace("]", "").replace("[", "").replace(")", "").replace("(", "") #previously slopedata4

        global normal_calib_summary
        normal_calib_summary = [r_sq, lrfit.intercept_[0], rounded_slope,sensor_lod[0],sensor_loq[0]]

        # textbox display regression summary
        regress_display = QLineEdit(self.window)
        regress_display.setAlignment(Qt.AlignCenter)
        regress_display.setText(str(regression_statssummary_cleaned))
        self.window.tab3.layout.addWidget(regress_display, 19, 3,19,4)

        #set up visualization
        global norm_fig
        norm_fig = (plt.figure(figsize=(2, 2), dpi=300))
        fig_norm = FigureCanvas(norm_fig)
        plt.errorbar(concs_values, mean_currents, yerr=sem_currents, fmt='.k', color='black', ecolor='black', elinewidth=1, capsize=2)
        plt.plot(concs, current_pred, color='black', linewidth=2) #plot regression line
        plt.ylabel('i$_{norm}$ / A', fontsize=10)
        plt.xlabel('[Concentration] / $\mu$M', fontsize=10)

        #plot layouts
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()

        self.window.tab3.layout.addWidget(fig_norm,10,4,12,5)

    def save_normalized_calib(self):
        # temporary fix to show the filename
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file,_ = QFileDialog.getSaveFileName(self,"Save Image", "", "All Files (*);; PNG (*.png);;TIFF (*.tiff);;JPEG (*.JPEG)", options=options)
        norm_fig.savefig(file)

    def export_normalized_plot(self):
            calib_data= pd.DataFrame(normal_calib_summary,index=['R_squared', 'Intercept','Slope','LOD','LOQ'],columns=[''])
            # create excel writer object
            writer = pd.ExcelWriter('Results.xlsx')
            # write dataframe to excel
            calib_data.to_excel(writer, sheet_name='Normalized Calibration',startcol=10 )
            calib_norm_selectedpts.to_excel(writer, sheet_name='Normalized Calibration',startcol=0)
            # save the excel
            writer.save()
