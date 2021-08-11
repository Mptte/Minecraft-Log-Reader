import os
import methods
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import getpass
import glob



class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #title
        self.setWindowTitle("Chat History")
        self.setFixedSize(250,100)
        self.setLayout(qtw.QVBoxLayout())
        

        my_combo = qtw.QComboBox(self)
        my_combo.addItem("Default minecraft",0)
        my_combo.addItem("Lunar Client",1)
        my_combo.addItem("Badlion Client",2)
        my_combo.addItem("Custom directory",3)
        self.layout().addWidget(my_combo)
        

        my_button = qtw.QPushButton("Confirm",
        clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
          
            
            if(my_combo.currentText() == "Default minecraft" ):
                mcdir = "C:\\Users\\" + getpass.getuser() + "\\AppData\\Roaming\\minecraft\\"

            if(my_combo.currentText() == "Lunar Client"):
                mcdir = "C:\\Users\\" + getpass.getuser() + "\\.lunarclient\\offline\\1.8\\logs\\"
            
            if(my_combo.currentText() == "Badlion Client"):
                mcdir = "C:\\Users\\" + getpass.getuser() + "\AppData\\Roaming\\.minecraft\\logs\\blclient\\chat"

            if(my_combo.currentText() == "Custom directory"):
                entry = qtw.QLineEdit()
                entry.setObjectName("minecraft_directory")
                self.layout().addWidget(entry)

                

            
        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

def logger():
    logfile = open(os.getenv("APPDATA") + "\\.minecraft\\logs\\latest.log", "r")
    loglines = methods.follow(logfile)
    for line in loglines:
        if "[Render thread/INFO]: [CHAT]" or "[Client thread/INFO]: [CHAT]"  in line:
            print(line)
        else:
            chatLines = None


