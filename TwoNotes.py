import os
import sys
from datetime import datetime

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QTableView, QGridLayout, QMainWindow, QWidget, QTabWidget, QPushButton, QTextBrowser, QTextEdit, QPlainTextEdit

path = "./Notes/"
trash = "./.Trash/"

def onChange():
    print('F\n')


app = QApplication([])
window = QMainWindow()
tabs = QTabWidget()
tabs.currentChanged.connect(onChange)

window.setWindowTitle('TwoNotes')

Notes = QWidget()
Notes.setObjectName("Notes")

NotesLayout = QGridLayout(Notes)
NoteTitle = QTextEdit()
NoteTitle.setText('Title')
NoteTitle.setMaximumHeight(25)
NotesLayout.addWidget(NoteTitle)
Note2B = QPlainTextEdit()
NotesLayout.addWidget(Note2B)
CreateButton = QPushButton('Save')
NotesLayout.addWidget(CreateButton)
ClearButton = QPushButton('Clear')
NotesLayout.addWidget(ClearButton)




List = QWidget()
List.setObjectName("List")

ListLayout = QGridLayout(List)
NotesListTable = QTableView()
ListLayout.addWidget(NotesListTable)
NotePreview = QTextBrowser()
ListLayout.addWidget(NotePreview)
EditButton = QPushButton('Edit')
ListLayout.addWidget(EditButton)
DeleteButton = QPushButton('Move to Trash')
ListLayout.addWidget(DeleteButton)


Editor = QWidget()
Editor.setObjectName("Editor")

EditorLayout = QGridLayout(Editor)
NotesEditorTable = QTableView()
EditorLayout.addWidget(NotesEditorTable)
NoteEditor = QPlainTextEdit()
EditorLayout.addWidget(NoteEditor)
SaveButton = QPushButton('Save')
EditorLayout.addWidget(SaveButton)
UndoButton = QPushButton('Undo')
EditorLayout.addWidget(UndoButton)

Trash = QWidget()
Trash.setObjectName("Trash")

TrashLayout = QGridLayout(Trash)
NotesTrashTable = QTableView()
TrashLayout.addWidget(NotesTrashTable)
TrashNotePreview = QTextBrowser()
TrashLayout.addWidget(TrashNotePreview)
RestoreButton = QPushButton('Restore')
TrashLayout.addWidget(RestoreButton)
PurgeButton = QPushButton('Delete')
TrashLayout.addWidget(PurgeButton)




tabs.addTab(Notes,'Notes')
tabs.addTab(List,'List')
tabs.addTab(Editor,'Editor')
tabs.addTab(Trash,'Trash')
window.setCentralWidget(tabs)
window.setMinimumSize(480,640)
window.show()
sys.exit(app.exec_())



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