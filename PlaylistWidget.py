from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist
import os 
from pprint import pprint 

from MediaWidget import MediaWidget


class PlaylistWidget(QWidget):
    def __init__(self, mediaWidget, mainwindow):
        # Generate Widget
        super().__init__()
        self.list = QListWidget()
        vbox = QVBoxLayout(self)
        
        self.musicList = []
        self.list.itemDoubleClicked.connect(self.music_double_clicked)

        self.songPaths = []
        self.songPath = ""

        self.mainWindow = mainwindow
        self.mediaWidget = mediaWidget
        self.player = mediaWidget.mediaPlayer
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)

        self.mediaWidget.fastForwardButton.clicked.connect(lambda: self.next_song())
        self.mediaWidget.rewindButton.clicked.connect(lambda: self.prev_song())
        self.mediaWidget.loopButton.clicked.connect(lambda: self.loopClicked())
        self.mediaWidget.shuffleButton.clicked.connect(lambda: self.shuffleClicked())


        self.playlist.currentIndexChanged.connect(lambda: self.song_changed())
# 
        vbox.addWidget(self.list)
        self.setLayout(vbox)
    
    def song_changed(self):
        self.add_wave()
        self.mediaWidget.songPlaying.setText(self.musicList[self.playlist.currentIndex()])

        
    def add_music_item(self, songfolder):
        self.musicList = os.listdir(songfolder)

        pprint(self.musicList)

        for song in self.musicList:
            self.list.addItem(song.split('/')[-1])
            songPath = os.path.join(songfolder, song)
            self.songPaths.append(songPath)
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(songPath)))
        self.playlist.setPlaybackMode(self.playlist.Sequential)
        return self.playlist
    
    def shuffleClicked(self):
        if self.mediaWidget.isShuffling == False:
            self.playlist.setPlaybackMode(self.playlist.Sequential)
        else:
            self.playlist.setPlaybackMode(self.playlist.Random)
    
    def loopClicked(self):
        if self.mediaWidget.isLooping == False:
            self.playlist.setPlaybackMode(self.playlist.Sequential)
        else:
            self.playlist.setPlaybackMode(self.playlist.Loop)
    
    def add_wave(self):
        self.songPath = self.songPaths[self.playlist.currentIndex()]
        if self.mainWindow.subplot != None:
            self.mediaWidget.configureSongWavePlot = True
            self.mainWindow.subplot.remove() 
            self.mainWindow.matPlotWidget.draw()
    
    def music_double_clicked(self):
        music_list_index = self.list.currentRow()
        self.music_play(music_list_index)

    def music_play(self, music_list_index):
        self.playlist.setCurrentIndex(music_list_index)
        # self.add_wave()
        if self.mediaWidget.isPlaying == False:
            self.mediaWidget.playSong()
        print(self.playlist.currentMedia())
        self.player.play()
    
    def next_song(self): 
        self.playlist.setCurrentIndex(self.playlist.currentIndex() + 1)
        self.player.play()
    
    def prev_song(self):
        self.playlist.setCurrentIndex(self.playlist.currentIndex() - 1)
        self.player.play()

