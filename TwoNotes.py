import os
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QGridLayout, QPushButton, QListView, QTextBrowser, QTextEdit, QMessageBox

home = os.path.expanduser("~")
path = home+'/.TwoNotes/Notes/'
trash = home+'/.TwoNotes/Trash/'


def create_notes():
    if not NoteTitle.toPlainText():
        msg = QMessageBox()
        msg.setText('Please add a title for your note.')
        msg.setInformativeText('Note must have a title.')
        msg.exec()
    elif not Note2B.toPlainText():
        msg = QMessageBox()
        msg.setText('Please add text to your note.')
        msg.setInformativeText('Note can not be empty')
        msg.exec()
    else:
        title = NoteTitle.toPlainText()
        note = Note2B.toPlainText()
        save_this = os.path.join(path, title)
        save = open(save_this, "w")
        save.write(note)
        save.close()
        Note2B.clear()


def edit_notes(note_title, entry):
    if EditNoteTitle.toPlainText() == note_title and NoteEditor.toPlainText() == entry:
        msg = QMessageBox()
        msg.setText('No changes were done.')
        msg.setInformativeText('Change note text in order to edit it.')
        msg.exec()
    elif EditNoteTitle.toPlainText() == note_title and NoteEditor.toPlainText() != entry:
        title = EditNoteTitle.toPlainText()
        note = NoteEditor.toPlainText()
        save_this = os.path.join(path, title)
        save = open(save_this, "w")
        save.write(note)
        save.close()
        EditNoteTitle.clear()
        NoteEditor.clear()
    else:
        os.remove(os.path.join(path, note_title))
        title = EditNoteTitle.toPlainText()
        note = NoteEditor.toPlainText()
        save_this = os.path.join(path, title)
        save = open(save_this, "w")
        save.write(note)
        save.close()
        EditNoteTitle.clear()
        NoteEditor.clear()
    on_change(2)


def trash_notes():
    note_title = str(NotesListTable.currentIndex().data())
    if not note_title == 'None':
        os.rename(os.path.join(path, note_title), os.path.join(trash, note_title))
        NotePreview.setText(None)
        on_change(3)


def restore_notes():
    note_title = str(NotesTrashTable.currentIndex().data())
    if not note_title == 'None':
        os.rename(os.path.join(trash, note_title), os.path.join(path, note_title))
        TrashNotePreview.setText(None)
        on_change(3)


def purge_notes():
    note_title = str(NotesTrashTable.currentIndex().data())
    if not note_title == 'None':
        msg = QMessageBox()
        msg.setText('Are you sure you want to permanently delete this note?')
        msg.setInformativeText('The deleted note won\'t be able to be restored.')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msg.exec()
        if ret == QMessageBox.Yes:
            os.remove(os.path.join(trash, note_title))
            TrashNotePreview.setText(None)
            on_change(3)


app = QApplication([])
window = QMainWindow()
model = QtGui.QStandardItemModel()

window.setWindowTitle('TwoNotes')


Notes = QWidget()
Notes.setObjectName("Notes")

NotesLayout = QGridLayout(Notes)
NoteTitle = QTextEdit()
NoteTitle.setText('Note Title')
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
NotesListTable.setModel(model)
NotesListTable.clicked.connect(lambda: on_select(1))
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
NotesEditorTable.setModel(model)
NotesEditorTable.clicked.connect(lambda: on_select(2))
EditorLayout.addWidget(NotesEditorTable)
EditNoteTitle = QTextEdit()
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
NotesTrashTable.setModel(model)
NotesTrashTable.clicked.connect(lambda: on_select(3))
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
    clicked = False
    if index == 0:  # create
        create_notes()
    elif index == 1:  # clear
        NoteTitle.setText(None)
        Note2B.setText(None)
    elif index == 2:  # edit
        tabs.setCurrentIndex(2)
    elif index == 3:  # trash
        trash_notes()
        on_change(1)
    elif index == 4:  # save
        clicked = True
        note_title = str(NotesEditorTable.currentIndex().data())
        reader = open(os.path.join(path, note_title), 'r')
        entry = reader.read()
        reader.close()
        edit_notes(note_title, entry)
    elif index == 5:  # undo
        if not clicked:
            note_title = str(NotesEditorTable.currentIndex().data())
            reader = open(os.path.join(path, note_title), 'r')
            entry = reader.read()
            reader.close()
        EditNoteTitle.setText(note_title)
        NoteEditor.setText(entry)
    elif index == 6:  # restore
        restore_notes()
        on_change(3)
    elif index == 7:  # purge
        purge_notes()
        on_change(3)


def on_select(tab_index):
    if tab_index == 1:
        note_title = str(NotesListTable.currentIndex().data())
        reader = open(os.path.join(path, note_title), 'r')
        entry = reader.read()
        reader.close()
        NotePreview.setText(entry)
    elif tab_index == 2:
        note_title = str(NotesEditorTable.currentIndex().data())
        reader = open(os.path.join(path, note_title), 'r')
        entry = reader.read()
        reader.close()
        EditNoteTitle.setText(note_title)
        NoteEditor.setText(entry)
    elif tab_index == 3:
        note_title = str(NotesTrashTable.currentIndex().data())
        reader = open(os.path.join(trash, note_title), 'r')
        entry = reader.read()
        reader.close()
        TrashNotePreview.setText(entry)


def on_change(index):
    if index == 1:
        items = os.listdir(path)
        model.clear()
        for i in items:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    elif index == 2:
        items = os.listdir(path)
        model.clear()
        for i in items:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    elif index == 3:
        items = os.listdir(trash)
        model.clear()
        for i in items:
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
