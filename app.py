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

    sys.exit(app.exec())