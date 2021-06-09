# ------------------------------------------------------------------------ #
# Title: Main.py
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# GShay,6.6.2021,Updated for Assignment09
# GShay,6.6.2021,Added menu choices
# GShay,6.8.2021,updated comments
# ------------------------------------------------------------------------ #
# TODO: Import Modules
import DataClasses

if __name__ == "__main__":
    import ProcessingClasses as P   # processing classes
    from IOClasses import EmployeeIO as Eio  # EmployeeIO class

else:
    raise Exception("This file was not created to be imported")


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice

    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# setup variables
strFileName = "EmployeeData.txt"
lstOfObjects = []

# Load data from file
lstOfObjects = P.FileProcessor.read_data_from_file(strFileName)

# Begin loop for menu
while True:
    Eio.print_menu_items()
    strChoice = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if strChoice.strip() == '1':
        Eio.print_current_list_items(lstOfObjects)
        continue

    # Let user add data to the list of employee objects
    elif strChoice.strip() == '2':
        objE1 = Eio.input_employee_data()
        lstOfObjects.append(objE1)
        continue

    # let user save current data to file
    elif strChoice.strip() == '3':
        P.FileProcessor.save_data_to_file(strFileName, lstOfObjects)
        continue

    # Let user exit program
    elif strChoice.strip() == '4':
        print('Exiting')
        exit()

# Main Body of Script  ---------------------------------------------------- #
