# -*- coding: utf-8 -*-
"""
Created on Thu Jan 4 19:29:03 2024

@author: patrick
"""
import os

# Function to clear the console
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function to display help menu
def show_help(shopping_list):
    clear_console()
    print("""
You have {} items in your current list.
Enter 'Help' to show this help menu again.
Enter 'Show' to see your current list.
Enter 'Remove' to remove an item.
Enter 'Clear' to delete your current list.
Enter 'Save' to save your new list and exit.
Enter 'Stop' to exit without saving.""".format(len(shopping_list)))

# Function to display the current shopping list
def show_list(shopping_list):
    clear_console()
    if not shopping_list:
        print("You have 0 items in your list.")
    else:
        print("\nHere's your list:\n")
        for num, item in enumerate(shopping_list, start=1):
            print(f"{num}.) {item}")

# Function to add a new item to the shopping list
def add_to_list(new_item, shopping_list):
    clear_console()
    shopping_list.append(new_item)
    print(f"Added {new_item}. List now has {len(shopping_list)} items.")

# Function to remove an item from the shopping list
def remove_from_list(shopping_list):
    clear_console()
    print("What item would you like to remove?\n")
    word = input("Remove an item: ")
    if word in shopping_list:
        shopping_list.remove(word)
        clear_console()
        print(f"{word} has been removed from your list.")
    else:
        clear_console()
        print(f"{word} is not in your list.")

# Function to read the saved list information from a file
def open_list(filename, shopping_list):
    try:
        with open(filename) as file:
            data = file.read().splitlines()
            shopping_list.extend(data)
    except FileNotFoundError:
        pass

# Function to save the current shopping list to a file
def save_list(filename, shopping_list):
    with open(filename, "w") as file:
        for item in shopping_list:
            file.write(item + "\n")
    print(f"\nYour new list has been saved to {filename}.")

# Function to delete the current shopping list and its corresponding file
def delete_list(filename, shopping_list):
    clear_console()
    shopping_list.clear()
    try:
        os.remove(filename)
        print("\nList deleted successfully.")
    except FileNotFoundError:
        print("\nList deleted successfully.")

# Main part of the script
saved_file = "shopping_list.txt"
shopping_list = []

# Load the existing shopping list from the file
open_list(saved_file, shopping_list)

# Display the initial help menu
show_help(shopping_list)

while True:
    # Ask the user for input
    new_item = input("\nAdd an item or enter a command: ")

    # Handle different user commands
    if new_item.upper() == "STOP":
        show_list(shopping_list)
        print("\nHappy Shopping!\n")
        break
    elif new_item.upper() == "HELP":
        show_help(shopping_list)
    elif new_item.upper() == "SHOW":
        show_list(shopping_list)
    elif new_item.upper() == "SAVE":
        show_list(shopping_list)
        save_list(saved_file, shopping_list)
        break
    elif new_item.upper() == "CLEAR":
        delete_list(saved_file, shopping_list)
    elif new_item.upper() == "REMOVE":
        remove_from_list(shopping_list)
    else:
        add_to_list(new_item, shopping_list)

