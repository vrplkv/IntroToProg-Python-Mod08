# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Vera Poliakova,8.26.2021,Modified code to complete assignment 8
#   Added File Processor code
#   Added main body code
# Vera Poliakova, 8.31.2021,Modified code to complete assignment 8
#   Added code to define class Product
#   Add error handling to user inputs
# Vera Poliakova, 9.1.2021, Modified code to complete assignment 8
#   Add Product to list
#   Show data in current list
#   Print to file
# Vera Poliakova ,9.6.2021, Added error handling to create filename if it does not exist in file directory
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
menu_selection = None

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Vera,8.26.2021,

    """
    # -- Fields --

    # -- Constructor --
    def __init__(self, product_name, product_price):
        #-- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties --
    # Product Name
    @property
    def product_name(self): # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # Product Price
    @property
    def product_price(self):  # (getter or accessor)
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):  # (setter or mutator)
        if str(value).isnumeric() == True:
            self.__product_price = value
        else:
            raise Exception("Price must be a number")
    # -- Methods --

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Vera,9.1.2021, Added code to save_data_to_file
        Vera,9.1.2021, Added code to read_data_from_file
        Vera,9.6.2021, Added error handling to create filename if it does not exist in file directory
    """

    # Process data from a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        objFile = open(file_name, "w")  # open textfile
        for obj in list_of_product_objects:  # write each row in the list to the text file
            objFile.write(obj.product_name + ", " + obj.product_price + "\n")
        objFile.close()
        print("Data saved to", file_name,"\b!")


    @staticmethod
    # Process data to a file
    def read_data_from_file(file_name):
        objFileData = []
        #Open existing file or create a blank one with no data
        try:
            objFile = open(file_name, "r")
        except FileNotFoundError:
            print("File did not exist. But we created one for you!")
            open(file_name, "x")  # create file
            objFile = []
        for line in objFile:
            name, price = line.split(",")
            objFileData.append(Product(product_name=name, product_price=price))
        objFile.close()
        print("Data retrieved from", file_name,"\b!")
        return objFileData

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Asks user data inputs:

    properties:
        menu_selection: (integer) with the menu option number the user has chosen
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        print_menu()

    changelog: (When,Who,What)
        Vera,8.26.2021, Created Class
        Vera,8.26.2021, Added function to print menu for user
        Vera,8.26.2021, Added function to get input for menu selection from user
        Vera,8.26.2021, Show the current data from the file to user using print(lstOfProductObjects)
        Vera,8.26.2021, Get input from user on a product name and price
    """

    # Show menu to user
    @staticmethod
    def print_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data in the list of product objects
        2) Add data to the list of product objects
        3) Save current data to file and exit program      
        ''')
        print()  # Add an extra line for looks

    # Get user's menu selection
    @staticmethod
    def get_user_menu_selection():
        """ Gets the menu selection from a user

        :return: string
        """
        menu_selection = int(input("Select menu item number:"))
        print()  # Add an extra line
        return menu_selection

    # Show the current data from the file to user
    @staticmethod
    def print_current_Tasks_in_list(product_object_list):
        """ Shows the current Tasks in the list of dictionaries rows

        :param lstOfProductObjects: (list) of product objects you want to display
        :return: nothing
        """
        print("--------- The current Products are: ---------")
        for obj in product_object_list:
            print(obj.product_name, obj.product_price, sep =' ')
        print("---------------------------------------------")
        print()  # Add an extra line

    #Get input from user and return the input
    @staticmethod
    def get_input(prompt,variableType,booleanVariableTypeIsString):
        while True:
            try:
                userInput = variableType(input(prompt))
                if variableType == str:
                    if userInput.isnumeric() == booleanVariableTypeIsString:
                        raise Exception()
                return userInput
            except Exception:     #Error Handling based on variable type
                if variableType == str:
                    strVariableType = "\b, not a string!"
                elif variableType == float:
                    strVariableType = "\b, not a number!"
                else:
                    strVariableType = "\b! "
                print("Error",strVariableType,"Try again!")

    # Call get_input() for product name and product price, return both variables
    @staticmethod
    def add_product_name_and_price():
        product_name = IO.get_input("What is the product name?", str, True)
        product_price = IO.get_input("What is the product's price?", float, False)
        return product_name, product_price




# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while(True):
    # Show user a menu of options
    IO.print_menu()

    # Get user's menu option choice
    menu_selection = IO.get_user_menu_selection()

    # Show user current data in the list of product objects
    if menu_selection == 1:
        IO.print_current_Tasks_in_list(lstOfProductObjects)

    # Let user add data to the list of product objects
    elif menu_selection == 2:
        name, price = IO.add_product_name_and_price()
        lstOfProductObjects.append(Product(product_name=name, product_price=price))

    # Let user save current data to file and exit program
    elif menu_selection == 3:
        FileProcessor.save_data_to_file(strFileName,lstOfProductObjects)
        break

    # Let user know they selected an invalid menu item
    else:
        print("Invalid menu item.")
        continue

# Main Body of Script  ---------------------------------------------------- #

