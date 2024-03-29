import os
import methods
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import getpass
from os import listdir, makedirs, replace
from os.path import isfile, join
import gzip
import glob as gb
import shutil


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #title
        self.setWindowTitle("Select mode")
        self.setFixedSize(250,80)
        self.setLayout(qtw.QVBoxLayout())

        

        my_combo = qtw.QComboBox(self)
        my_combo.addItem("Default minecraft",0)
        my_combo.addItem("Lunar Client",1)
        my_combo.addItem("Badlion Client",2)
        self.layout().addWidget(my_combo)
        

        my_button = qtw.QPushButton("Confirm",
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():

            if(my_combo.currentText() == "Default minecraft" ):
                mcdir = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/logs/"

            if(my_combo.currentText() == "Lunar Client"):
                mcdir = "C:/Users/" + getpass.getuser() + "/.lunarclient/offline/1.8/logs/"
            
            if(my_combo.currentText() == "Badlion Client"):
                mcdir = "C:/Users/" + getpass.getuser() + "/AppData/Roaming/.minecraft/logs/blclient/chat/"

            
            latest = open(mcdir + "latest.log")

            logsRawLoc = gb.glob(mcdir + '*.gz')
            logs = []
            for item in logsRawLoc:
                item.replace("\\", "/")
                logs.append(item)


            class MainGui(qtw.QWidget):
                
                def __init__(self):
                    super().__init__()
                    layout = qtw.QGridLayout()
                    self.setLayout(layout)
                    self.setFixedSize(500,500)

                    self.list = qtw.QListWidget()
                    def open(self):
                        print(":C")
                    if(logs):
                        self.list.addItems(logs)
                        self.list.doubleClicked.connect(self.open)
                        self.layout().addWidget(self.list)

                    else:
                        self.list.addItem("There are no logs to parse")
                        self.layout().addWidget(self.list)


                def open(self):
                    print(self.list.currentItem().text())
                    os.startfile(f'{self.list.currentItem().text()}')

                    


            self.w = MainGui()
            self.w.show()
            self.close()

        self.show()

app = qtw.QApplication([])
app.setStyle('Fusion')
mw = MainWindow()

app.exec_()

