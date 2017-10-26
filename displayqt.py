import sys
from PyQt5 import QtGui as qt

def window():
    app = qt.QApplication(sys.argv)
    w = qt.QWidget()
    b = qt.QLabel(w)
    b.setText('hello world')
    w.setGerometry(100,100,200,50)
    b.move(50,29)
    w.setWindowTitle("Jack Thomson is a punk")
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
