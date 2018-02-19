# User Selects Menu Option
from fileHandling import fileHandling

class userInput():
    def userInputValueInput(self):
        userInputValue = input("Enter Command:")
        print(userInputValue)
        fileHandlingCommands = fileHandling()
        if userInputValue == "Exit" or userInputValue == "0" or userInputValue == "exit":
            return False

        elif userInputValue == "New" or userInputValue == "1" or userInputValue == "new":
            total_number_of_notes = 0
            createAnotherStickyNote = True
            while total_number_of_notes < 10 and createAnotherStickyNote == True:
                fileHandlingCommands.newStickyNotes()
                invalid_answer_to_yes_no_question = "true"
                while invalid_answer_to_yes_no_question == "true":
                    doesUserWantToCreateAnotherStickyNote = input(
                        "Would you like to create another sticky note? Y/N:")
                    if doesUserWantToCreateAnotherStickyNote == "N" or doesUserWantToCreateAnotherStickyNote == "n":
                        invalid_answer_to_yes_no_question = "false"
                        createAnotherStickyNote = "false"
                        print("\n")
                    elif doesUserWantToCreateAnotherStickyNote == "Y" or doesUserWantToCreateAnotherStickyNote == "y":
                        invalid_answer_to_yes_no_question = "false"
                        print("\n")
                    else:
                        print("Invalid answer, please try again:")
                        print("\n")
                total_number_of_notes += 1
                if total_number_of_notes == 9:
                    print("You can have a maximum of ten notes, please delete a note")
                    print("\n")
            return True

        elif userInputValue == "List" or userInputValue == "2" or userInputValue == "list":
            fileHandlingCommands.listStickyNotes()
            return True

        elif userInputValue == "Edit" or userInputValue == "3" or userInputValue == "edit":
            invalidNoteToBeEdited = True
            while invalidNoteToBeEdited == True:
                try:
                    fileHandlingCommands.editStickyNotes()
                    print("Note Edited Sucesfully")
                    invalidNoteToBeEdited = False
                except:
                    print("Note does not exist, please try again")
                    print("\n")
            return True

        elif userInputValue == "View" or userInputValue == "4" or userInputValue == "view":
            invalidNoteToBeViewed = True
            while invalidNoteToBeViewed == True:
                try:
                    viewStickyNote = fileHandlingCommands.viewStickyNotes()
                    print(viewStickyNote)
                    invalidNoteToBeViewed = False
                except:
                    print("Note does not exist, please try again")
                    print("\n")
            return True

        elif userInputValue == "Delete" or userInputValue == "5" or userInputValue == "delete":
            invalidNoteToBeDeleted = True
            while invalidNoteToBeDeleted == True:
                try:
                    fileHandlingCommands.deleteStickyNotes()
                    print("Note Deleted")
                    invalidNoteToBeDeleted = False
                except:
                    print("Note does not exist, please try again")
                    print("\n")
            return True

        else:
            print("Invalid Input, please try again")
            print("\n")
            return True

#Changes
# Change all cases using a function rather than put all permutations of capitals.
# Get rid of while loops- do not need functionality to create another one.
# methods- find out how to put arguements in.
# Renaming conventions
# Split functionality so methods do one thing- e.g new has extra datetime functionality
#