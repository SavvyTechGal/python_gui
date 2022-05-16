from PyQt5.QtWidgets import QWidget, QListWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox
from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlaylist
import os 
from pprint import pprint 

from MediaWidget import MediaWidget


class PlaylistWidget(QWidget):
    def __init__(self, mediaWidget, mainwindow):
        # Generate Widget
        super().__init__()

        vbox = QVBoxLayout(self)

        self.dir = QListWidget()
        self.list = self.dir
        self.addItemtoNewList = QPushButton("+")
        self.removeItemFromNewList = QPushButton("-")
        self.newList = QListWidget()
        self.clearNewList = QPushButton("Clear Playlist")
        self.playFromPlaylist = QCheckBox("Play from Playlist")
        self.playFromPlaylist.setChecked(False) #Automatically False
        self.playFromPlaylist.stateChanged.connect(lambda:self.playFromDirOrNewList()) #check for Mute Changes



        
        self.musicList = []

        self.songPaths = []
        self.songPath = ""
        self.songFolder = ""

        self.mainWindow = mainwindow
        self.mediaWidget = mediaWidget
        self.player = mediaWidget.mediaPlayer

        #create playlist widget and pass our mediaplayer into it
        self.playlist = QMediaPlaylist(self.player)

        #set the playlist object to the mediaplayer
        self.player.setPlaylist(self.playlist)

        
        # --- Event change functions ---

        #on list item double clicked play selected song
        self.list.itemDoubleClicked.connect(self.music_double_clicked)

        #on next button clicked call next_song
        self.mediaWidget.fastForwardButton.clicked.connect(lambda: self.next_song())

        #on prev button clicked call prev_song
        self.mediaWidget.rewindButton.clicked.connect(lambda: self.prev_song())

        #on loop button clicked call loop_clicked
        self.mediaWidget.loopButton.clicked.connect(lambda: self.loop_clicked())

        #on shuffle button clicked call shuffle_clicked
        self.mediaWidget.shuffleButton.clicked.connect(lambda: self.shuffle_clicked())

        #on CurrentIndexChanged call song_changed function
        self.playlist.currentIndexChanged.connect(lambda: self.song_changed())

        # --- Event change for New List ---
        self.addItemtoNewList.clicked.connect(lambda: self.add_item_to_newList())
        self.removeItemFromNewList.clicked.connect(lambda: self.remove_item_from_newList())
        self.clearNewList.clicked.connect(lambda: self.clear_newList())

        self.hbox_top = QHBoxLayout() 
        self.hbox_top.addWidget(self.addItemtoNewList)
        self.hbox_top.addWidget(self.removeItemFromNewList)


        self.hbox_bottom = QHBoxLayout() 
        self.hbox_bottom.addWidget(self.clearNewList)
        self.hbox_bottom.addWidget(self.playFromPlaylist)

        #Add current playlist directory to top box in mainwindow
        vbox.addWidget(self.dir)
        vbox.addLayout(self.hbox_top)
        #Add new playlist directory to bottom box in mainwindow
        vbox.addWidget(self.newList)
        vbox.addLayout(self.hbox_bottom)
        self.setLayout(vbox)

#You cannot add or remove or clear while playFromPlayList is checked
    def add_item_to_newList(self):
        if self.playFromPlaylist.isChecked():
            return
        else:
            song = self.musicList[self.list.currentRow()]
            self.newList.addItem(song.split('/')[-1])
    
    def remove_item_from_newList(self):
        if self.playFromPlaylist.isChecked():
            return
        else:
            self.newList.takeItem(self.newList.currentRow())
    
    def clear_newList(self):
        if self.playFromPlaylist.isChecked():
            return
        else:
            self.newList.clear()

    # Properly updates song text and wave drawing when currentIndex is changed 
    def song_changed(self):
        self.add_wave()
        self.mediaWidget.songPlaying.setText(self.musicList[self.playlist.currentIndex()])


    #Adds music to playlist when play from playlist is checked or unchecked
    def playFromDirOrNewList(self):
        self.mediaWidget.stop_and_clear()
        # CLEAR/RESET SUBPLOT HERE 
        # if self.mainWindow.subplot != None:
        #     self.mainWindow.subplot.remove()
        #     self.mainWindow.matPlotWidget.draw()
        #     self.mainWindow.subplot = None
        if self.list == self.dir:

            self.list = self.newList
        else:
            self.list = self.dir
        
        self.musicList =  [str(self.list.item(i).text()) for i in range(self.list.count())]
        pprint(self.musicList)
        
        self.playlist.clear()
        for song in self.musicList:
            songPath = os.path.join(self.songFolder, song)
            self.songPaths.append(songPath)
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(songPath)))
        self.playlist.setPlaybackMode(self.playlist.Sequential)


    #Adds music to playlist when openfolder is called in MainWindow  
    def add_music_item(self, songfolder):
        self.musicList = os.listdir(songfolder)
        self.songFolder = songfolder
        pprint(self.musicList)

        for song in self.musicList:
            self.list.addItem(song.split('/')[-1])
            songPath = os.path.join(songfolder, song)
            self.songPaths.append(songPath)
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(songPath)))
        self.playlist.setPlaybackMode(self.playlist.Sequential)
        return self.playlist
    
    #Randomizes playlist when isShuffle is True
    def shuffle_clicked(self):
        if self.mediaWidget.isShuffling == False:
            self.playlist.setPlaybackMode(self.playlist.Sequential)
        else:
            self.playlist.setPlaybackMode(self.playlist.Random)
    
    #Loops entire playlist when isLooping is True
    def loop_clicked(self):
        if self.mediaWidget.isLooping == False:
            self.playlist.setPlaybackMode(self.playlist.Sequential)
        else:
            self.playlist.setPlaybackMode(self.playlist.Loop)
    
    #Prints correct wave for song being played
    def add_wave(self):
        self.songPath = self.songPaths[self.playlist.currentIndex()]
        if self.mainWindow.subplot != None:
            self.mediaWidget.configureSongWavePlot = True
            self.mainWindow.subplot.remove() 
            self.mainWindow.matPlotWidget.draw()
    
    #Selects correct index to be played from double click 
    def music_double_clicked(self):
        music_list_index = self.list.currentRow()
        self.music_play(music_list_index)

    #Plays the song double clicked on 
    def music_play(self, music_list_index):
        self.playlist.setCurrentIndex(music_list_index)
        if self.mediaWidget.isPlaying == False:
            self.mediaWidget.playSong()
        print(self.playlist.currentMedia())
        self.player.play()
    
    #Called when clicking next button
    def next_song(self): 
        self.playlist.setCurrentIndex(self.playlist.currentIndex() + 1)
        self.player.play()
    
    #Called when clicking prev button
    def prev_song(self):
        self.playlist.setCurrentIndex(self.playlist.currentIndex() - 1)
        self.player.play()

