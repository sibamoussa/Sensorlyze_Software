#This script includes functions for opening files to be used to import data

from import_modules import*

#to open a single file

def openFile(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self.window, "Import File", "",
                                                  "All Files (*);;Data Files (*.asc);;Excel Files (*.xlsx);;Text Files (*.txt)", options=options)
    return (fileName)

#to open multiple files
def openFiles(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileNames(self.window, "Import File", "",
                                                  "All Files (*);;Data Files (*.asc);;Excel Files (*.xlsx);;Text Files (*.txt)", options=options)
    return (fileName)
