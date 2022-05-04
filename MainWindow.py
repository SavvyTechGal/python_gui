
from VolumeWidget import VolumeWidget
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QGridLayout, QDial
from MediaWidget import MediaWidget
# from VolumeWidget import VolumeWidget

class MainWindow(QMainWindow):
    def __init__(self):
        # Generate Window
        super().__init__()
        self.setWindowTitle("Music Player")
        # self.setFixedSize(1200, 700)
        self.setGeometry(300, 150, 350, 300)

        self.mainWidget = QWidget()
        self.mainLayout = QGridLayout()
        self.mainLayout.setColumnStretch(0,3) #First param is the column number, second is the stretch factor
        self.mainLayout.setColumnStretch(1,4) 
        # self.mainLayout.setRowStretch(0,0)
        # self.mainLayout.setRowStretch(2,3)
        # self.mainLayout.setVerticalSpacing(50)
        self.mainLayout.addWidget(QPushButton("Directory Place Holder"), 0,0) #the numbers are coordiantes that correspond to a location in the grid. (row, col)
        self.mainLayout.addWidget(QPushButton("Playlist Place Holder"), 2,0)
        self.mainLayout.addWidget(VolumeWidget(), 0,1)
        self.mainLayout.addWidget(MediaWidget(),2,1, 4,1)

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)