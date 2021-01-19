from import_modules import*
##This class is responsible for the quantification

class quant():

    def open_file_quant(self):
        global fileName, extension
        fileName=openFile(self)
        name, extension=os.path.splitext(fileName)
    def win_setup(self):
            ######################## Setting up Window ##########################
            self.window = QMainWindow()
            self.window = QMainWindow()
            self.window.setWindowTitle('Quantification')
            self.window.setGeometry(0, 0, 3000, 1500)
            ######################## Setting up Tabs ##########################
            self.window.tabWidget = QTabWidget(self.window)
            self.window.tabWidget.resize(2500, 1500)
            self.window.tab1 = QWidget(self.window)
            self.window.tab2 = QWidget(self.window)
            self.window.tab3 = QWidget(self.window)

            self.window.tabWidget.addTab(self.window.tab1, "Visualize Data")
            self.window.tabWidget.addTab(self.window.tab2, "Analytics - Point Selection")
            self.window.tabWidget.addTab(self.window.tab3, "Analytics - Analyte Quantification")

            self.window.tab1.layout = QGridLayout(self.window)
            self.window.tab2.layout = QGridLayout(self.window)
            self.window.tab3.layout = QGridLayout(self.window)
############ TAB1 ########
            import_statement = QLabel("Import a data file to visualize:")
            self.window.tab1.layout.addWidget(import_statement, 0, 0)
            import_statement.setAlignment(Qt.AlignRight)

            select_file_button = QPushButton("Select File")
            self.window.tab1.layout.addWidget(select_file_button, 0,1)
            select_file_button.clicked.connect(self.open_file_quant)

            plot_file_button = QPushButton("Plot File")
            self.window.tab1.layout.addWidget(plot_file_button, 2, 0)
            plot_file_button.clicked.connect(self.plot_file_quant)

            save_plot_button = QPushButton("Save Figure")
            self.window.tab1.layout.addWidget(save_plot_button, 2, 1)
            save_plot_button.clicked.connect(self.save_file_quant)

            clear_plot_button = QPushButton('Clear Plot')
            self.window.tab1.layout.addWidget(clear_plot_button, 2, 2)
            clear_plot_button.clicked.connect(self.clr_plt_quant)

            #Selecting File Type
            manufacturer_label = QLabel('Select Manufacturer & File Type:')
            self.window.tab1.layout.addWidget(manufacturer_label, 1, 0)
            manufacturer_label.setAlignment(Qt.AlignRight)

            filelist = QComboBox(self.window)
            filetype_list = ["", "HEKA (.asc)", "Biologic (.txt)","CH (.txt)","Excel (.xlsx)"]

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
                df=df.values
            filelist.activated[int].connect(filelist_selections)

            # Add PlaceHolder
            placehold = QLabel(' ')
            self.window.tab1.layout.addWidget(placehold, 3, 0, 8, 2)

############ TAB2 #########
            placehold2 = QLabel(' ')
            self.window.tab2.layout.addWidget(placehold2, 2, 0, 20, 4)

            import_statement = QLabel("Import a data file to visualize:", self.window)
            self.window.tab2.layout.addWidget(import_statement,0,0)
            import_statement.setAlignment(Qt.AlignLeft)

            select_file_button = QPushButton("Select File", self.window)
            self.window.tab2.layout.addWidget(select_file_button,0,1)
            select_file_button.clicked.connect(self.open_file_quant)

            plot_file_button = QPushButton("Plot File", self.window)
            self.window.tab2.layout.addWidget(plot_file_button,0,2)
            plot_file_button.clicked.connect(self.plot_file_quant_tab2)

            global noise_filter_button
            noise_filter_button = QCheckBox("Apply Noise-Reduction Filter?", self.window)
            self.window.tab2.layout.addWidget(noise_filter_button, 0, 3)
            noise_filter_button.stateChanged.connect(self.apply_filter_quant)

            done_selection_button = QPushButton("Done", self.window)
            self.window.tab2.layout.addWidget(done_selection_button,0,4)
            done_selection_button.clicked.connect(self.append_currents_quant)

            input_timerange_widget = QLabel("Please input the range over which the values are to be averaged (seconds): ", self.window)
            self.window.tab2.layout.addWidget(input_timerange_widget, 2, 0)

            input_timerange_text = QLineEdit(self.window)
            self.window.tab2.layout.addWidget(input_timerange_text, 2, 1)

            done_timerange_input_button = QPushButton('Done', self.window)
            self.window.tab2.layout.addWidget(done_timerange_input_button, 2, 2)

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

            def data_selection(self):
                global range,lr,time_data, current_data
                range = []
                range = np.array([int(i) for i in input_timerange_text.text().split()])

                lr = pg.LinearRegionItem(values=(0, range), orientation=pg.LinearRegionItem.Vertical)
                lr.lines[0].label = InfLineLabel(lr.lines[0], text="{value:0.3f}")
                lr.lines[1].label = InfLineLabel(lr.lines[1], text="{value:0.3f}")

                time_data = []
                current_data = []
                def update_region(self):
                    region = np.array(lr.getRegion())
                    region = np.round(region, decimals=2)
                    df2= np.array(df)

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

                    # find the data over range of points selected
                    time_pts = df2[yminloc, 0],df2[ymaxloc, 0]
                    current_pts=df2[yminloc, 1],df2[ymaxloc, 1]
                    time_data.append(time_pts)
                    current_data.append(current_pts)


                if noise_filter_button.isChecked():
                    graphWidget2.addItem(lr)
                    lr.sigRegionChangeFinished.connect(update_region)
                    curr_sel.clear()
                else:
                    graphWidgetm.addItem(lr)
                    lr.sigRegionChangeFinished.connect(update_region)


            done_timerange_input_button.clicked.connect(data_selection)

            export_points_button= QPushButton('Export Selected Points', self.window)
            self.window.tab2.layout.addWidget(export_points_button, 2,3)
            export_points_button.clicked.connect(self.export_points_quant)


            clear_pts_button = QPushButton('Clear Selections', self.window)
            self.window.tab2.layout.addWidget(clear_pts_button, 2, 4, 2, 5)
            clear_pts_button.clicked.connect(self.clear_sel_quant)
