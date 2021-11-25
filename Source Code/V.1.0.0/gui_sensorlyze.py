"""
Sensorlyze: Source Code Vers. 1.0.2

Copyright (c) 2021 Siba Moussa
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

This script contains the source code for Sensorlyze, a GUI developed to simplify the
process of treating biosensor data sets.

A separate class has been defined for each experiment type (Single Sensors, Multiple Sensors, Quantification , etc...) which consists of the set of functions required to process data for each type of analysis.
"""

from single_cal import * # Single Sensor Calibrations
from multiple_cal import * # Multiple Sensor Calibrations
from quant import * #Quantification
from main_win import* # Main Win
from import_modules import*
from datavis import *
import sys
import os

# def resource_path(relative_path):
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.abspath("."), relative_path)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)


global extension, filenamee
class MainWindow(QMainWindow):
    switch_window=pyqtSignal(str)
########################################### MAIN WINDOW ###################################################
    def __init__(self):
        super().__init__()
        self.InitUI()
    def InitUI(self):
        initUI(self)
    def information(self):
        information(self)
    def contact(self):
        contact(self)
    def start_clicked(self):
        start_clicked(self)
    def exp_selection_window(self):
         exp_selection_window(self)
    def exp_selection(self):
        exp_selection(self)
    def exit_clicked(self):
        exit_clicked(self)
    def msgButtonClick(self, i):
        print("Buttonclickedis:", i.text())

################# SINGLE SENSOR CALIBRATION  DATA ANALYSIS#########################################
    def windows(self):
        if self.text == 'Single Sensor Calibration':
            single_cal.win_setup(self)
################# MULTIPLE SENSOR CALIBRATION  DATA ANALYSIS#########################################
        elif self.text == 'Multiple Sensor Calibration':
            multiple_cal.win_setup(self)
################# QUANTIFICATION  DATA ANALYSIS##########################################
        elif self.text == 'Quantification':
            quant.win_setup(self)
################# DATA VISUALIZATION ( NOT JUST CHRONOAMPEROMETRY#########################################
        elif self.text == 'Data Visualization':
            datavis.win_setup(self)
################# UNDER DEVELOPMENT#########################################
        elif self.text == 'Under Development':
          self.window = QMainWindow()
          self.window.setWindowTitle('Under Development')
          #window.setGeometry(x, y, width, height)
         # self.window.setGeometry(400,300 , 600, 300)
          screen = QDesktopWidget().screenGeometry()
          size = self.geometry()
          # self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2
          self.window.setGeometry((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2, 800, 500)
          self.window.show()

########################################### SINGLE SENSOR CALIBRATION###################################################
########################### VISUALIZE DATA ############################
    def open_file_single(self):
        single_cal.open_file_single(self)
    def plot_file_single(self):
        single_cal.plot_file_single(self)
    def clr_plt_single(self):
        single_cal.clr_plt_single(self)
    def save_plt_single(self):
        single_cal.save_plt_single(self)
########################### SINGLE SENSOR ############################
    def plot_file_single_tab2(self):
        single_cal.plot_file_single_tab2(self)
    def plot_cal_single(self):
        single_cal.plot_cal_single(self)
    def regress_data(self):
        single_cal.regress_data(self)
    def export_cal_single(self):
        single_cal.export_cal_single(self)
    def plot_normal_cal_single(self):
        single_cal.plot_normal_cal_single(self)
    def export_normal_plt_single(self):
        single_cal.export_normal_plt_single(self)
    def clr_plt_single(self):
        single_cal.clr_plt_single(self)
    def save_plt_single(self):
        single_cal.save_plt_single(self)
    def sel_pts_single(self):
        single_cal.sel_pts_single(self)
    def save_cal_single(self):
        single_cal.save_cal_single(self)
    def clear_calib_single(self):
        single_cal.clear_calib_single(self)
    def save_normal_plt_single(self):
        single_cal.save_normal_plt_single(self)
    def clr_normal_plt_single(self):
        single_cal.clr_normal_plt_single(self)
    def export_plot_single(self):
        single_cal.export_plot_single(self)
    def export_all_data_single(self):
        single_cal.export_all_data_single(self)
    def apply_filter_single(self,state):
        single_cal.apply_filter_single(self,state)
########################################### MULTIPLE SENSOR CALIBRATION###################################################
    ########################### VISUALIZE DATA ############################
    def open_file_mult(self):
        multiple_cal.open_file_mult(self)
    def plot_file_mult(self):
        multiple_cal.plot_file_mult(self)
    def clr_plt(self):
        multiple_cal.clr_plt(self)
    def save_file(self):
        multiple_cal.save_file(self)
    ########################### MULTIPLE SENSOR ############################
    def plot_file_mult_tab2(self):
        multiple_cal.plot_file_mult_tab2(self)
    def append_currents(self):
        multiple_cal.append_currents(self)
    def mean_curr_checkequalarr(self):
        multiple_cal.mean_curr_checkequalarr(self)
    def plot_average_cal(self):
        multiple_cal.plot_average_cal(self)
    def save_calib(self):
        multiple_cal.save_calib(self)
    def export_plot(self):
        multiple_cal.export_plot(self)
    def plot_normalized_calib(self):
        multiple_cal.plot_normalized_calib(self)
    def export_normalized_plot(self):
        multiple_cal.export_normalized_plot(self)
    def apply_filter(self, state):
        multiple_cal.apply_filter(self, state)
    def save_normalized_calib(self):
        multiple_cal.save_normalized_calib(self)
    def export_points(self):
        multiple_cal.export_points(self)

########################################### QUANTIFICATION ###################################################
########################### VISUALIZE DATA ############################
    def open_file_quant(self):
        quant.open_file_quant(self)
    def plot_file_quant(self):
         quant.plot_file_quant(self)
    def clr_plt_quant(self):
        quant.clr_plt_quant(self)
    def save_file_quant(self):
        quant.save_file_quant(self)
########################### POINT SELECTION ############################
    def plot_file_quant_tab2(self):
        quant.plot_file_quant_tab2(self)
    def apply_filter_quant(self,state):
        quant.apply_filter_quant(self,state)
    def append_currents_quant(self):
        quant.append_currents_quant(self)
    def clear_sel_quant(self):
        quant.clear_sel_quant(self)
    def clear_sel_quant(self):
        quant.clear_sel_quant(self)
    def export_points_quant(self):
        quant.export_points_quant(self)
########################### QUANTIFICATION ############################
    def calc_conc_quant(self):
        quant.calc_conc_quant(self)
    def clr_table_quant(self):
        quant.clr_table_quant(self)
    def save_table_quant(self):
        quant.save_table_quant(self)

    ########################################### DATA VIS ###################################################

    ########################### DATA VIS ############################
    def open_file_datavis(self):
        datavis.open_file_datavis(self)
    def plot_file_datavis(self):
        datavis.plot_file_datavis(self)
    def clr_plt_datavis(self):
        datavis.clr_plt_datavis(self)
    def save_plt_datavis(self):
        datavis.save_plt_datavis(self)
########################################### FORMATTING ###################################################
#Set Windows Background Style
# stylesheet = """
#     QMainWindow {
#     background-image: url("biosensor.jpg");
#     background-repeat: no-repeat;
#     background-size: 20 px 20 px;
#     background-position:center;
#
#     }
# """

stylesheet = """
    QMainWindow {
    border-image: url("background.jpg") 0 0 0 0 stretch stretch;
    }
"""
#background - image: url("C:/Users/admin/Desktop/Sensorlyze/biosensor.jpg");


#Run Application
def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()