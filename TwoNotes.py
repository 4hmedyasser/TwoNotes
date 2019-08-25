import os
import sys

from PyQt5.QtWidgets import QMessageBox, QApplication, QListView, QGridLayout, QMainWindow, QWidget, QTabWidget, QPushButton, QTextBrowser, QTextEdit, QPlainTextEdit


path = "./Notes/"
trash = "./.Trash/"


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
        save_this = os.path.join(path, title+".txt")
        save = open(save_this, "w")
        save.write(note)
        save.close()
        Note2B.clear()


def list_notes():
    on_change(2)


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
Note2B = QPlainTextEdit()
NotesLayout.addWidget(Note2B)
CreateButton = QPushButton('Save')
NotesLayout.addWidget(CreateButton)
ClearButton = QPushButton('Clear')
NotesLayout.addWidget(ClearButton)


List = QWidget()
List.setObjectName("List")

ListLayout = QGridLayout(List)
NotesListTable = QListView()
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
NotesEditorTable = QListView()
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
NotesTrashTable = QListView()
TrashLayout.addWidget(NotesTrashTable)
TrashNotePreview = QTextBrowser()
TrashLayout.addWidget(TrashNotePreview)
RestoreButton = QPushButton('Restore')
TrashLayout.addWidget(RestoreButton)
PurgeButton = QPushButton('Delete')
TrashLayout.addWidget(PurgeButton)


def on_change(index):
    if index == 1:
        print('F')
    elif index == 2:
        print('F')
    elif index == 3:
        print('F')


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
