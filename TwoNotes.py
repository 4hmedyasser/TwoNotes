import os
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QLabel, QPushButton, QTextBrowser, QTextEdit, QPlainTextEdit

path = "./Notes/"
trash = "./.Trash/"

app = QApplication([])
window = QMainWindow()
tabs = QTabWidget()

window.setWindowTitle('TwoNotes')

Notes = QWidget()
Notes.setObjectName("Notes")

List = QWidget()
List.setObjectName("List")

Editor = QWidget()
Editor.setObjectName("Editor")

Trash = QWidget()
Trash.setObjectName("Trash")


tabs.addTab(Notes,'Notes')
tabs.addTab(List,'List')
tabs.addTab(Editor,'Editor')
tabs.addTab(Trash,'Trash')
window.setCentralWidget(tabs)
window.setMinimumSize(480,640)
window.show()
app.exec_()


def takeNote():
    title = input("Enter Note's Title\n\n>")
    note = input("Enter Note\n\n>")
    now = datetime.now()
    save_this=os.path.join(path,title+".txt")
    save = open(save_this, "w")
    save.write(title+"\n")
    save.write('%02d:%02d:%02d %02d/%02d/%04d' % (now.hour, now.minute, now.second, now.month, now.day, now.year))
    save.write("\n"+note)
    save.close()
    print("Note Saved successfully!\n")

def listNotes():
    print(os.listdir(path))
    print("\n")

def viewNote():
    title = input("Enter Note's Title\n\n>")
    view_this=os.path.join(path,title+".txt")
    view = open(view_this, "r")
    note = view.read()
    view.close()
    print(note)
    print("\n")

def editNote():
    choice = input("1-Add to The Note/n/n2-Re-Write The Note\n\n>")
    title = input("Enter Note's Title\n\n>")
    if choice == "1" :
        note = input("Re-Enter Note\n\n>")
        now = datetime.now()
        append_this=os.path.join(path,title+".txt")
        append = open(append_this, "a")
        append.write("Modification @ ")
        append.write('%02d:%02d:%02d %02d/%02d/%04d' % (now.hour, now.minute, now.second, now.month, now.day, now.year))
        append.write("\n"+note+"\n")
        append.close()
        print("Note Edited successfully!\n")
    elif choice == "2" :
        note = input("Re-Enter Note\n\n>")
        now = datetime.now()
        rewrite_this=os.path.join(path,title+".txt")
        rewrite = open(rewrite_this, "w")
        rewrite.write(title+"\n")
        rewrite.write('%02d:%02d:%02d %02d/%02d/%04d' % (now.hour, now.minute, now.second, now.month, now.day, now.year))
        rewrite.write("\n"+note+"\n")
        rewrite.close()
        print("Note Edited successfully!\n")

def removeNote():
    title=input("Enter Note's Title\n\n>")
    delete_this=os.path.join(path,title+".txt")
    os.remove(delete_this)
    print("Note Removed successfully!\n")