from functools import partial
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

from MainWindow import MainWindow

# This function may be what can be used to help a Playlist get the tracks
def foo(window : MainWindow):
    print(window.mediaWidget.songPlaying.text())

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # The commands below, but above sys.exit are ALL required to setup a SystemTray 
    icon = QIcon("traypic.jpeg")
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    menu = QMenu()
    opt1 = QAction("Open Folder")
    #opt1.triggered.connect(partial(foo, window))
    menu.addAction(opt1) 
    tray.setContextMenu(menu) #Attaches menu to the system tray

    sys.exit(app.exec())



