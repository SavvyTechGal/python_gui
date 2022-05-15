from functools import partial

from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QScrollBar, QLabel, QSlider
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys
import os

from math import floor

class MediaWidget(QWidget):
    def __init__(self):
        self.isShuffling = False
        self.isPlaying = False
        self.isLooping = False
        # This needs to update as a song continues playing
        self.currentSongProgress = QLabel()
        self.songLength = QLabel()  # When a song is loaded/pressed to play, this is changed
        self.songPlaying = QLabel()  # When a song is loaded/pressed to play, this is changed
        self.songFolder = ""
        self.songPath = ""

        # Generate Widget
        super().__init__()

        # Generate Layout for Widget
        self.mediaLayout = QGridLayout()

        # Generate Buttons and attach to Layout
        self.shuffleButton = QPushButton("Press to Shuffle")
        self.shuffleButton.clicked.connect(partial(self.changeShuffling, self.shuffleButton))
        self.mediaLayout.addWidget(self.shuffleButton, 0, 0)

        self.rewindButton = QPushButton('<')
        self.mediaLayout.addWidget(self.rewindButton, 0, 1)

        self.playPauseButton = QPushButton('►')
        self.playPauseButton.clicked.connect(self.playSong)
        self.mediaLayout.addWidget(self.playPauseButton, 0, 2)

        self.fastForwardButton = QPushButton('>')
        self.mediaLayout.addWidget(self.fastForwardButton, 0, 3)

        self.loopButton = QPushButton("Press to Loop")
        self.loopButton.clicked.connect(partial(self.changeLooping, self.loopButton))
        self.mediaLayout.addWidget(self.loopButton, 0, 4)

        self.currentSongProgress.setText("--:--")
        self.mediaLayout.addWidget(self.currentSongProgress, 1, 0, 1, 1, Qt.AlignLeft)

        self.songSlider = QSlider(Qt.Horizontal)
        self.songSlider.setMinimumWidth(425)
        self.mediaLayout.addWidget(self.songSlider, 1, 0, 1, 5, Qt.AlignCenter)

        self.songLength.setText("--:--")
        self.mediaLayout.addWidget(self.songLength, 1, 4, 1, 1, Qt.AlignRight)

        self.songPlaying.setText("No Song Playing")
        self.songPlaying.setFont(QFont("Arial",16))
        self.mediaLayout.addWidget(self.songPlaying, 2, 0, 1, 5, Qt.AlignCenter)

        # Finish by setting layout to the QWidget
        self.setLayout(self.mediaLayout)

        # Generate media player
        self.mediaPlayer = QMediaPlayer()
        # Handler for certain changes in mediaStatus as mediaPlayer runs
        self.mediaPlayer.mediaStatusChanged.connect(self.handleMediaStatusChanged)
        # Configure mediaPlayer to update song progress label as song plays
        self.mediaPlayer.positionChanged.connect(self.updateCurrentSongProgress)
        # Configure mediaPlayer to update song length label when song begins playing
        self.mediaPlayer.durationChanged.connect(self.updateSongLength)

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

    def setSongFolder(self, folder):
        self.songFolder = folder
        print(self.songFolder)

    def playSong(self):
        # With help from https://learndataanalysis.org/source-code-how-to-play-an-audio-file-using-pyqt5-pyqt5-tutorial/
        # When playing a song for the first time
        if(not self.isPlaying and self.songPath == ""):
            folder = self.songFolder # THIS WILL BE self.songFolder
            song = "Japanese House - Saw You in a Dream.mp3" # THIS WILL COME FROM THE SELECTION IN THE PLAYLIST

            self.songPath = os.path.join(folder, song) # THIS WILL JOIN self.songFolder AND TRACK SELECTED FROM PLAYLIST
            url = QUrl.fromLocalFile(self.songPath)
            # print(url) Shows how PyQt sees a selected file
            content = QMediaContent(url)
            self.mediaPlayer.setMedia(content)
            self.mediaPlayer.play()

            self.playPauseButton.setText('||')
            self.songPlaying.setText(song) # THIS CAN BE INSTEAD DONE WHEN A SONG IS SELECTED
            self.isPlaying = True            
        # Pause current song
        elif(self.isPlaying):
            print("Paused")
            self.mediaPlayer.pause()
            self.playPauseButton.setText('►')
            self.isPlaying = False            
        # Play current song
        elif(not self.isPlaying):
            print("Playing")
            self.mediaPlayer.play()
            self.playPauseButton.setText("||")
            self.isPlaying = True

        #print(self.mediaPlayer.mediaStatus())

    def handleMediaStatusChanged(self, mediaStatus):
        # When the song ends, mediastatus is changed to 7 is sent according to documentation
        if mediaStatus == 7:
            # Loop current song
            if self.isLooping:
                self.mediaPlayer.play()
            # Reset player
            else:
                self.playPauseButton.setText('►')
                self.isPlaying = False
                self.currentSongProgress.setText("--:--")
                self.songLength.setText("--:--")
                self.songPlaying.setText("No Song Playing")
                self.songPath = ""
                self.mediaPlayer.setMedia(QMediaContent(None))

    def updateCurrentSongProgress(self):
        secondsSinceStart = floor(self.mediaPlayer.position()/1000)
        result = ""
        
        seconds = str(secondsSinceStart%60)
        if(len(seconds) == 1):
            seconds = "0" +seconds
        
        minutes = str(floor(secondsSinceStart/60))
        if(len(minutes) == 1):
            minutes = "0" + minutes
        
        result = minutes+":"+seconds
        self.currentSongProgress.setText(result)

        #LIKELY HAVE TO UPDATE THE SLIDER'S POSITION HERE AS WELL

    def updateSongLength(self):
        songLength = floor(self.mediaPlayer.duration()/1000)
        result = ""
        
        seconds = str(songLength % 60)
        if(len(seconds) == 1):
            seconds = "0" + seconds
        
        minutes = str(floor(songLength/60))
        if(len(minutes) == 1):
            minutes = "0" + minutes
        
        result = minutes+":"+seconds
        self.songLength.setText(result)
