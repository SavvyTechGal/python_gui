# Technical Spec

Details the functions and classes and describes what each does.

## Classes

### MainWindow
The MainWindow renders the gui for the media player and holds all widgets involved with front end and back end

### MediaWidget
The MediaWidget comprises the logic for instantiating, running, and handling certain aspects (specific PyQt5 widgets) of the media player. These aspects are: * button for play/pause
* button for shuffling a playlist
* button for looping a song
* label for song duration
* label for song progress
* slider for traversing a song 

### MatPlotWidget
The MatPlotWidget comprises the logic for instantiating a MatPlot and attaching it to a layout

### VolumeWidget
This class handles volume control of the mediaplayer. It creates volume knob and mute checkbox. The volume knob effects the volume of the track playing. The mute checkbox turns the volume knob to 0. 
The PyQT5 widgets used are:
* Dial for volume control
* Checkbox for Muting volume


### PlaylistWidget
This class creates a list of songs from the directory which is defined OpenFolder in the mainWindow. It also adds those songs to the playlist of the mediawidget player. 
It gives the option to play from directory or create your own playlist from the directory with functions (add, remove, clear, playfromplaylist).

The playlist of the mediawidget player is cleared and replaced everytime the Play From Playlist checkbox is turned off or on. 

It also handles playing by double clicking an item in the directory or playlist (depending on what it is currently playing from) and shuffling and looping through a playlist. 

The PyQT5 widgets used are:
* 2 QListWidgets -> one for directory and one for playlist creation
* QMediaPlaylist -> which takes in the mediaplayer defined in MediaWidget so it can directly manipulate the object. 
* a few buttons, and a checkbox for user playlist creation


<br>

## Functions

### MainWindow

#### openFolder
Upon click of Open Folder in the menu bar, this prompts the user to select a folder/directory via a QFileDialog. The selected folder is then saved to the MediaWidget's songFolder variable as a path in string form.

#### passVolume 
Upon volume knob change this function is called and passes the volume level to the MediaWidget mediaplayer. 

#### displaySongWave
When the position of a song, aka its progress through the duration, changes, this function activates to configure the MatPlotWidget to generate a displaywave of the song being played. For efficiency, once the function runs, it sets the MediaWidget's configureSongWavePlot to False such that it will not configure the widget every time the position changes. This is because the plot only needs to be created once per song.

#### resetPlot
When the mediaStatus variable of the QMediaPlayer in the QMediaWidget changes, this function activates. Iff the value of the variable is 7, meaning the song ended, the function executes instructions that make the plot blank.

### MediaWidget

#### changeShuffling 
Upon click of the shuffle button in the gui, this toggles the isShuffling variable from True to False and vice versa along with updating the button's text to reflect the new state of this variable.
* isShuffling value -> Button Text
  + True -> Shuffling Enabled
  + False -> Press to Shuffle

#### changeLooping 
Follows the same logic as changeShuffling, but for the isLooping variable
* isLooping value -> Button Text
  + True -> Looping Enabled
  + False -> Press to Loop

#### stop_and_clear
This function is called by the playlistWidget class when checkbox for switching between playing from directory or playing from playlist is checked/unchecked. This is to stop the player and clear all current song data. 

#### playSong
Upon click of the play/pause button in the gui, this function activates. This function relies on the existance of two possible situations and performs the following for each: 
* no song is playing, but one has been loaded via clicking on a track -> Attaches the loaded song to the QMediaPlayer, plays the song, changes isPlaying to True, updates the gui to reflect that a song is playing
* there is a song that has been playing/paused -> pauses/plays the song, changes isPlaying accordingly, updates the play/pause button to reflect the change

<!-- #### handleMediaStatusChanged
This function activates the same way MainWindow's resetPlot does. This function relies on the current value of isLooping such that the following happens for its possible values
* isLooping == True -> play the song 
* isLooping == False -> update the gui to show nothing is playing, remove the song from the QMediaPlayer, sets configureSongWavePlot to True (allows for a new plot to be generated for a new song) -->

#### updateCurrentSongProgress
This function activates the same way MainWindow's displaySongWave does. This function takes the QMediaPlayer's position variable, which is in milliseconds, and converts to the format MM:SS as a string. The result of the conversion is saved to the currentSongProgress label, which updates itself in the gui.

#### updateSongLength
When a newly loaded song is played, this function activates. It follows the same logic as updateCurrentSongProgress except it converts the QMediaPlayer's duration variable, which is in milliseconds. The result of the conversion is saved to the songLength label, which updates itself in the gui.

#### changeTemporarySliderValue
When the slider is moved by the user, this function activates. It follows the same logic as updateCurrentSongProgress except it converts the current value of the slider, which is in milliseconds. The result of the conversion is saved to the currentSongProgress label, which updates itself in the gui.
Note: as the song continues to play after this function terminates, the updateCurrentSongProgress will still activate and update the currentSongProgress label.

#### updateCurrentSongPosition
When the slider is released by the user, this function activates. It takes the current value of the slider and passes it as an arg to the QMediaPlayer's setPosition function.

### MatPlotWidget

#### getFigure
This helper function returns the value of the fig variable in the class

#### draw
This helper function calls upon the draw function of the canvas variable

### VolumeWidget

#### get_volume_level
This function changes volume dial label on dial change, and returns current volume. This function is called in mainwindow on dial change and use the passVolume function to give mediaWidget the volume it should adjust to. 

#### mute_state
This function changes volume dial to 0 if mute is checked or 10 when mute is unchecked


### PlaylistWidget

The following 3 functions for adding, removing, clearing a playlist do not work when play from playlist is checked. 
#### add_item_to_newList
Highlighted item in top directory list are added to bottom playlist when + button is clicked.

#### remove_item_from_newList
Highlighted item in bottom playlist list are removed from playlist when - button is clicked.

#### clear_newList
Clears entire playlist when 'clear playlist' button is clicked

#### playFromDirOrNewList
Adds music to playlist when play from playlist is checked or unchecked

#### song_changed
Properly updates song text and wave drawing when currentIndex is changed aka song changes

#### add_music_item
Adds music to playlist when openfolder is called in MainWindow  

#### shuffle_clicked
Randomizes playlist when isShuffle is True

#### loop_clicked
Loops entire playlist when isLooping is True

#### add_wave
Prints correct wave for song being played

#### music_double_clicked
Selects correct index to be played from double click

#### music_play
Helper function called by music_double_clicked. Plays the song double clicked on 

#### next_song
Called when next button is clicked and plays next song in playlist

#### prev_song
Called when prev button is clicked and plays prev song in playlist









