#!/bin/bash

# Activate virtual environment
source "task-wizard/bin/activate"

# Function to display the menu
function display_menu() {
  echo "(1) Generate API keys"
  echo "(2) Extend epochs"
  echo "(3) Compare JSON files"
  echo "Enter your choice: "
}

# Get user input
display_menu
read -r choice

# Process user choice using a case statement
case $choice in
  1)
    python tasks/api_key_generator.py
    ;;
  2)
    python tasks/epoch_handler.py
    ;;
  3)
    # Script might require two file paths, prompt the user
    echo "Enter the path to the first JSON file: "
    read -r file1
    echo "Enter the path to the second JSON file: "
    read -r file2
    python tasks/json_comparator.py $file1 $file2  # Pass multiple arguments
    ;;
  *)
    echo "Invalid choice!"
    ;;
esac

