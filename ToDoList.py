# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Mark Brugger,11.13.22,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strTask = "" # Capture the name of the user's added task
strPriority = "" # Capture the priority of the user's added task
strRemoval = "" # Capture the task that the user wants to remove


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    dicRow = {}
    objFile = open("TodoList.txt", "r")
    for row in objFile:
        strData = row.split(",")
        dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
        lstTable.append(dicRow)
    objFile.close()

except:
    print("\nFile not found. One will be created when you save")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task Name, Priority of Task")
        print("=" * 27)
        for row in lstTable:
            print(row["Task"], row["Priority"], sep = ", ")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter the name of the task: ")
        strPriority = input("Enter the priority level of the task, (Low/Medium/High): ")
        lstTable.append({"Task": strTask, "Priority": strPriority})
        print("\nYour task has been recorded.")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemoval = input("Enter the name of the Task to Remove: ")
        for row in lstTable:
            if row["Task"].lower() == strRemoval.lower():
                lstTable.remove(row)
                print("\nYour task has been removed")
            else:
                print("\nTask was not found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("TodoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"] + "\n") )
        objFile.close()
        print("\nYour tasks have been saved to a file.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Now exiting the program...")
        break  # and Exit the program