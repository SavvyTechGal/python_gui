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


### PlaylistWidget


<br>

## Functions

### MainWindow

#### openFolder
Upon click of Open Folder in the menu bar, this prompts the user to select a folder/directory via a QFileDialog. The selected folder is then saved to the MediaWidget's songFolder variable as a path in string form.

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

#### setSongFolder
This is the helper function called by MainWindows's openFolder function that saves the folder to songFolder.

#### playSong
Upon click of the play/pause button in the gui, this function activates. This function relies on the existance of two possible situations and performs the following for each: 
* no song is playing, but one has been loaded via clicking on a track -> Attaches the loaded song to the QMediaPlayer, plays the song, changes isPlaying to True, updates the gui to reflect that a song is playing
* there is a song that has been playing/paused -> pauses/plays the song, changes isPlaying accordingly, updates the play/pause button to reflect the change

#### handleMediaStatusChanged
This function activates the same way MainWindow's resetPlot does. This function relies on the current value of isLooping such that the following happens for its possible values
* isLooping == True -> play the song 
* isLooping == False -> update the gui to show nothing is playing, remove the song from the QMediaPlayer, sets configureSongWavePlot to True (allows for a new plot to be generated for a new song)

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


### PlaylistWidget