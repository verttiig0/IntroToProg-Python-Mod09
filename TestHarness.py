# ---------------------------------------------------------- #
# Title: TestHarness.py
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# GShay,6.6.2021,Updated for Assignment09
# GShay,6.6.2021,added module imports
# GShay,6.8.2021,reworked Employee and Person tests
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Person as Per
    from DataClasses import Employee as Emp
    import ProcessingClasses as P  # processing classes
    from IOClasses import EmployeeIO as Eio

else:
    raise Exception("This file was not created to be imported")

# Test Person Class from data module
objP1 = Per("Bob", "Smith")
objP2 = Per("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module for Person Class
lstFileData = []
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_person_file("PersonData.txt")
print(lstFileData)


# Test Employee Class from data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test Processing module for Employee Class
lstFileData = []
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
print(lstFileData)


# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
Eio.input_employee_data()
print(Eio.input_menu_options())
