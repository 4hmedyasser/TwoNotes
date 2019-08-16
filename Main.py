import os
from datetime import datetime


path = "/home/user/openNotes/Notes/"


def takeNote():
    title = raw_input("Enter Note's Title\n\n>")
    note = raw_input("Enter Note\n\n>")
    now = datetime.now()
    save_this=os.path.join(path,title+".txt")
    save = open(save_this, "w")
    save.write(title+"\n")
    save.write('%02d:%02d:%02d %02d/%02d/%04d' % (now.hour, now.minute, now.second, now.month, now.day, now.year))
    save.write("\n"+note)
    save.close()
    print "Note Saved successfully!\n"

def listNotes():
    print os.listdir("/home/user/openNotes/Notes/")
    print("\n")

def viewNote():
    title = raw_input("Enter Note's Title\n\n>")
    view_this=os.path.join(path,title+".txt")
    view = open(view_this, "r")
    note = view.read()
    view.close()
    print note
    print "\n"

def editNote():
    choice = raw_input("1-Add to The Note/n/n2-Re-Write The Note\n\n>")
    title = raw_input("Enter Note's Title\n\n>")
    if choice == "1" :
        note = raw_input("Re-Enter Note\n\n>")
        now = datetime.now()
        append_this=os.path.join(path,title+".txt")
        append = open(append_this, "a")
        append.write("Modification @ ")
        append.write('%02d:%02d:%02d %02d/%02d/%04d' % (now.hour, now.minute, now.second, now.month, now.day, now.year))
        append.write("\n"+note+"\n")
        append.close()
        print "Note Edited successfully!\n"
    elif choice == "2" :
        note = raw_input("Re-Enter Note\n\n>")
        now = datetime.now()
        rewrite_this=os.path.join(path,title+".txt")
        rewrite = open(rewrite_this, "w")
        rewrite.write(title+"\n")
        rewrite.write('%02d:%02d:%02d %02d/%02d/%04d' % (now.hour, now.minute, now.second, now.month, now.day, now.year))
        rewrite.write("\n"+note+"\n")
        rewrite.close()
        print "Note Edited successfully!\n"

def removeNote():
    title=raw_input("Enter Note's Title\n\n>")
    delete_this=os.path.join(path,title+".txt")
    os.remove(delete_this)
    print "Note Removed successfully!\n"

print "Welcome to openNotes!\n\n"
choice = None

while choice != "EXIT":
    choice = raw_input("1-Take Note\n\n2-List Notes\n\n3-View Note\n\n4-Edit Note\n\n5-Remove Note\n\n\nTo End The Program Enter EXIT.\n\n>")
    if choice == "1" :
        takeNote()
    elif choice == "2" :
        listNotes()
    elif choice == "3" :
        viewNote()
    elif choice == "4" :
        editNote()
    elif choice == "5" :
        removeNote()
    elif choice == "EXIT":
        break