########

############# TAB3 #########
            global input_conc, input_intercept, input_current,table

            ###Quantification
            ##Slope
            slope_button_label = QLabel("Please input the regression line slope: ", self.window)
            self.window.tab3.layout.addWidget(slope_button_label, 0, 0)

            slope_input_text= QLineEdit(self.window)
            self.window.tab3.layout.addWidget(slope_input_text, 0, 1)

            ## Intercept
            intercept_button_label = QLabel("Please input the regression line intercept: ", self.window)
            self.window.tab3.layout.addWidget(intercept_button_label, 1, 0)

            intercept_input_text = QLineEdit(self.window)
            self.window.tab3.layout.addWidget(intercept_input_text, 1, 1)

            ## Current Value
            current_input_label = QLabel("Please input the current value:  ", self.window)
            self.window.tab3.layout.addWidget(current_input_label, 2, 0)
            current_input_text = QLineEdit(self.window)
            self.window.tab3.layout.addWidget(current_input_text, 2, 1)

            done_current_button = QPushButton('Done', self.window)
            self.window.tab3.layout.addWidget(done_current_button,  3, 0,3,4)

            calc_conc_button = QPushButton('Calculate Concentration', self.window)
            self.window.tab3.layout.addWidget(calc_conc_button, 4, 0,4,4)
            calc_conc_button.clicked.connect(self.calc_conc_quant)
            global values
            values = 0
            def input_values(self):
                global values, slope_value, intercept_value, current_value
                slope_value = slope_input_text.text()
                table.setItem(0, values, QTableWidgetItem( slope_value))

                intercept_value = intercept_input_text.text()
                table.setItem(1, values, QTableWidgetItem(intercept_value))

                current_value = current_input_text.text()
                table.setItem(2, values, QTableWidgetItem(current_value))
                values += 1
                slope_input_text.clear()
                intercept_input_text.clear()
                current_input_text.clear()

            done_current_button.clicked.connect(input_values)

            table = QTableWidget(self.window)
            table.setRowCount(4)
            table.setColumnCount(11)
            columnLabels = ["Reading 1", "Reading 2", "Reading 3","Reading 4","Reading 5","Reading 6","Reading 7","Reading 8","Reading 9","Reading 10","Reading 11"]
            rowLabels = ["Slope", "Intercept", "Current","Concentration "]
            table.setHorizontalHeaderLabels(columnLabels)
            table.setVerticalHeaderLabels(rowLabels)
            table.resizeColumnsToContents()
            table.resizeRowsToContents()

            self.window.tab3.layout.addWidget(table, 10, 0,10,9)

            export_table = QPushButton('Export Table', self.window)
            self.window.tab3.layout.addWidget(export_table, 5, 0, 5, 4)
            export_table.clicked.connect(self.save_table_quant)

            clear_table = QPushButton('Clear Table', self.window)
            self.window.tab3.layout.addWidget(clear_table, 6, 0, 6, 4)
            clear_table.clicked.connect(self.clr_table_quant)

            placehold3 = QLabel(' ')
            self.window.tab3.layout.addWidget(placehold3, 11, 0, 12, 10)

            ###Display all tabs
            self.window.tab1.setLayout(self.window.tab1.layout)
            self.window.tab2.setLayout(self.window.tab2.layout)
            self.window.tab3.setLayout(self.window.tab3.layout)
            self.window.show()
    ######################## Data Analysis ##########################

    ######## Tab 1: Visualize Data ########
    def plot_file_quant(self):
        pg.setConfigOption('foreground', 'k')
        font = QFont()
        penn= pg.mkPen(color='k', width=2)
        font.setBold(False)
        font.setPixelSize(25)
        global graphWidget ,save_plot_button
        graphWidget = pg.PlotWidget(self.window)
        graphWidget.getAxis('bottom').setTickFont(font)
        graphWidget.getAxis('left').setTickFont(font)
        graphWidget.getAxis('bottom').setStyle(tickTextOffset=10)
        graphWidget.getAxis('left').setStyle(tickTextOffset=5)
        graphWidget.getAxis('left').setPen(penn)
        graphWidget.getAxis('bottom').setPen(penn)
        pen = pg.mkPen(color=(255, 0, 0)) #,width=2)
        graphWidget.plot(df[:,0], df[:,1], pen=pen)
        styles = {'color': 'k', 'font-size': '30px','font-weight':'bold','font-type':'arial'}
        graphWidget.setLabel('left', 'Current / A', **styles)
        graphWidget.setLabel('bottom', 'Time / s', **styles)
        graphWidget.setBackground('w')
        graphWidget.show()
        save_plot_button = QPushButton("Save File", self.window)
        self.window.tab1.layout.addWidget(save_plot_button,3,0,6,2)  #fix location here
        save_plot_button.clicked.connect(self.save_file_quant)
        self.window.tab1.layout.addWidget(graphWidget)

    def clr_plt_quant(self):
        graphWidget.deleteLater()
        save_plot_button.deleteLater()

    def save_file_quant(self):
        # temporary fix to show the filename
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(graphWidget, "Save File", "",
                                           "All Files (*);; PNG (*.png);;TIFF (*.tiff)", options=options)
        print(file[0])
        exporter = pg.exporters.ImageExporter(graphWidget.plotItem)
        exporter.parameters()['width'] = 5000
        exporter.export(file[0])

    ######## Tab 2: Select Points ########
    def plot_file_quant_tab2(self):
        #Plot File
        global graphWidgetm,curr_sel
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
        graphWidgetm.setLabel('left', 'Current /pA', **styles)
        graphWidgetm.setLabel('bottom', 'Time /s', **styles)
        graphWidgetm.setBackground('w')
        graphWidgetm.show()
        curr_sel=[]
        self.window.tab2.layout.addWidget(graphWidgetm,3,0,20,5)

    def apply_filter_quant(self, state):
        if noise_filter_button.isChecked():
            global graphWidget2
            smooth_1dg = savgol_filter(df[:, 1], window_length=5, polyorder=1)
            df[:, 1] = smooth_1dg
            plt.plot(df[:, 0], df[:, 1])  # , label='2nd order') #, kind = 'line',legend=False)
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
            self.window.tab2.layout.addWidget(graphWidget2,2,0,20,5)

        else:
            graphWidget2.deleteLater()

    global curr_sel2
    curr_sel2 = []
    def append_currents_quant(self):
        curr_sel2.append(curr_sel)
        global current_sel, time_values, current_values
        current_sel = []
        current_sel =np.array(curr_sel2)

        time_values=[]
        current_values=[]
        time_values.append(time_data)
        current_values.append(current_data)


    def clear_sel_quant(self):
        lr.hide()
        curr_sel.clear()
        curr_sel2.clear()

    def export_points_quant(self):
        current_sel_ = pd.DataFrame(current_sel)
        time_values_ = pd.DataFrame(time_values)
        current_values_=pd.DataFrame(current_values)
        time_values_.columns = pd.MultiIndex.from_product([['Time Points (first,last)'], time_values_.columns])
        current_values_.columns = pd.MultiIndex.from_product([['Current Values (first,last)'], current_values_.columns])
        current_sel_.columns = pd.MultiIndex.from_product([['Mean Currents (pA)'], current_sel_.columns])

        writer = pd.ExcelWriter('Results.xlsx')
        # # write dataframe to excel
        current_sel_.to_excel(writer, sheet_name='Point Selection', startrow=10)
        time_values_.to_excel(writer, sheet_name='Point Selection', startcol=0)
        current_values_.to_excel(writer, sheet_name='Point Selection', startrow=5)

        # # save the excel
        writer.save()
    ######################## TAB 3- QUANTIFICATION ##########################
    def calc_conc_quant(self):
        calc_conc=(float(current_value)-float(intercept_value))/float(slope_value)
        table.setItem(3, values-1, QTableWidgetItem(str(calc_conc)))

    def clr_table_quant(self):
        table.clear()
        columnLabels = ["Reading 1", "Reading 2", "Reading 3", "Reading 4", "Reading 5", "Reading 6", "Reading 7",
                        "Reading 8", "Reading 9", "Reading 10", "Reading 11"]
        rowLabels = ["Slope", "Intercept", "Current", "Concentration "]
        table.setHorizontalHeaderLabels(columnLabels)
        table.setVerticalHeaderLabels(rowLabels)
        global values
        values=0


    def save_table_quant(self):
        filename,_ = QFileDialog.getSaveFileName(self, 'Save File', '', ".xls(*.xls)")
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet("sheet", cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.bold = True
        style.font = font
        model =table.model()
        for c in range(model.columnCount()):
            text = model.headerData(c, Qt.Horizontal)
            sheet.write(0, c+1, text, style=style)

        for r in range(model.rowCount()):
            text = model.headerData(r, Qt.Vertical)
            sheet.write(r+1, 0, text, style=style)

        for c in range(model.columnCount()):
            for r in range(model.rowCount()):
                text = model.data(model.index(r, c))
                sheet.write(r+1, c+1, text)
        wbk.save(filename)