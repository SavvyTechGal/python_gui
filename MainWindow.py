from functools import partial
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QFileDialog, QVBoxLayout
from MediaWidget import MediaWidget
from VolumeWidget import VolumeWidget
from MatPlotWidget import MatplotWidget
import wave
import numpy as np
from pydub import AudioSegment

class MainWindow(QMainWindow):
    def __init__(self):
        # Generate Window
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(300, 150, 900, 300)

        # MAKING THE WIDGETS self. ALLOWS OTHER OBJS TO ACCESS THESE THROUGH MainWindow, addWidget(Widget()) prevents this
        self.mediaWidget = MediaWidget()
        self.volumeWidget = VolumeWidget()
        print(self.volumeWidget.get_volume_level())

        #Change Volume Label as Dial is turned and pass correct volume level to media widget
        self.volumeWidget.dial.valueChanged.connect(lambda: self.passVolume(self.volumeWidget.get_volume_level()))

        self.mediaWidget.mediaPlayer.positionChanged.connect(self.displaySongWave)
        self.mediaWidget.mediaPlayer.mediaStatusChanged.connect(self.resetPlot)

        self.mainWidget = QWidget()
        self.mainLayout = QGridLayout()
        # First param is the column number, second is the stretch factor
        self.mainLayout.setColumnStretch(0, 3)
        self.mainLayout.setColumnStretch(1, 4)

        # the numbers are coordiantes that correspond to a location in the grid. (row, col)
        self.mainLayout.addWidget(QPushButton("Directory Place Holder"), 0, 0)
        self.mainLayout.addWidget(QPushButton("Playlist Place Holder"), 2, 0)

        self.matPlotWidget = MatplotWidget()
        self.subplot = None
        self.matPlotWidget.draw()
        #self.mainLayout.addWidget(QPushButton("Place Holder"), 0, 1)
        self.mainLayout.addWidget(self.matPlotWidget, 0, 1, 1, 2)

        self.mainLayout.addWidget(self.volumeWidget, 0, 3)
        self.mainLayout.addWidget(self.mediaWidget, 2, 1, 2, 3)

        menuBar = self.menuBar()
        menu = menuBar.addMenu("File")
        openFolderAction = menu.addAction("Open Folder")
        openFolderAction.triggered.connect(lambda: self.openFolder())
        self.menuBar = menuBar

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

    # The action.connect automatically sends a MainWindow as an arg
    def openFolder(self):
        # Sourced from https://stackoverflow.com/questions/4286036/how-to-have-a-directory-dialog
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.mediaWidget.setSongFolder(folder)
        print(self.mediaWidget.songFolder)
        #PERHAPS LINK THE FOLDER TO THE PLAYLIST via # os.listdir(folder)
    
    def passVolume(self, value: int):
        self.mediaWidget.mediaPlayer.setVolume(value)

    def displaySongWave(window):
        if window.mediaWidget.configureSongWavePlot:
            if window.mediaWidget.songPath[-3:] == "wav":            
                # Sourced from https://www.geeksforgeeks.org/plotting-various-sounds-on-graphs-using-python-and-matplotlib/
                wave_obj = wave.open(window.mediaWidget.songPath,'rb')
                freq = wave_obj.getframerate()
                signal = wave_obj.readframes(-1)
                signal = np.frombuffer(signal, dtype="int16")
                time = np.linspace(0,len(signal)/freq,num = len(signal))
                
            elif window.mediaWidget.songPath[-3:] == "mp3":
                # With help from https://stackoverflow.com/questions/16634128/how-to-extract-the-raw-data-from-a-mp3-file-using-python 
                sound = AudioSegment.from_mp3(window.mediaWidget.songPath)
                freq = sound.frame_rate
                signal = bytes(sound.raw_data)
                signal = np.frombuffer(signal, dtype="int16")
                time = np.linspace(0, len(signal)/freq, num=len(signal))

            else:
                print("Unsupported file type provided, Matplot not configured")
                window.mediaWidget.configureSongWavePlot = False
                return

            # With help from same link for creating the MatLib widget
            window.subplot = window.matPlotWidget.getFigure().add_subplot(111)
            window.subplot.plot(time,signal)
            
            # With help from https://stackoverflow.com/questions/14908576/how-to-remove-frame-from-matplotlib-pyplot-figure-vs-matplotlib-figure-frame
            window.subplot.axis("off")
            
            window.matPlotWidget.draw()

            # Prevents the plot from remaking itself every time the position changes
            window.mediaWidget.configureSongWavePlot= False
            
    def resetPlot(self, mediaStatus):
        # When the song ends, mediastatus is changed to 7 is sent according to documentation
        if mediaStatus == 7 and not self.mediaWidget.isLooping:
            self.subplot.remove()
            self.matPlotWidget.draw()

