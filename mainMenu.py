#from menuOptions import menuOptions
from userInput import userInput

def main():
    #Print the Menu Options
    print_screen = True
    while print_screen == True:
        #menuChoice = menuOptions()
        #menuChoices = menuChoice.Menu()
        print("0. Exit" + "\n" + "1. New" + "\n" + "2. List" + "\n" + "3. Edit" + "\n" + "4. View" + "\n" + "5. Delete")

    #Retreieve User Input and Direct them to the correct file handling logic
        userChoice = userInput()
        print_screen = userChoice.userInputValueInput()



if __name__ == "__main__":
    main()