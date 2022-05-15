from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# With help from https://python.hotexamples.com/site/file?hash=0xf9d80bcc2b9c96f5da4ecc3b22454aeb65ead4fffc1a51baa98d97238571a926&fullName=pysimiam--master/pysimiam-coursera-week4/gui/pyqtgraph/MatplotlibWidget.py&project=altexdim/pysimiam-original-fork
class MatplotWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.fig = Figure()
        self.canvas = FigureCanvasQTAgg(self.fig)
        self.canvas.setParent(self)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        self.setLayout(self.vbox)

    def getFigure(self):
        return self.fig

    def draw(self):
        self.canvas.draw()
