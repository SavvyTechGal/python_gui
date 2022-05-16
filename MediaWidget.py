from functools import partial

from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QLabel, QSlider
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
import os

from math import floor

class MediaWidget(QWidget):
    def __init__(self):
        self.current_index = -1
        self.isShuffling = False
        self.isPlaying = False
        self.isLooping = False
        # This needs to update as a song continues playing
        self.currentSongProgress = QLabel()
        self.songLength = QLabel()  # When a song is loaded/pressed to play, this is changed
        self.songPlaying = QLabel()  # When a song is loaded/pressed to play, this is changed
        self.temporarySliderValue = 0
        self.configureSongWavePlot = True

        # Generate Widget
        super().__init__()

        # Generate Layout for Widget
        self.mediaLayout = QGridLayout()

        # Generate Buttons and attach to Layout
        self.shuffleButton = QPushButton("Press to Shuffle")
        self.shuffleButton.setMinimumWidth(140)
        self.shuffleButton.clicked.connect(partial(self.changeShuffling, self.shuffleButton))
        self.mediaLayout.addWidget(self.shuffleButton, 0, 0)

        self.rewindButton = QPushButton('<')
        self.mediaLayout.addWidget(self.rewindButton, 0, 1)

        self.playPauseButton = QPushButton("►")
        self.playPauseButton.setMinimumWidth(80)
        self.playPauseButton.clicked.connect(self.playSong)
        self.mediaLayout.addWidget(self.playPauseButton, 0, 2)

        self.fastForwardButton = QPushButton('>')
        self.mediaLayout.addWidget(self.fastForwardButton, 0, 3)
        

        self.loopButton = QPushButton("Press to Loop")
        self.loopButton.setMinimumWidth(130)
        self.loopButton.clicked.connect(partial(self.changeLooping, self.loopButton))
        self.mediaLayout.addWidget(self.loopButton, 0, 4)

        self.currentSongProgress.setText("--:--")
        self.mediaLayout.addWidget(self.currentSongProgress, 1, 0, 1, 1, Qt.AlignLeft)

        self.songSlider = QSlider(Qt.Horizontal)
        self.songSlider.setMinimumWidth(425)
        self.mediaLayout.addWidget(self.songSlider, 1, 0, 1, 5, Qt.AlignCenter)
        self.songSlider.sliderMoved.connect(self.changeTemporarySliderValue)
        self.songSlider.sliderReleased.connect(lambda: self.updateCurrentSongPosition())

        self.songLength.setText("--:--")
        self.mediaLayout.addWidget(self.songLength, 1, 4, 1, 1, Qt.AlignRight)

        self.songPlaying.setText("No Song Playing")
        self.songPlaying.setFont(QFont("Arial", 16))
        self.mediaLayout.addWidget(self.songPlaying, 2, 0, 1, 5, Qt.AlignCenter)

        # Finish by setting layout to the QWidget
        self.setLayout(self.mediaLayout)

        # Generate media player
        self.mediaPlayer = QMediaPlayer()

        # Configure mediaPlayer to update song progress label as song plays
        self.mediaPlayer.positionChanged.connect(lambda: self.updateCurrentSongProgress())
        # Configure mediaPlayer to update song length label when song begins playing
        self.mediaPlayer.durationChanged.connect(lambda: self.updateSongLength())

    def changeShuffling(self, button):
        if self.isShuffling:
            button.setText("Press to Shuffle")
            self.isShuffling = False
        elif not self.isShuffling:
            button.setText("Shuffling Enabled")
            self.isShuffling = True

    def changeLooping(self, button):
        if self.isLooping:
            button.setText("Press to Loop")
            self.isLooping = False
        elif not self.isLooping:
            button.setText("Looping Enabled")
            self.isLooping = True
    
    def stop_and_clear(self):
        self.mediaPlayer.pause()
        self.playPauseButton.setText('►')
        self.isPlaying = False  
        self.songPlaying.setText("No Song Playing")
        self.currentSongProgress.setText("--:--")
        self.songLength.setText("--:--")

    def playSong(self):
        # With help from https://learndataanalysis.org/source-code-how-to-play-an-audio-file-using-pyqt5-pyqt5-tutorial/
        # Play current song
        if(not self.isPlaying):
            self.mediaPlayer.play()
            self.playPauseButton.setText('||')
            self.isPlaying = True            
        # Pause current song
        elif(self.isPlaying):
            print("Paused")
            self.mediaPlayer.pause()
            self.playPauseButton.setText('►')
            self.isPlaying = False            
        # Play current song
        # elif(not self.isPlaying):
        #     print("Playing")
        #     self.mediaPlayer.play()
        #     self.playPauseButton.setText("||")
        #     self.isPlaying = True
    
    def updateCurrentSongProgress(self):
        secondsSinceStart = floor(self.mediaPlayer.position()/1000)

        seconds = str(secondsSinceStart % 60)
        if(len(seconds) == 1):
            seconds = "0" + seconds

        minutes = str(floor(secondsSinceStart/60))
        if(len(minutes) == 1):
            minutes = "0" + minutes

        self.currentSongProgress.setText(minutes+":"+seconds)

        # Update slider position as song plays as well
        self.songSlider.setValue(self.mediaPlayer.position())

    def updateSongLength(self):
        songLength = floor(self.mediaPlayer.duration()/1000)
        seconds = str(songLength % 60)
        if(len(seconds) == 1):
            seconds = "0" + seconds

        minutes = str(floor(songLength/60))
        if(len(minutes) == 1):
            minutes = "0" + minutes

        self.songLength.setText(minutes+":"+seconds)

        # Set range of slider so updating slider position as song plays works
        self.songSlider.setRange(0, self.mediaPlayer.duration())

    def changeTemporarySliderValue(self, value):
        self.temporarySliderValue = value

        secondsSinceStart = floor(value/1000)

        seconds = str(secondsSinceStart % 60)
        if(len(seconds) == 1):
            seconds = "0" + seconds

        minutes = str(floor(secondsSinceStart/60))
        if(len(minutes) == 1):
            minutes = "0" + minutes

        self.currentSongProgress.setText(minutes+":"+seconds)

    def updateCurrentSongPosition(self):
        self.mediaPlayer.setPosition(self.temporarySliderValue)
