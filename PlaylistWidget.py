from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist
import os 
from pprint import pprint 

from MediaWidget import MediaWidget


class PlaylistWidget(QWidget):
    def __init__(self, player):
        # Generate Widget
        super().__init__()
        self.list = QListWidget()
        vbox = QVBoxLayout(self)
        
        self.musicList = []
        self.list.itemDoubleClicked.connect(self.music_double_clicked)

        self.player = player
        self.playlist = QMediaPlaylist(self.player)
        self.player.setPlaylist(self.playlist)

        vbox.addWidget(self.list)
        self.setLayout(vbox)

    def add_music_item(self, songfolder):
        dir_list = os.listdir(songfolder)

        pprint(dir_list)

        for song in dir_list:
            self.list.addItem(song.split('/')[-1])
            songPath = os.path.join(songfolder, song)
            print(songPath)
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(songPath)))
        self.playlist.setPlaybackMode(2)
        return self.playlist
    
    def music_double_clicked(self):
        music_list_index = self.list.currentRow()
        self.music_play(music_list_index)

    def music_play(self, music_list_index):
        self.playlist.setCurrentIndex(music_list_index)
        self.player.play()
