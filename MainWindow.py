
from functools import partial
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QMenuBar, QMenu, QPlainTextEdit, QFileDialog
from MediaWidget import MediaWidget
from VolumeWidget import VolumeWidget

class MainWindow(QMainWindow):
    def __init__(self):
        # Generate Window
        super().__init__()
        self.setWindowTitle("Music Player")
        # self.setFixedSize(1200, 700)
        self.setGeometry(300, 150, 350, 300)

        # MAKING THE WIDGETS self. ALLOWS OTHER OBJS TO ACCESS THESE THROUGH MainWindow, addWidget(Widget()) prevents this
        self.mediaWidget = MediaWidget()
        self.volumeWidget = VolumeWidget()

        self.mainWidget = QWidget()
        self.mainLayout = QGridLayout()
        self.mainLayout.setColumnStretch(0,3) #First param is the column number, second is the stretch factor
        self.mainLayout.setColumnStretch(1,4) 
        # self.mainLayout.setRowStretch(0,0)
        # self.mainLayout.setRowStretch(2,3)
        # self.mainLayout.setVerticalSpacing(50)
        self.mainLayout.addWidget(QPushButton("Directory Place Holder"), 0,0) #the numbers are coordiantes that correspond to a location in the grid. (row, col)
        self.mainLayout.addWidget(QPushButton("Playlist Place Holder"), 2,0)
        self.mainLayout.addWidget(QPushButton("Place Holder"), 0,1)
                
        self.mainLayout.addWidget(self.volumeWidget, 0, 3)
        self.mainLayout.addWidget(self.mediaWidget,2 ,1, 2, 3)

        menuBar = self.menuBar()
        menu = menuBar.addMenu("File")
        openFolderAction = menu.addAction("Open Folder")
        openFolderAction.triggered.connect(partial(self.openFolder,self))
        self.menuBar = menuBar

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

    # The action.connect automatically sends a MainWindow as an arg
    def openFolder(window, self): 
        # Sourced from https://stackoverflow.com/questions/4286036/how-to-have-a-directory-dialog
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(folder)



