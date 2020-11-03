import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication, QPushButton, QFileDialog, QAction)

from PyQt5.QtGui import QIcon

class UI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        chooseb = QPushButton("выбрать csv")
        runb = QPushButton("добавить надпись")

        chooseb.addAction(QAction(QIcon('open.png'), 'Open', self))
        chooseb.setStatusTip('Выбрать csv файл со списком скриншотов')
        chooseb.clicked.connect(self.showDialog)

        runb.addAction(QAction(QIcon('run.png'), 'Run', self))
        runb.setStatusTip('Запустить программу')
        runb.clicked.connect(self.runProgram)


        vbox = QVBoxLayout()
        vbox.addWidget(chooseb)
        vbox.addWidget(runb)


        self.setLayout(vbox)
        self.setGeometry(100, 100, 280, 180)
        self.setWindowTitle('Добавить надпись')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.fname = fname

    def runProgram(self):
        import writeOnImage
        writeOnImage.main(file=self.fname)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())