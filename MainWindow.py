from functools import partial
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QGridLayout, QFileDialog, QVBoxLayout
from PyQt5.QtMultimedia import QMediaPlaylist
from MediaWidget import MediaWidget
from VolumeWidget import VolumeWidget
from PlaylistWidget import PlaylistWidget
from MatPlotWidget import MatplotWidget
import wave
import numpy as np
from pydub import AudioSegment

class MainWindow(QMainWindow):
    def __init__(self):
        # Generate Window
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(300, 150, 1000, 400)

        # MAKING THE WIDGETS self. ALLOWS OTHER OBJS TO ACCESS THESE THROUGH MainWindow, addWidget(Widget()) prevents this
        self.mediaWidget = MediaWidget()
        self.volumeWidget = VolumeWidget()
        self.playlistWidget = PlaylistWidget(self.mediaWidget, self)

        #Change Volume Label as Dial is turned and pass correct volume level to media widget
        self.volumeWidget.dial.valueChanged.connect(lambda: self.passVolume(self.volumeWidget.get_volume_level()))

        self.mediaWidget.mediaPlayer.positionChanged.connect(lambda: self.displaySongWave())

        self.mainWidget = QWidget()
        self.mainLayout = QGridLayout()
        # First param is the column number, second is the stretch factor
        self.mainLayout.setColumnStretch(0, 4)
        self.mainLayout.setColumnStretch(1, 4)

        # the numbers are coordiantes that correspond to a location in the grid. (row, col)
        self.mainLayout.addWidget(self.playlistWidget, 0, 0, 3, 1, Qt.AlignLeft)

        self.matPlotWidget = MatplotWidget()
        self.subplot = None
        self.matPlotWidget.draw()
        self.mainLayout.addWidget(self.matPlotWidget, 0, 1, 2, 1)

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
        self.playlistWidget.add_music_item(folder)
    
    def passVolume(self, value: int):
        self.mediaWidget.mediaPlayer.setVolume(value)

    def displaySongWave(self):
        if self.playlistWidget.songPath != "":
            if self.mediaWidget.configureSongWavePlot:
                if self.playlistWidget.songPath[-3:] == "wav":  
                    # Sourced from https://www.geeksforgeeks.org/plotting-various-sounds-on-graphs-using-python-and-matplotlib/
                    wave_obj = wave.open(self.playlistWidget.songPath,'rb')
                    freq = wave_obj.getframerate()
                    signal = wave_obj.readframes(-1)
                    signal = np.frombuffer(signal, dtype="int16")
                    time = np.linspace(0,len(signal)/freq,num = len(signal))
                    
                elif self.playlistWidget.songPath[-3:] == "mp3":
                    # With help from https://stackoverflow.com/questions/16634128/how-to-extract-the-raw-data-from-a-mp3-file-using-python 
                    sound = AudioSegment.from_mp3(self.playlistWidget.songPath)
                    freq = sound.frame_rate
                    signal = bytes(sound.raw_data)
                    signal = np.frombuffer(signal, dtype="int16")
                    time = np.linspace(0, len(signal)/freq, num=len(signal))

                else:
                    print("Unsupported file type provided, Matplot not configured")
                    self.mediaWidget.configureSongWavePlot = False
                    return

                # With help from same link for creating the MatLib widget
                self.subplot = self.matPlotWidget.getFigure().add_subplot(111)
                self.subplot.plot(time,signal)
                
                # With help from https://stackoverflow.com/questions/14908576/how-to-remove-frame-from-matplotlib-pyplot-figure-vs-matplotlib-figure-frame
                self.subplot.axis("off")
                
                self.matPlotWidget.draw()

                # Prevents the plot from remaking itself every time the position changes
                self.mediaWidget.configureSongWavePlot= False

