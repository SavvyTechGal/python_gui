from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QDial

class VolumeWidget(QWidget):
    def __init__(self):
        # Generate Widget
        super().__init__()
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(40)
        # Generate Layout for Widget
        self.hbox = QHBoxLayout() 
        self.hbox.addStretch(1) # right aligns the widget
        self.hbox.addWidget(self.dial)
        # self.vbox = QVBoxLayout()
        # self.vbox.addStretch(-1)
        # self.vbox.addLayout(self.hbox)

        self.setLayout(self.hbox)


