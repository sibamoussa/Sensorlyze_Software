from import_modules import*
def openFile(self):
# temporary fix to show the filename
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileNames(self.window, "Import File", "",
                                                  "All Files (*);;Data Files (*.asc);;Excel Files (*.xlsx);;Text Files (*.txt)", options=options)
    return (fileName)
