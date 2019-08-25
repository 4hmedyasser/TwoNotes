import os
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMessageBox, QApplication, QListView, QPushButton, QGridLayout, QMainWindow, QWidget, QTabWidget, QTextBrowser, QTextEdit

home = os.path.expanduser("~")
path = home+'/.TwoNotes/Notes/'
trash = home+'/.TwoNotes/Trash/'


def create_note():
    if not NoteTitle.toPlainText() or NoteTitle.toPlainText() == 'Title':
        msg = QMessageBox()
        msg.setText('Please add a title for your note.')
        msg.exec()
    elif not Note2B.toPlainText():
        msg = QMessageBox()
        msg.setText('Please add text to your note.')
        msg.exec()
    else:
        title = NoteTitle.toPlainText()
        note = Note2B.toPlainText()
        save_this = os.path.join(path, title)
        save = open(save_this, "w")
        save.write(note)
        save.close()
        Note2B.clear()


def preview_notes():
    view_this = os.path.join(path, ".txt")
    view = open(view_this, "r")
    note = view.read()
    view.close()
    print(note)
    print("\n")


def edit_notes():
    choice = input("1-Add to The Note/n/n2-Re-Write The Note\n\n>")
    title = input("Enter Note's Title\n\n>")
    if choice == "1":
        note = input("Re-Enter Note\n\n>")
        append_this = os.path.join(path, title+".txt")
        append = open(append_this, "a")
        append.write("\n"+note+"\n")
        append.close()
        print("Note Edited successfully!\n")
    elif choice == "2":
        note = input("Re-Enter Note\n\n>")
        rewrite_this = os.path.join(path, title+".txt")
        rewrite = open(rewrite_this, "w")
        rewrite.write(title+"\n")
        rewrite.write("\n"+note+"\n")
        rewrite.close()
        print("Note Edited successfully!\n")


def delete_notes():
    title = input("Enter Note's Title\n\n>")
    delete_this = os.path.join(path, title + ".txt")
    os.remove(delete_this)
    print("Note Removed successfully!\n")


def purge_notes():
    print('F')


app = QApplication([])
window = QMainWindow()

window.setWindowTitle('TwoNotes')


Notes = QWidget()
Notes.setObjectName("Notes")

NotesLayout = QGridLayout(Notes)
NoteTitle = QTextEdit()
NoteTitle.setText('Title')
NoteTitle.setMaximumHeight(25)
NotesLayout.addWidget(NoteTitle)
Note2B = QTextEdit()
NotesLayout.addWidget(Note2B)
CreateButton = QPushButton('Save')
CreateButton.clicked.connect(lambda: on_click(0))
NotesLayout.addWidget(CreateButton)
ClearButton = QPushButton('Clear')
ClearButton.clicked.connect(lambda: on_click(1))
NotesLayout.addWidget(ClearButton)


List = QWidget()
List.setObjectName("List")

ListLayout = QGridLayout(List)
NotesListTable = QListView()
NotesListTable.setEditTriggers(QListView.NoEditTriggers)
ListLayout.addWidget(NotesListTable)
NotePreview = QTextBrowser()
ListLayout.addWidget(NotePreview)
EditButton = QPushButton('Edit')
EditButton.clicked.connect(lambda: on_click(2))
ListLayout.addWidget(EditButton)
DeleteButton = QPushButton('Move to Trash')
DeleteButton.clicked.connect(lambda: on_click(3))
ListLayout.addWidget(DeleteButton)


Editor = QWidget()
Editor.setObjectName("Editor")

EditorLayout = QGridLayout(Editor)
NotesEditorTable = QListView()
NotesEditorTable.setEditTriggers(QListView.NoEditTriggers)
EditorLayout.addWidget(NotesEditorTable)
EditNoteTitle = QTextEdit()
EditNoteTitle.setText('Title')
EditNoteTitle.setMaximumHeight(25)
EditorLayout.addWidget(EditNoteTitle)
NoteEditor = QTextEdit()
EditorLayout.addWidget(NoteEditor)
SaveButton = QPushButton('Save')
SaveButton.clicked.connect(lambda: on_click(4))
EditorLayout.addWidget(SaveButton)
UndoButton = QPushButton('Undo')
UndoButton.clicked.connect(lambda: on_click(5))
EditorLayout.addWidget(UndoButton)

Trash = QWidget()
Trash.setObjectName("Trash")

TrashLayout = QGridLayout(Trash)
NotesTrashTable = QListView()
NotesTrashTable.setEditTriggers(QListView.NoEditTriggers)
TrashLayout.addWidget(NotesTrashTable)
TrashNotePreview = QTextBrowser()
TrashLayout.addWidget(TrashNotePreview)
RestoreButton = QPushButton('Restore')
RestoreButton.clicked.connect(lambda: on_click(6))
TrashLayout.addWidget(RestoreButton)
PurgeButton = QPushButton('Delete')
PurgeButton.clicked.connect(lambda: on_click(7))
TrashLayout.addWidget(PurgeButton)


def on_click(index):
    if index == 0:
        create_note()
    elif index == 1:
        NoteTitle.setText(None)
        Note2B.setText(None)
    elif index == 2:
        tabs.setCurrentIndex(2)
    elif index == 3:
        # os.rename( str(path) + 'NewFile', str(trash) + 'NewFile')
        on_change(1)
        print('F')
    elif index == 4:
        print('F')
    elif index == 5:
        print('F')
    elif index == 6:
        print('F')
    elif index == 7:
        print('F')


def on_change(index):
    if index == 1:
        entries = os.listdir(path)
        model = QtGui.QStandardItemModel()
        NotesListTable.setModel(model)
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    elif index == 2:
        entries = os.listdir(path)
        model = QtGui.QStandardItemModel()
        NotesEditorTable.setModel(model)
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    elif index == 3:
        entries = os.listdir(path)
        model = QtGui.QStandardItemModel()
        NotesTrashTable.setModel(model)
        for i in entries:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)


tabs = QTabWidget()
tabs.currentChanged.connect(lambda: on_change(tabs.currentIndex()))
tabs.addTab(Notes, 'Notes')
tabs.addTab(List, 'List')
tabs.addTab(Editor, 'Editor')
tabs.addTab(Trash, 'Trash')
window.setCentralWidget(tabs)
window.setMinimumSize(480, 640)
window.show()
sys.exit(app.exec_())
