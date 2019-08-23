import os
import sys
from datetime import datetime

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QTableView, QGridLayout, QMainWindow, QWidget, QTabWidget, QLabel, QPushButton, QTextBrowser, QTextEdit, QPlainTextEdit

path = "./Notes/"
trash = "./.Trash/"

class TwoNotes(QtGui, QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.resize(400, 500)
        self.setWindowTitle('TwoNotes')
        self.tabs = QTabWidget()
        self.centralWidget = self.tabs
        self.tabs.currentChanged.connect(self.onChange)

        self.Notes = QWidget()
        self.Notes.setObjectName("Notes")

        self.NotesLayout = QGridLayout(self.Notes)
        self.NoteTitle = QTextEdit()
        self.NoteTitle.setText('Title')
        self.NoteTitle.setMaximumHeight(25)
        self.NotesLayout.addWidget(self.NoteTitle)
        self.Note2B = QPlainTextEdit()
        self.NotesLayout.addWidget(self.Note2B)
        self.CreateButton = QPushButton('Save')
        self.NotesLayout.addWidget(self.CreateButton)
        self.ClearButton = QPushButton('Clear')
        self.NotesLayout.addWidget(self.ClearButton)

        self.List = QWidget()
        self.List.setObjectName("List")

        self.ListLayout = QGridLayout(self.List)

        self.NotesListTable = QTableView()
        self.ListLayout.addWidget(self.NotesListTable)

        self.NotePreview = QTextBrowser()
        self.ListLayout.addWidget(self.NotePreview)

        self.EditButton = QPushButton('Edit')
        self.ListLayout.addWidget(self.EditButton)

        self.DeleteButton = QPushButton('Move to Trash')
        self.ListLayout.addWidget(self.DeleteButton)



        self.Editor = QWidget()
        self.Editor.setObjectName("Editor")

        self.EditorLayout = QGridLayout(self.Editor)

        self.NotesEditorTable = QTableView()
        self.EditorLayout.addWidget(self.NotesEditorTable)

        self.NoteEditor = QPlainTextEdit()
        self.EditorLayout.addWidget(self.NoteEditor)

        self.SaveButton = QPushButton('Save')
        self.EditorLayout.addWidget(self.SaveButton)

        self.UndoButton = QPushButton('Undo')
        self.EditorLayout.addWidget(self.UndoButton)



        self.Trash = QWidget()
        self.Trash.setObjectName("Trash")

        self.TrashLayout = QGridLayout(self.Trash)

        self.NotesTrashTable = QTableView()
        self.TrashLayout.addWidget(self.NotesTrashTable)

        self.TrashNotePreview = QTextBrowser()
        self.TrashLayout.addWidget(self.TrashNotePreview)

        self.RestoreButton = QPushButton('Restore')
        self.TrashLayout.addWidget(self.RestoreButton)

        self.PurgeButton = QPushButton('Delete')
        self.TrashLayout.addWidget(self.PurgeButton)

        self.tabs.addTab(self.Notes,'Notes')
        self.tabs.addTab(self.List,'List')
        self.tabs.addTab(self.Editor,'Editor')
        self.tabs.addTab(self.Trash,'Trash')

    def onChange(self, i):  # changed!
        QtGui.QMessageBox.information(self,
              "Tab Index Changed!",
              "Current Tab Index: %d" % i)  # changed!

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = TwoNotes
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