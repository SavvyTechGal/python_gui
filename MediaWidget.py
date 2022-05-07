from functools import partial

from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QScrollBar, QLabel, QSlider
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont

class MediaWidget(QWidget):
    def __init__(self):
        self.isShuffling = False
        self.isPlaying = True
        self.isLooping = False
        self.currentSongProgress = QLabel() # This needs to update as a song continues playing
        self.songLength = QLabel() # When a song is loaded/pressed to play, this is changed
        self.songPlaying = QLabel() # When a song is loaded/pressed to play, this is changed
        
        # Generate Widget
        super().__init__()
        
        # Generate Layout for Widget
        self.mediaLayout = QGridLayout()
        
        # Generate Buttons and attach to Layout
        self.shuffleButton = QPushButton("Press to Shuffle")
        self.shuffleButton.clicked.connect(partial(self.changeShuffling, self.shuffleButton))
        self.mediaLayout.addWidget(self.shuffleButton, 0, 0)

        self.rewindButton = QPushButton("Prev Song")
        self.mediaLayout.addWidget(self.rewindButton, 0, 1)

        self.playPauseButton = QPushButton("Play")
        self.playPauseButton.clicked.connect(partial(self.changePlayPause, self.playPauseButton))
        self.mediaLayout.addWidget(self.playPauseButton, 0, 2)

        self.fastForwardButton = QPushButton("Next Song")
        self.mediaLayout.addWidget(self.fastForwardButton, 0, 3)

        self.loopButton = QPushButton("Press to Loop")
        self.loopButton.clicked.connect(partial(self.changeLooping, self.loopButton))
        self.mediaLayout.addWidget(self.loopButton, 0, 4)

        self.currentSongProgress.setText("--:--")
        self.mediaLayout.addWidget(self.currentSongProgress, 1, 0, 1, 1, Qt.AlignLeft)

        self.songSlider = QSlider(Qt.Horizontal)
        self.songSlider.setMinimumWidth(425)
        self.mediaLayout.addWidget(self.songSlider, 1, 0, 1, 5, alignment = Qt.AlignCenter)

        self.songLength.setText("--:--")
        self.mediaLayout.addWidget(self.songLength, 1, 4, 1, 1, alignment= Qt.AlignRight)
        
        self.songPlaying.setText("No Song Playing")
        self.songPlaying.setFont(QFont("Arial",16))
        self.mediaLayout.addWidget(self.songPlaying, 2, 0, 1, 5, Qt.AlignCenter)

        # Finish by setting layout to the QWidget
        self.setLayout(self.mediaLayout)

    def changeShuffling(self,button):
        if self.isShuffling:
            button.setText("Press to Shuffle")
            self.isShuffling = False
        elif not self.isShuffling:
            button.setText("Shuffling Enabled")
            self.isShuffling = True

    def changePlayPause(self, button):
        if self.isPlaying:
            button.setText("Pause")
            self.isPlaying = False
        elif not self.isPlaying:
            button.setText("Play")
            self.isPlaying = True

    def changeLooping(self, button):
        if self.isLooping:
            button.setText("Press to Loop")
            self.isLooping = False
        elif not self.isLooping:
            button.setText("Looping Enabled")
            self.isLooping = True