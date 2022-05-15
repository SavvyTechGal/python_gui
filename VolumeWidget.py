from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QDial, QLabel

class VolumeWidget(QWidget):
    def __init__(self):
        # Generate Widget
        super().__init__()
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100) 
        self.dial.setValue(40) #starting volume level
        self.dial.setNotchesVisible(True)
        #Add Volume Label
        self.label = QLabel(self)
        self.label.setText(str(self.dial.value()) + "            ")

        # #Change Volume Label as Dial is turned
        # self.dial.valueChanged.connect(self.get_volume_level)
        

        # Generate Layout for the volume Knob
        self.hbox = QHBoxLayout() 
        self.hbox.addStretch(1) # right aligns the widget
        self.hbox.addWidget(self.dial)

        # Generate Layout for the volume label
        self.hbox2 = QHBoxLayout()
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.label)

        # Add both horizontal layouts to a vertical layout so that volume knob is above label
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.hbox2)
        # self.vbox.addStretch(1) #this would bottom align the widget

        #Set final layout
        self.setLayout(self.vbox) 

    def get_volume_level(self):
        value = self.dial.value()
        # setting text to the label
        self.label.setText(str(value) + "            ")
        return int(value)



