import sys           
import vat as v
from PyQt4 import QtGui             


class Example(QtGui.QMainWindow):
    
    def __init__(self, c):
        super(Example, self).__init__()
        self.c=c
        self.initUI()
        
    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textEdit.setMaximumHeight(525)
        self.textEdit.setMaximumWidth(175)
        self.textEdit.setStyleSheet("border: 1px solid grey; font: 9pt 'Consolas'")
##        self.textEdit.setMaximumHeight(766)
##        self.textEdit.setMaximumWidth(1366)
        self.textEdit.setText('Введіть текст для шифрування')
        self.textEdit.textChanged.connect(self.change)
        
        self.teextEdit = QtGui.QTextEdit(self)
        self.teextEdit.move(175,55)
        self.teextEdit.setMinimumHeight(525)
        self.teextEdit.setMinimumWidth(725)
##        self.teextEdit.setDisabled(True)
        self.teextEdit.setStyleSheet("background: white; color: black; border: 1px solid grey; font: 9pt 'Consolas'")
        

        self.statusBar()

        saveFile = QtGui.QAction(QtGui.QIcon('icons/save.png'), 'Save file', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)

        clear = QtGui.QAction(QtGui.QIcon('icons/clear.png'), 'Clear', self)
        clear.setShortcut('Ctrl+S')
        clear.setStatusTip('Clear Input')
        clear.triggered.connect(self.edit_clear)

        exitAction = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        openFile = QtGui.QAction(QtGui.QIcon('icons/open.png'), 'Open...', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.file_open)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(clear)
        fileMenu.addAction(exitAction)
        
        toolbar = self.addToolBar('Панель интрументов')
        toolbar.addAction(openFile)
        toolbar.addAction(saveFile)
        toolbar.addSeparator()
        toolbar.addAction(clear)
        
        self.setGeometry(100, 100, 900, 600)
        self.setWindowTitle('tools4noobs')
        self.show()

    def change(self, decode = False):
         
         self.teextEdit.setText(self.c.multicaesar((self.textEdit.toPlainText())))
         
    def edit_clear(self):
        self.textEdit.setText('')
           
    def file_open(self):

        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
                '/home')
        
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            self.textEdit.setText(data)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.teextEdit.toPlainText()
        file.write(text)
        file.close()
                                
        
def main():
    c=v.Cezar()
    
    app = QtGui.QApplication(sys.argv)
    ex = Example(c)
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
