# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TwoNotes.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TwoNotes(object):
    def setupUi(self, TwoNotes):
        TwoNotes.setObjectName(_fromUtf8("TwoNotes"))
        TwoNotes.resize(361, 369)
        self.QuickNotes = QtGui.QWidget()
        self.QuickNotes.setObjectName(_fromUtf8("QuickNotes"))
        self.Note = QtGui.QPlainTextEdit(self.QuickNotes)
        self.Note.setGeometry(QtCore.QRect(10, 10, 331, 261))
        self.Note.setObjectName(_fromUtf8("Note"))
        self.Save = QtGui.QPushButton(self.QuickNotes)
        self.Save.setGeometry(QtCore.QRect(15, 290, 161, 28))
        self.Save.setObjectName(_fromUtf8("Save"))
        self.Clear = QtGui.QPushButton(self.QuickNotes)
        self.Clear.setGeometry(QtCore.QRect(180, 290, 161, 28))
        self.Clear.setObjectName(_fromUtf8("Clear"))
        TwoNotes.addTab(self.QuickNotes, _fromUtf8(""))
        self.Editor = QtGui.QWidget()
        self.Editor.setObjectName(_fromUtf8("Editor"))
        self.AllNotes = QtGui.QTableView(self.Editor)
        self.AllNotes.setGeometry(QtCore.QRect(10, 10, 331, 131))
        self.AllNotes.setObjectName(_fromUtf8("AllNotes"))
        self.SaveEdit = QtGui.QPushButton(self.Editor)
        self.SaveEdit.setGeometry(QtCore.QRect(10, 300, 331, 28))
        self.SaveEdit.setObjectName(_fromUtf8("SaveEdit"))
        self.EditNote = QtGui.QTextEdit(self.Editor)
        self.EditNote.setGeometry(QtCore.QRect(10, 164, 331, 111))
        self.EditNote.setObjectName(_fromUtf8("EditNote"))
        TwoNotes.addTab(self.Editor, _fromUtf8(""))
        self.Trash = QtGui.QWidget()
        self.Trash.setObjectName(_fromUtf8("Trash"))
        self.TrashNotes = QtGui.QTableView(self.Trash)
        self.TrashNotes.setGeometry(QtCore.QRect(10, 10, 331, 271))
        self.TrashNotes.setObjectName(_fromUtf8("TrashNotes"))
        self.Delete = QtGui.QPushButton(self.Trash)
        self.Delete.setGeometry(QtCore.QRect(180, 300, 161, 28))
        self.Delete.setObjectName(_fromUtf8("Delete"))
        self.Restore = QtGui.QPushButton(self.Trash)
        self.Restore.setGeometry(QtCore.QRect(10, 300, 161, 28))
        self.Restore.setObjectName(_fromUtf8("Restore"))
        TwoNotes.addTab(self.Trash, _fromUtf8(""))

        self.retranslateUi(TwoNotes)
        TwoNotes.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TwoNotes)

    def retranslateUi(self, TwoNotes):
        TwoNotes.setWindowTitle(_translate("TwoNotes", "TwoNotes", None))
        self.Save.setText(_translate("TwoNotes", "Save", None))
        self.Clear.setText(_translate("TwoNotes", "Clear", None))
        TwoNotes.setTabText(TwoNotes.indexOf(self.QuickNotes), _translate("TwoNotes", "Quick Notes", None))
        self.SaveEdit.setText(_translate("TwoNotes", "Save", None))
        TwoNotes.setTabText(TwoNotes.indexOf(self.Editor), _translate("TwoNotes", "Editor", None))
        self.Delete.setText(_translate("TwoNotes", "Delete", None))
        self.Restore.setText(_translate("TwoNotes", "Restore", None))
        TwoNotes.setTabText(TwoNotes.indexOf(self.Trash), _translate("TwoNotes", "Trash", None))

