from functools import partial
import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QGridLayout

class MediaWidget(QWidget):
    def __init__(self):
        self.isShuffling = 0
        self.isPlaying = 1
        self.isLooping = 0
        
        # Generate Widget
        super().__init__()
        
        # Generate Layout for Widget
        self.mediaLayout = QHBoxLayout()
        
        # Generate Buttons and attach to Layout
        self.shuffleButton = QPushButton("Press to Shuffle")
        self.shuffleButton.clicked.connect(partial(self.changeShuffling,self.shuffleButton))
        self.mediaLayout.addWidget(self.shuffleButton)

        self.playPauseButton = QPushButton("Play")
        self.playPauseButton.clicked.connect(partial(self.changePlayPause,self.playPauseButton))
        self.mediaLayout.addWidget(self.playPauseButton)

        self.loopButton = QPushButton("Press to Loop")
        self.loopButton.clicked.connect(partial(self.changeLooping,self.loopButton))
        self.mediaLayout.addWidget(self.loopButton)

        # Finish by setting layout to the QWidget
        self.setLayout(self.mediaLayout)

    def changeShuffling(self,button):
        if self.isShuffling:
            button.setText("Press to Shuffle")
            self.isShuffling = 0
        elif not self.isShuffling:
            button.setText("Shuffling Enabled")
            self.isShuffling = 1

    def changePlayPause(self, button):
        if self.isPlaying:
            button.setText("Pause")
            self.isPlaying = 0
        elif not self.isPlaying:
            button.setText("Play")
            self.isPlaying = 1

    def changeLooping(self, button):
        if self.isLooping:
            button.setText("Press to Loop")
            self.isLooping = 0
        elif not self.isLooping:
            button.setText("Looping Enabled")
            self.isLooping = 1

class MainWindow(QMainWindow):
    def __init__(self):
        # Generate Window
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setFixedSize(1200, 700)

        
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(MediaWidget())

        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())