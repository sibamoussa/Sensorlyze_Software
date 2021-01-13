
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QFile, Qt
from PyQt5.QtGui import QIcon, QFont, QIntValidator
import sys

#from Import import OpenFile In case of importing function from another pyfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from statistics import mean
from openpyxl import Workbook


import pyqtgraph as pg
import pyqtgraph.exporters
from pyqtgraph.graphicsItems.InfiniteLine import InfLineLabel

from pyqtgraph import PlotWidget, plot
from scipy.signal import savgol_filter
from scipy import stats
from sklearn.linear_model import LinearRegression
import seaborn as sns
from open_file import *
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import sys
