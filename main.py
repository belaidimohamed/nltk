from PyQt5.QtWidgets import *
from PyQt5.QtGui  import  QIcon , QFont 
import sys
import sentiment as s 

class one(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('finder')
        self.setWindowIcon(QIcon('detective1.png'))# put here window icon (full path)
        self.setGeometry(350,100,500,240)
        self.initwindow()
        self.show()
    def initwindow(self):
        self.vbox=QVBoxLayout()
        self.hbox=QHBoxLayout()
        self.hbox_2=QHBoxLayout()
        self.vbox.setContentsMargins(30,30,30,10)

        #---------------------------------
        label=QLabel('Enter a phrase to analyse : ')
        label.setFont(QFont('bold',11))

        self.line=QLineEdit()
  

        self.hbox.addWidget(self.line)
        self.hbox.setContentsMargins(10,0,30,30)

        button=QPushButton('Analyse')
        button.setStyleSheet('background-color:green;max-width:140px;height:25px;text-align:center;margin-left:150px;margin-bottom:10px')
        button.clicked.connect(self.b1)
        
        self.label2=QLabel('')
        self.label2.setStyleSheet('color: green')
        self.label2.setFont(QFont('ink free',12))

        self.label3=QLabel('')
        self.label3.setStyleSheet('color: green')
        self.label3.setFont(QFont('ink free',12))

        self.vbox.addWidget(label)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(button)
        self.vbox.addWidget(self.label2)
        self.vbox.addWidget(self.label3)

        self.setLayout(self.vbox)

    def b1(self):
        ch = s.sentiment(self.line.text())
        if(ch[0]=="neg"):
          self.label2.setText("Type of text: "+"negtive")
          self.label3.setText('Level of confidance: '+str(ch[1]*100) + "%")
          self.label3.setStyleSheet('color: red')
          self.label2.setStyleSheet('color: red')
        else :
          self.label2.setText("Type of text: "+"positive")
          self.label3.setText('Level of confidance: '+str(ch[1]*100) + "%")
          self.label3.setStyleSheet('color: green')
          self.label2.setStyleSheet('color: green')

app = QApplication(sys.argv)

win=one()
sys.exit(app.exec_())
