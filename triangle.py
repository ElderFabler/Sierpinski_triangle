import random as rnd
import time
from PyQt5 import QtWidgets, QtCore, QtGui

class TriangleWin(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setFixedSize(512,512)

        self.win_in = QtWidgets.QLabel()
        self.setStyleSheet("QLabel {background: black}")
    
        self.pixmap = QtGui.QPixmap(self.win_in.size())
        self.P = 0

        vlay = QtWidgets.QVBoxLayout()
        vlay.addWidget(self.win_in)
        self.setLayout(vlay)

    def labelSize(self):
        return self.win_in.size()

    def firstDot(self,qp,poly):
        soize = self.labelSize()
        while True:
            self.P = QtCore.QPoint(rnd.randrange(soize.width()),rnd.randrange(soize.height()))
            if poly.containsPoint(self.P,QtCore.Qt.OddEvenFill):
                qp.drawPoint(self.P)
                return self.P
            else:
                pass

    def drawTriangle(self,qp):
        soize = self.labelSize()
        A = QtCore.QPoint(int(soize.width()/2),0)
        B = QtCore.QPoint(0,soize.height())
        C = QtCore.QPoint(soize.width(),soize.height())
        polygon = QtGui.QPolygon()
        polygon << A << B << C
        try:
            V = rnd.choice([A,B,C])
            self.P = QtCore.QPoint(int((V.x()+self.P.x())/2),int((V.y()+self.P.y())/2))
            qp.drawPoint(self.P)
        except:
            self.P = self.firstDot(qp,polygon)
        
    def paintEvent(self, event):
        qp = QtGui.QPainter(self.pixmap)
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtCore.Qt.red)
        qp.setPen(pen)
        self.drawTriangle(qp)
        qp.end()
        self.win_in.setPixmap(self.pixmap)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = TriangleWin()
    win.setWindowTitle("Serpinski triangle")
    
    win.show()
    sys.exit(app.exec_())