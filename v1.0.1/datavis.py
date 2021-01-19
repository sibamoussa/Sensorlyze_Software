from import_modules import*
##This class is responsible for visualizing data
class datavis():

    def open_file_datavis(self):
        global fileName,extension
        fileName = openFile(self)

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
            self.window.tab4 = QWidget(self.window)

            self.window.tabWidget.addTab(self.window.tab1, "Visualize Data")
            self.window.tabWidget.addTab(self.window.tab2, "Manipulate Data")
            self.window.tabWidget.addTab(self.window.tab3, "Formatting")


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
                global filename2
                extension2=[]
                for i in fileName:
                    fileName2=str(fileName)
                    name, extension = os.path.splitext(fileName2)
                    extension2.append(extension)
                global df
                format_check = False;
                if len(extension2) > 0:
                    format_check = all(elem == extension2[0] for elem in extension2)
                if format_check:
                    filetype_selection = filelist.currentText()
                    if filetype_selection == "HEKA (.asc)":
                        if '.asc' in extension2[0] :
                            global header, indexes
                            header=[]
                            data = []
                            df=[]
                            indexes=[]

                            for x in fileName:
                                styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold',
                                          'font-type': 'arial'}
                                with open(x, 'r') as fh:
                                    for curline in fh:
                                        if curline[0]=='"':
                                            curline = curline.strip('\n').split('\t')
                                            header=curline
                                        else:
                                            pass
                                fh.close()
                                with open(x, 'r') as fh:
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
                            df.columns = df.columns.str.replace("]", '')
                            df.columns = df.columns.str.replace('"', '')
                            df.columns = df.columns.str.replace("[", '/')

                    elif filetype_selection == "Biologic (.txt)":
                            if '.txt' in extension2[0]:
                                header = []
                                data = []
                                df = []
                                indexes = []
                                for x in fileName:
                                    styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold',
                                              'font-type': 'arial'}
                                    with open(x, 'r') as fh:
                                        for curline in fh:
                                            if curline[0] == 'm':
                                                curline = curline.split('\t')
                                                curline=[item.replace('>','') for item in curline]
                                                curline=[item.replace('<','') for item in curline]

                                                header = curline
                                            else:
                                                pass
                                    fh.close()
                                    with open(x, 'r') as fh:
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

                                    colsdata = len(data[0])
                                    colsdata3 =len(header)
                                    if colsdata!=colsdata3 :
                                        del header[-1]
                                    else:
                                        pass

                                    headercap = [val.capitalize() for val in header]

                                    print(headercap)
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
            xaxis_selection = ["", "Emon","Imon","Time","I","Ewe","E", "Current","Potential"]
            xaxis_list.addItems(xaxis_selection)

            def xaxis_sel1(self):
                global xaxis_sel
                xaxis_sel = xaxis_list.currentText()
                print(xaxis_sel)

            xaxis_list.activated[int].connect(xaxis_sel1)


            self.window.tab1.layout.addWidget(xaxis_list, 2, 1)
            # Select y axis
            select_y_axis = QLabel('S elect Y-Axis:')
            self.window.tab1.layout.addWidget(select_y_axis, 3, 0)
            select_y_axis.setAlignment(Qt.AlignRight)

            yaxis_list = QComboBox(self.window)
            yaxis_selection = ["", "Emon","Imon","Time","I","Ewe","E", "Current","Potential"]

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

##
###Display all tabs
            self.window.tab1.setLayout(self.window.tab1.layout)
            self.window.show()


            # ###Display all tabs
            self.window.tab2.setLayout(self.window.tab2.layout)
            self.window.show()
    ######################## BASIC FILE VISUALIZATION ##########################

    def plot_file_datavis(self):
        df2 = df.filter(regex=xaxis_sel)
        df2 = df2.loc[:, ~df2.columns.duplicated()]
        df3=df.filter(regex=yaxis_sel)
        df3=df3.loc[:,~df3.columns.duplicated()]
        df_new=df2.join(df3)
        print(df_new)
        #print(df_new)
        dfs=np.split(df_new,indexes)
        font = QFont()
        penn= pg.mkPen(color='k', width=2)
        font.setBold(False)
        font.setPixelSize(25)
        global graphWidget
        graphWidget = pg.PlotWidget(self.window)
        n=0
        i=0
        ind=(len(indexes))
        print(ind)
        for array in dfs:
            if n <= ind-1:
                arrayx=array.filter(regex=xaxis_sel)
                arrrayx=arrayx.values

                arrayy=array.filter(regex=yaxis_sel)
                arrrayy = arrayy.values
                graphWidget.getAxis('bottom').setTickFont(font)
                graphWidget.getAxis('left').setTickFont(font)
                graphWidget.getAxis('bottom').setStyle(tickTextOffset=10)
                graphWidget.getAxis('left').setStyle(tickTextOffset=5)
                graphWidget.getAxis('left').setPen(penn)
                pen = pg.mkPen(color=(125+i, 50+i, i))
                fileNamee=str(fileName[n]).replace("'"," ")
                fileName2=str(fileNamee).split('/')
                ss = (len(fileName2))
                fileName3 = str(fileName2[ss-1]).split('.')
                s=(len(fileName3))
                styles = {'color': 'k', 'font-size': '30px', 'font-weight': 'bold', 'font-type': 'arial'}
                graphWidget.addLegend()
                print(fileName3)
                graphWidget.plot(arrrayx[:,0], arrrayy[:,0],pen=pen,name=fileName3[s-2])
                n=n+1
                i = i + 50
                graphWidget.setLabel('left', df3.columns.values, **styles)
                graphWidget.setLabel('bottom', df2.columns.values, **styles)
                graphWidget.setBackground('w')
                graphWidget.show()
                self.window.tab1.layout.addWidget(graphWidget,5,0,8,2)
            else:
                pass

    def clr_plt_datavis(self):
        graphWidget.clear()
        global df
        df=pd.DataFrame(columns=header)

    def save_plt_datavis(self):
        # temporary fix to show the filename
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file = QFileDialog.getSaveFileName(graphWidget, "Save File", "",
                                           "All Files (*);; PNG (*.png);;TIFF (*.tiff)", options=options)
        print(file[0])
        exporter = pg.exporters.ImageExporter(graphWidget.plotItem)
        exporter.parameters()['width'] = 5000
        exporter.export(file[0])


