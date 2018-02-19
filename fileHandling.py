import os
import datetime
class fileHandling():
        def newStickyNotes(self):
            current_time = str(datetime.datetime.now())
            current_time = current_time.replace(":", "-")
            current_time = current_time.replace(".","-")
            current_time = current_time.replace(" ","-")
            newStickyNote = str("Title:" + input("Please write sticky note title here:") + ", Content:" + input(
            "Please write sticky note content here:"))
            textFiles = open("Sticky Note " + current_time + ".txt", "w+")
            textFiles.write(newStickyNote)
            textFiles.close()

        def listStickyNotes(self):
            #for file in os.listdir("C:/Users/Adam.Grimes/PycharmProjects/MOJ_Project"):
            #    if file.endswith(".txt"):
            #        print(os.path.join("C:/Users/Adam.Grimes/PycharmProjects/MOJ_Project", file))
            for root, dirs, files in os.walk("C:/Users/Adam.Grimes/PycharmProjects/MOJ_Project"):
                for file in files:
                    if file.endswith(".txt") and "Sticky Note" in file:
                        #print(os.path.join(root, file))
                        print(os.path.join(file))

        def editStickyNotes(self):
            noteToBeEdited = input("What note would you like to edit?: ")
            noteEdit = "Title:" + input("Please write the new title of the note: ") + ", Content:" + input(
                "Please write the new sticky note content here:")
            editFiles = open(noteToBeEdited, "w+")
            editFiles.write(noteEdit)
            editFiles.close()

        def viewStickyNotes(self):
            note_to_be_viewed = input("What note would you like to view?: ")
            note = open(note_to_be_viewed, "r")
            contents = note.read()
            return contents

        def deleteStickyNotes(self):
                noteToBeDeleted = input("What note would you like to delete?: ")
                os.remove(noteToBeDeleted)

