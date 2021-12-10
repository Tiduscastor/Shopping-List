# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:29:03 2021

@author: patrick
"""
# To be able to create a save file and also clear the console screen for ease of viewing output
import os

#Declaring of list and variable to name the finished file
shopping_list = []
saved_file = "shopping_list.txt"

#Function to clear screen in program on new call
def clear_console():
    # Clear the console
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#initial instructional screen with optional commands
def show_help(list):
    clear_console()
    print("""
You have {} items in your current list.
Enter 'Help' to show this help menu again.
Enter 'Show' to see your current list.
Enter 'Remove' to remove an item.
Enter 'Clear' to delete your current list.
Enter 'Save' to save your new list and exit.
Enter 'Stop' to exit without saving.""".format(len(list)))

#shows current list and adds some prefacing numbers with '1.)' style
def show_list(list):
    clear_console()
    if len(list) == 0:
        print("You have 0 items in your list.")
    elif len(list) > 0:
        num = 1
        print("\nHere's your list:\n")
        for item in list:
            print(str(num) + ".)", item)
            num += 1

#adds new item to list. Be careful with typing it as you will need the exact typing to remove item.
def add_to_list(new_item, list):
    clear_console()
    # Add new items to the list
    list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(list)))

#function to remove item from list
def remove_from_list(list):
    clear_console()
    print("What item would you like to remove?\n")
    word = input("Remove an item: ")
    if word in list:
        # remove item from the shopping list
        list.remove(word)
        clear_console()
        print("{} has been removed from your list.".format(word))
    else:
        clear_console()
        print("{} is not in your list.".format(word))

#reads saved list information to be able to display it from the previously created file
def open_list(filename, list):
    try:
        with open(filename) as file:
            data = file.read().splitlines()
            list.extend(data)
    except FileNotFoundError:
        pass

#Save new list to file or creates one if it doesn't exist
def save_list(filename, list):
    with open(filename, "w") as file:
        for item in list:
            file.write(item + "\n")
    print("\nYour new list has been saved to {}.".format(filename))

#clears the previous list
def delete_list(filename, list):
    clear_console()
    list.clear()
    try:
        os.remove(filename)
        print("\nList deleted successfully.")
    except FileNotFoundError:
        print("\nList deleted successfully.")

open_list(saved_file, shopping_list)

show_help(shopping_list)

while True:
    # Ask for new items
    new_item = input("\nAdd an item or enter a command: ")

#reads input and acts accordingly. Input is set to Upper to offset user-input error
    if new_item.upper() == "STOP":
        show_list(shopping_list)
        print("\nHappy Shopping!\n")
        break
    elif new_item.upper() == "HELP":
        show_help(shopping_list)
        continue
    elif new_item.upper() == "SHOW":
        show_list(shopping_list)
        continue
    elif new_item.upper() == "SAVE":
        show_list(shopping_list)
        save_list(saved_file, shopping_list)
        break
    elif new_item.upper() == "CLEAR":
        delete_list(saved_file, shopping_list)
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list(shopping_list)
        continue
    else:
        add_to_list(new_item, shopping_list)
