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

        self.mediaWidget.playPauseButton.clicked.connect(lambda: self.add_wave())
        self.mediaWidget.fastForwardButton.clicked.connect(lambda: self.next_song())
        self.mediaWidget.rewindButton.clicked.connect(lambda: self.prev_song())
        self.player.mediaStatusChanged.connect(lambda: self.resetPlot(self.player.mediaStatus()))


        vbox.addWidget(self.list)
        self.setLayout(vbox)

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
    
    def add_wave(self):
        self.songPath = self.songPaths[self.playlist.currentIndex()]
        if self.mainWindow.subplot != None:
            self.mediaWidget.configureSongWavePlot = True
            self.mainWindow.subplot.remove() 
            self.mainWindow.matPlotWidget.draw()
    
    def resetPlot(self, mediaStatus):
        # When the song ends, mediastatus is changed to 7 is sent according to documentation
        if mediaStatus == 7 and not self.mediaWidget.isLooping:
            self.add_wave()
    
    def music_double_clicked(self):
        music_list_index = self.list.currentRow()
        self.music_play(music_list_index)

    def music_play(self, music_list_index):
        self.playlist.setCurrentIndex(music_list_index)

        self.mediaWidget.songPlaying.setText(self.musicList[self.playlist.currentIndex()])
        self.add_wave()
        self.player.play()
    
    def next_song(self): 
        self.playlist.setCurrentIndex(self.playlist.currentIndex() + 1)
        
        self.add_wave()
        self.player.play()
    
    def prev_song(self):
        self.playlist.setCurrentIndex(self.playlist.currentIndex() - 1)
        
        self.add_wave() 
        self.player.play()

