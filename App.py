# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:58:37 2018

@author: Moshiur
"""



from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from Db import Db


class ClickLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)



class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(600, 600)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)

        # database create

        self.db = Db()
        #db.create_table()


        self.noteFirstLookLayout()




    # Note App First Look Layout

    def on_buttonCreateNote_clicked(self):
        # self.noteEntryLayout()
        self.noteTitleLayout()

    def on_buttonShoweNote_clicked(self):
        self.noteListLayout()

    # Note Entry Layout

    def on_buttonBackNoteEntry_clicked(self):
        self.noteFirstLookLayout()

    # Note List Layout
    def on_buttonBackNoteList_clicked(self):
        self.noteFirstLookLayout()

    def on_buttonBackNote_clicked(self):
        self.noteListLayout()

    def on_button_Ok_TitleEntry_clicked(self):
        self.title = self.lineedit.text()
        self.noteEntryLayout()

    def return_pressed_lineedit(self):
        self.title = self.lineedit.text()
        print(self.title)
        self.noteEntryLayout()

    def on_buttonNoteEntry_clicked(self):
        self.text = self.plaintextedit.toPlainText()
        self.db.insert_data(self.title,self.text)
        self.noteFirstLookLayout()

    def on_label_1_clicked(self):
        self.title_list=self.db.read_from_db()


    # For All Layout

    def noteFirstLookLayout(self):
        layout = QVBoxLayout()

        buttonCreateNote = QPushButton("Create Note")
        buttonCreateNote.setFont(QFont('Arial', 15))
        buttonCreateNote.clicked.connect(self.on_buttonCreateNote_clicked)

        buttonShoweNote = QPushButton("Note List")
        buttonShoweNote.setFont(QFont('Arial', 15))
        buttonShoweNote.clicked.connect(self.on_buttonShoweNote_clicked)

        labelTextTitle = QLabel("NoteBook")
        labelTextTitle.setFont(QFont('Arial', 20))
        labelTextTitle.setAlignment(Qt.AlignHCenter)

        self.image = QLabel()
        self.image.setPixmap(QPixmap('111.jpg'))
        self.image.setAlignment(Qt.AlignHCenter)

        buttonExit=QPushButton("Exit")
        buttonExit.setFont(QFont('Arial', 15))
        buttonExit.clicked.connect(QCoreApplication.instance().quit)

        layout.addWidget(labelTextTitle)
        layout.addWidget(self.image)
        layout.addWidget(buttonCreateNote)
        layout.addWidget(buttonShoweNote)
        layout.addWidget(buttonExit)

        self.setLayout(layout)


    def noteTitleLayout(self):
        layout = QVBoxLayout()



        buttonBack = QPushButton("Back")
        buttonBack.setFont(QFont('Arial', 15))
        buttonBack.clicked.connect(self.on_buttonBackNoteEntry_clicked)

        labelTextTitle = QLabel("Enter Your Note Title Here : ")
        labelTextTitle.setFont(QFont('Arial', 18))
        #labelTextTitle.resize(100,200)
        labelTextTitle.setAlignment(Qt.AlignHCenter)

        self.lineedit = QLineEdit()
        self.lineedit.setFont(QFont('Arial', 15))
        self.lineedit.resize(300,500)
        self.lineedit.setPlaceholderText("Note Write Here")
        #self.lineedit.move(100, 100)
        self.lineedit.returnPressed.connect(self.return_pressed_lineedit)
        self.lineedit.setAlignment(Qt.AlignHCenter)

        button_ok = QPushButton("OK")
        button_ok.setFont(QFont('Arial', 15))
        button_ok.clicked.connect(self.on_button_Ok_TitleEntry_clicked)

        layout.setAlignment(Qt.AlignVCenter)




        layout.addWidget(labelTextTitle)
        layout.addWidget(self.lineedit)
        layout.addWidget(button_ok)
        layout.addWidget(buttonBack)

        self.setLayout(layout)

    def noteEntryLayout(self):
        layout = QVBoxLayout()

        buttonBack = QPushButton("Back")
        buttonBack.setFont(QFont('Arial', 15))
        buttonBack.clicked.connect(self.on_buttonBackNoteEntry_clicked)

        labelTextTitle = QLabel("Enter Your Note Here : ")
        labelTextTitle.setFont(QFont('Arial', 18))

        self.plaintextedit = QPlainTextEdit()
        self.plaintextedit.setFont(QFont('Arial', 15))
        # self.plaintextedit.insertPlainText("")
        self.plaintextedit.setPlaceholderText("Note Write Here")
        # textedit = QTextEdit()
        # textedit.setPlaceholderText("This is some placeholder text.")

        button_ok = QPushButton("OK")
        button_ok.setFont(QFont('Arial', 15))
        button_ok.clicked.connect(self.on_buttonNoteEntry_clicked)

        layout.addWidget(labelTextTitle)
        layout.addWidget(self.plaintextedit)
        layout.addWidget(button_ok)
        layout.addWidget(buttonBack)

        self.setLayout(layout)






    def createLabelList(self,layout):
        self.title_list=self.db.read_from_db()
        #label=[]
        length=len(self.title_list)
        for t in range(length):
            print(self.title_list[length-t-1])
            #tex= repr(self.title_list[t][1])
            label = ClickLabel(self.title_list[length-t-1][1])
            label.setWordWrap(True)
            label.setFont(QFont('Arial', 16))
            label.setStyleSheet("ClickLabel { background-color : white; color : black;border-style: outset;border-width: 10px;border-color: black; }")
            label.setAlignment(Qt.AlignHCenter)
            #label.setAlignment(Qt.AlignVCenter)
            layout.addWidget(label)
            label.clicked.connect(lambda: self.commander(self.title_list[length-t-1][2]))

    def commander(self,id):
        #print(">>>>",self.sender().text())
        ttl=self.sender().text()
        note="Nothing"
        for t in range(len(self.title_list)):
            if self.title_list[t][1]==ttl:
                note=self.title_list[t][2]


        #print("ID : ",note)

        layout=QVBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)

        labelTitle=QLabel(ttl)
        labelTitle.setWordWrap(True)
        labelTitle.setFont(QFont('Arial', 19))

        label=QLabel(note)
        label.setFont(QFont('Arial', 14))
        label.setWordWrap(True)

        buttonBack = QPushButton("Back")
        buttonBack.setFont(QFont('Arial', 15))
        buttonBack.clicked.connect(self.on_buttonBackNote_clicked)

        layout.addWidget(labelTitle)
        layout.addWidget(label)
        layout.addWidget(buttonBack)
        self.setLayout(layout)






    def noteListLayout(self):

        layout = QVBoxLayout()

        #layout.addStretch()

        buttonBack = QPushButton("Back")
        buttonBack.setFont(QFont('Arial', 15))
        buttonBack.clicked.connect(self.on_buttonBackNoteList_clicked)



        labelTextTitle = QLabel("List Of All Note : ")
        labelTextTitle.setFont(QFont('Arial', 18))
        labelTextTitle.setAlignment(Qt.AlignHCenter)


        layout.addWidget(labelTextTitle)

        self.createLabelList(layout)
        layout.addWidget(buttonBack)

        self.setLayout(layout)



    # For Set Layout
    def setLayout(self, layout):
        self.clearLayout()
        QWidget.setLayout(self, layout)

    def clearLayout(self):
        if self.layout() is not None:
            old_layout = self.layout()
            for i in reversed(range(old_layout.count())):
                old_layout.itemAt(i).widget().setParent(None)
            import sip
            sip.delete(old_layout)


app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())
