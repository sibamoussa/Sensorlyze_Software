##This class is responsible for visualizing data

from import_modules import*

class datavis():

    def open_file_datavis(self):
        global fileName,extension
        fileName = openFiles(self)

    def win_setup(self):
            self.window = QMainWindow()
            self.window.setWindowTitle('Data Visualization')
            self.window.setGeometry(0, 0, 3000, 1500)
            ######################## Setting up Tabs ##########################
            self.window.tabWidget = QTabWidget(self.window)
            self.window.tabWidget.resize(2500, 1500)
            self.window.tab1 = QWidget(self.window)
            self.window.tab2 = QWidget(self.window)
            self.window.tab3 = QWidget(self.window)

            self.window.tabWidget.addTab(self.window.tab1, "Visualize Data")


            # Working on Tab 1
            self.window.tab1.layout = QGridLayout(self.window)
            self.window.tab2.layout = QGridLayout(self.window)
            self.window.tab3.layout = QVBoxLayout(self.window)

 ############ TAB1 #########
            import_statement = QLabel("Import a data file to visualize:")
            self.window.tab1.layout.addWidget(import_statement,0,0)
            import_statement.setAlignment(Qt.AlignRight)

            select_file_button = QPushButton("Select File")
            self.window.tab1.layout.addWidget(select_file_button,0,1)
            select_file_button.clicked.connect(self.open_file_datavis)

            plot_file_button = QPushButton("Plot File")
            self.window.tab1.layout.addWidget(plot_file_button,0,3)
            plot_file_button.clicked.connect(self.plot_file_datavis)

            save_plot_button = QPushButton("Save Plot")
            self.window.tab1.layout.addWidget(save_plot_button,1,3)
            save_plot_button.clicked.connect(self.save_plt_datavis)

            clear_plot_button = QPushButton('Clear Plot')
            self.window.tab1.layout.addWidget(clear_plot_button,2,3)
            clear_plot_button.clicked.connect(self.clr_plt_datavis)

            # Selecting File Type
            manufacturer_label = QLabel('Select Manufacturer & File Type:')
            self.window.tab1.layout.addWidget(manufacturer_label,1,0)
            manufacturer_label.setAlignment(Qt.AlignRight)

            filelist = QComboBox(self.window)
            filetype_list = ["", "HEKA (.asc)", "Biologic (.txt)"]

            filelist.addItems(filetype_list)
            self.window.tab1.layout.addWidget(filelist, 1, 1)

            def filelist_selections(self):
                global fileName_str, df
                extension_name=[]
                for i in fileName:
                    fileName_str=str(fileName)
                    name, extension = os.path.splitext(fileName_str)
                    extension_name.append(extension)

                #check that the file extension matches the selected extension to proceed with data analysis
                format_check = False;
                if len(extension_name) > 0:
                    format_check = all(elem == extension_name[0] for elem in extension_name)
                if format_check:
                    filetype_selection = filelist.currentText()
                    if filetype_selection == "HEKA (.asc)":
                        if '.asc' in extension_name[0] :
                            global header, indexes
                            header=[]
                            data = []
                            df=[]
                            indexes=[]

                            for file in fileName:
                                styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold',
                                          'font-type': 'arial'}
                                with open(file, 'r') as fh:
                                    for curline in fh:
                                        if curline[0]=='"':
                                            curline = curline.strip('\n').split('\t')
                                            header=curline
                                        else:
                                            pass
                                fh.close()
                                with open(file, 'r') as fh:
                                    for curline in fh:
                                         curline = curline.split()
                                         try:
                                             float(curline[0])
                                             data.append(curline)
                                         except:
                                                pass
                                indexes.append(len(data))
                                fh.close()
                            df = pd.DataFrame(data,columns=header,dtype='float')

                            #removing unnecessary characters
                            df.columns = df.columns.str.replace("]", '')
                            df.columns = df.columns.str.replace('"', '')
                            df.columns = df.columns.str.replace("[", '/')

                    elif filetype_selection == "Biologic (.txt)":
                            if '.txt' in extension_name[0]:
                                header = []
                                data = []
                                df = []
                                indexes = []
                                for file in fileName:
                                    styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold',
                                              'font-type': 'arial'}
                                    with open(file, 'r') as fh:
                                        for curline in fh:
                                            if curline[0] == 'm':
                                                curline = curline.split('\t')
                                                curline=[item.replace('>','') for item in curline]
                                                curline=[item.replace('<','') for item in curline]
                                                header = curline
                                            else:
                                                pass
                                    fh.close()
                                    with open(file, 'r') as fh:
                                        for curline in fh:
                                            curline = curline.split()
                                            try:
                                                float(curline[0])
                                                data.append(curline)
                                            except:
                                                pass
                                    indexes.append(len(data))
                                    fh.close()
                                    print(header)
                                    header = [str(x) for x in header]

                                    num_cols = len(data[0])
                                    num_headers =len(header)
                                    if num_cols!=num_headers:
                                        del header[-1]
                                    else:
                                        pass

                                    #capitalize the first letter for each label in header
                                    headercap = [label.capitalize() for label in header]
                                df = pd.DataFrame(data,columns=headercap,dtype='float')


                            else:
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Critical)
                                msg.setText("Please chose file with .asc extension")
                                msg.setWindowTitle("Error")
                                returnValue = msg.exec()
                    else:
                        pass
                else:
                    print("Not all selected files are the same file format")
            filelist.activated[int].connect(filelist_selections)

            # Select x axis
            select_x_axis = QLabel('Select X-Axis:')
            self.window.tab1.layout.addWidget(select_x_axis, 2, 0)
            select_x_axis.setAlignment(Qt.AlignRight)

            xaxis_list = QComboBox(self.window)
            xaxis_selection = ["", "Emon","Imon","Time","Ewe","I"]
            xaxis_list.addItems(xaxis_selection)

            def xaxis_sel1(self):
                global xaxis_sel
                xaxis_sel = xaxis_list.currentText()
                print(xaxis_sel)

            xaxis_list.activated[int].connect(xaxis_sel1)


            self.window.tab1.layout.addWidget(xaxis_list, 2, 1)
            # Select y axis
            select_y_axis = QLabel('Select Y-Axis:')
            self.window.tab1.layout.addWidget(select_y_axis, 3, 0)
            select_y_axis.setAlignment(Qt.AlignRight)

            yaxis_list = QComboBox(self.window)
            yaxis_selection = ["", "Emon","Imon","Time","Ewe","I"]

            yaxis_list.addItems(yaxis_selection)

            def yaxis_sel1(self):
                global yaxis_sel
                yaxis_sel = yaxis_list.currentText()
                print(yaxis_sel)

            yaxis_list.activated[int].connect(yaxis_sel1)
            self.window.tab1.layout.addWidget(yaxis_list, 3, 1)

            #PlaceHolder
            placehold = QLabel(' ')
            self.window.tab1.layout.addWidget(placehold,5,0,8,2)

            # ###Display all tabs
            self.window.tab1.setLayout(self.window.tab1.layout)
            self.window.tab2.setLayout(self.window.tab2.layout)
            self.window.show()
    ######################## BASIC FILE VISUALIZATION ##########################

    def plot_file_datavis(self):
        df_x = df.filter(regex=xaxis_sel)
        df_x = df_x.loc[:, ~df_x.columns.duplicated()]
        df_y=df.filter(regex=yaxis_sel)
        df_y=df_y.loc[:,~df_y.columns.duplicated()]
        df_filtered=df_x.join(df_y)
        df_split=np.split(df_filtered,indexes)
        font = QFont()
        penn= pg.mkPen(color='k', width=2)
        font.setBold(False)
        font.setPixelSize(25)
        global graphWidget
        graphWidget = pg.PlotWidget(self.window)
        file_index=0
        plot_color=0
        ind=(len(indexes))
        for array in df_split:
            if file_index <= ind-1:
                arrayx=array.filter(regex=xaxis_sel)
                array_x=arrayx.values

                arrayy=array.filter(regex=yaxis_sel)
                array_y = arrayy.values

                graphWidget.getAxis('bottom').setTickFont(font)
                graphWidget.getAxis('left').setTickFont(font)
                graphWidget.getAxis('bottom').setStyle(tickTextOffset=10)
                graphWidget.getAxis('left').setStyle(tickTextOffset=5)
                graphWidget.getAxis('left').setPen(penn)
                pen = pg.mkPen(color=(125+plot_color, 50+plot_color, plot_color))

                #formatting the legend
                filename=str(fileName[file_index]).replace("'"," ")
                fileName_str=str(filename).split('/')
                fileName_str_length= (len(fileName_str))
                fileName_cleaned = str(fileName_str[fileName_str_length-1]).split('.')
                filename_length=(len(fileName_cleaned))
                styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold', 'font-type': 'arial'}
                graphWidget.addLegend()
                #plotting
                graphWidget.plot(array_x[:,0], array_y[:,0],pen=pen,name=fileName_cleaned[filename_length-2])
                graphWidget.setLabel('left', df_y.columns.values, **styles)
                graphWidget.setLabel('bottom', df_x.columns.values, **styles)
                graphWidget.setBackground('w')
                graphWidget.show()
                self.window.tab1.layout.addWidget(graphWidget,5,0,8,2)
                file_index=file_index+1
                plot_color = plot_color + 50
            else:
                pass

    def clr_plt_datavis(self):
        graphWidget.clear()
        global df
        df=pd.DataFrame(columns=header)

    def save_plt_datavis(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(graphWidget, "Save File", "",
                                           "All Files (*);; PNG (*.png);;TIFF (*.tiff)", options=options)
        print(file[0])
        exporter = pg.exporters.ImageExporter(graphWidget.plotItem)
        exporter.parameters()['width'] = 5000
        exporter.export(file[0])


