from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QDial, QLabel, QCheckBox

class VolumeWidget(QWidget):
    def __init__(self):
        # Generate Widget
        super().__init__()
        #Create dial for volume control
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100) 
        self.dial.setValue(40) #starting volume level
        self.dial.setNotchesVisible(True)

        #Create Mute Checkbox
        self.mute = QCheckBox("Mute")
        self.mute.setChecked(False) #Automatically False
        self.mute.stateChanged.connect(lambda:self.mute_state()) #check for Mute Changes

        #Add Volume Label
        self.label = QLabel(self)
        self.label.setText(str(self.dial.value()) + "            ")
        
        # Generate Layout for the volume Knob
        self.hbox = QHBoxLayout() 
        self.hbox.addStretch(1) # right aligns the widget
        self.hbox.addWidget(self.dial)

        # Generate Layout for the volume label
        self.hbox2 = QHBoxLayout()
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.label)

        # Generate Layout for the mute checkbox 
        self.hbox3 = QHBoxLayout()
        self.hbox3.addStretch(1)
        self.hbox3.addWidget(self.mute)

        # Add both horizontal layouts to a vertical layout so that volume knob is above label, and mute is below label
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        # self.vbox.addStretch(1) #this would bottom align the widget

        #Set final layout
        self.setLayout(self.vbox) 

    #changes volume dial label on dial change, and returns current volume 
    def get_volume_level(self):
        value = self.dial.value()
        # setting text to the label
        self.label.setText(str(value) + "            ")
        return int(value)
    
    #mute state, changes volume dial to 0 if mute is checked or 10 when mute is unchecked
    def mute_state(self):
        if self.mute.isChecked():
            self.dial.setValue(0)
        else:
            self.dial.setValue(10)



