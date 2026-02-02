import re
import os

# Regex patterns
patterns = {
    "Email": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "URL": r"^https?://[^\s]+$",
    "Phone": r"^(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})$",
    "Credit Card": r"^(\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4})$",
    "Time": r"^((1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM)|([01]?[0-9]|2[0-3]):[0-5][0-9])$",
    "HTML Tag": r"^<[^>]+>$",
    "Hashtag": r"^#\w+$",
    "Currency": r"^\$\d{1,3}(,\d{3})*(\.\d{2})?$",
}

# Loading data file
def load_data(filename="data.txt"):
    if not os.path.exists(filename):
        print("Data file not found!")
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]
                
# CLI System
def main():
    data_list = load_data("data.txt")

    while True:
        print("\nREGEX DATA EXTRACTION SYSTEM")
        print("Choose category to extract valid data:")
        for i, key in enumerate(patterns.keys(), start=1):
            print(f"{i}. {key}")
        print(f"{len(patterns)+1}. Exit")

        choice = input("Enter choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input, enter a number!")
            continue 
        
