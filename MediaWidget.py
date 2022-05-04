from functools import partial
from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout

class MediaWidget(QWidget):
    def __init__(self):
        self.isShuffling = 0
        self.isPlaying = 1
        self.isLooping = 0
        
        # Generate Widget
        super().__init__()
        
        # Generate Layout for Widget
        self.mediaLayout = QGridLayout()
        
        # Generate Buttons and attach to Layout
        self.shuffleButton = QPushButton("Press to Shuffle")
        self.shuffleButton.clicked.connect(partial(self.changeShuffling,self.shuffleButton))
        self.mediaLayout.addWidget(self.shuffleButton, 0, 0)

        self.rewindButton = QPushButton("Prev Song")
        self.mediaLayout.addWidget(self.rewindButton, 0, 1)

        self.playPauseButton = QPushButton("Play")
        self.playPauseButton.clicked.connect(partial(self.changePlayPause,self.playPauseButton))
        self.mediaLayout.addWidget(self.playPauseButton, 0, 2)

        self.fastForwardButton = QPushButton("Next Song")
        self.mediaLayout.addWidget(self.fastForwardButton, 0, 3)

        self.loopButton = QPushButton("Press to Loop")
        self.loopButton.clicked.connect(partial(self.changeLooping,self.loopButton))
        self.mediaLayout.addWidget(self.loopButton, 0, 4)

        self.mediaLayout.addWidget(QPushButton("music scroll placeholder"), 1,0, 1,5)

        # Finish by setting layout to the QWidget
        self.setLayout(self.mediaLayout)

    def changeShuffling(self,button):
        if self.isShuffling:
            button.setText("Press to Shuffle")
            self.isShuffling = 0
        elif not self.isShuffling:
            button.setText("Shuffling Enabled")
            self.isShuffling = 1

    def changePlayPause(self, button):
        if self.isPlaying:
            button.setText("Pause")
            self.isPlaying = 0
        elif not self.isPlaying:
            button.setText("Play")
            self.isPlaying = 1

    def changeLooping(self, button):
        if self.isLooping:
            button.setText("Press to Loop")
            self.isLooping = 0
        elif not self.isLooping:
            button.setText("Looping Enabled")
            self.isLooping = 1