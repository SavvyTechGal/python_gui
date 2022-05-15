from PyQt5.QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout, QScrollBar, QLabel, QSlider
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

from MediaWidget import MediaWidget


class PlaylistWidget(QWidget):
    def __init__(self):
        self.player = MediaWidget()
        self.playlist = QMediaPlaylist(self.player)
    
    def setMediaWidget(self, media_player):
        self.player = media_player