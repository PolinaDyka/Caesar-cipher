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
        self.textEdit.setMaximumHeight(210)
        self.textEdit.setMaximumWidth(600)
##        self.textEdit.setMaximumHeight(766)
##        self.textEdit.setMaximumWidth(1366)
        self.textEdit.setText('Введіть текст для шифрування')
        self.textEdit.textChanged.connect(self.change)
        
        self.teextEdit = QtGui.QTextEdit(self)
        self.teextEdit.move(0,280)
        self.teextEdit.setMinimumHeight(200)
        self.teextEdit.setMinimumWidth(600)
        self.teextEdit.setMaximumHeight(766)
        self.teextEdit.setMaximumWidth(1366)
##        self.teextEdit.setDisabled(True)
        self.teextEdit.setStyleSheet("background: white; color: black")
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

        self.combo = QtGui.QComboBox(self)
        self.combo.addItem("Encrypt")
        self.combo.addItem("Decrypt")
        self.combo.activated[str].connect(self.onActivated)
        self.combo.setStyleSheet("margin-left: 5px; padding-left: 4px")

        key = QtGui.QLabel()
        key.setFixedSize(40,40)
        key.setStyleSheet("image: url(icons/key.png); margin-left: 7px; margin-top: -3px")
 
        self.keyEdit = QtGui.QLineEdit()
        self.keyEdit.setMaximumHeight(25)
        self.keyEdit.setMaximumWidth(100)
##        self.keyEdit.setText('1')
        self.keyEdit.setStyleSheet("margin-left: 2px; border:  1px solid")
        self.keyEdit.setValidator(QtGui.QIntValidator())
        self.keyEdit.textChanged.connect(self.change)

        swapper = QtGui.QAction(QtGui.QIcon('icons/swap.png'), 'Swap', self)
        swapper.setStatusTip('Swap text from inputs')
        swapper.triggered.connect(self.swap)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(clear)
        fileMenu.addAction(swapper)
        fileMenu.addAction(exitAction)
        
        toolbar = self.addToolBar('Панель интрументов')
        toolbar.addAction(openFile)
        toolbar.addAction(saveFile)
        toolbar.addSeparator()
        toolbar.addAction(swapper)
        toolbar.addWidget(self.combo)
        toolbar.addWidget(key)
        toolbar.addWidget(self.keyEdit)
        
        
        self.setGeometry(100, 100, 600, 500)
        self.setWindowTitle('tools4noobs')
        self.show()

    def change(self, decode = False):
         if self.combo.currentText() == 'Encrypt': decode = False
         self.teextEdit.setText(self.c.caesar(self.textEdit.toPlainText(), int(self.keyEdit.text()), decode))

    def edit_clear(self):
        self.textEdit.setText('')

    def swap(self):
        swap = self.textEdit.toPlainText()
        self.textEdit.setText(self.teextEdit.toPlainText())
        self.teextEdit.setText(swap)
        if self.combo.currentIndex() == 0:
            self.combo.setCurrentIndex(1)
        else: self.combo.setCurrentIndex(0)
          
        
        
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

    def onActivated(self, text):
        if (text=="Decrypt"):
            self.change(True)
        else: self.change()

                                
        
def main():
    c=v.Cezar()
    
    app = QtGui.QApplication(sys.argv)
    ex = Example(c)
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
    
