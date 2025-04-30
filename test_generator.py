import csv
import os
import re
import random

def list_csv_files(directory="."):
    """
    Lists all CSV files in the given directory.
    """
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def load_test(filepath):
    """
    Loads test questions from a CSV file.
    Assumes the CSV has headers: question, optionA, optionB, optionC, optionD, answer, explanation.
    """
    questions = []
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, escapechar='\\')
            next(reader)
            for row in reader:

                cleaned_row = []

                for item in row:
                    new_item = re.sub('"', '', item)
                    cleaned_row.append(new_item)

                questions.append(cleaned_row)

    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return questions


def run_test(test_data):
    """
    Iterates over the test questions, displays them, and checks the user's answers.
    """
    random.shuffle(test_data)
    score = 0
    for i, question in enumerate(test_data, start=1):
        print(f"\nQuestion {i}: {question[0]}\n")
        
        # List of possible answers
        options_list = [
            question[1],
            question[2],
            question[3],
            question[4]
        ]

        # Shuffle the list
        random.shuffle(options_list)

        # Reassign letters for presenting shuffled letters
        presented_options = {}
        letter_list = ['A', 'B', 'C', 'D']

        for new_letter, text in zip(letter_list, options_list):
            presented_options[new_letter] = text


        correct_original = question[5].strip().upper()

        #Display the shuffled answer options
        for letter in letter_list:
            print(f"  {letter}. {presented_options[letter]}")



        # Retrieve input from the user and validate input

        user_answer = input("\nYour answer (A, B, C, D): ").strip().upper()

        while user_answer not in letter_list:
            print(f'You have selected an invalid option.\nPlease select a valid option.')
            user_answer = input("\nYour answer (A, B, C, D): ").strip().upper()

        if presented_options[user_answer].strip().upper() == correct_original:
            print("\nCorrect!")
            score += 1
        else:
            print(f"\nIncorrect. The correct answer was {correct_original}.")
        
        print("Explanation:", question[6])
        print("-" * 50)

    print(f"\nTest completed! Your score: {score}/{len(test_data)}\n")

def main():
    print("Welcome to the CSV Test Generator!\n")

    tests_folder = os.path.join(".", "tests")
    test_category_list = os.listdir(tests_folder)
    
    print("Select a category from the following folders:\n")
    for idx, folder_name in enumerate(test_category_list, start=1):
        print(f"{idx}. {folder_name}")

    try:
        category_selection = int(input("\nEnter the number of the category you'd like to take: ").strip())
        if category_selection < 1 or category_selection > len(test_category_list):
            print("Invalid selection. Please try again.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return 

    selected_category = test_category_list[category_selection -1]
    print(f"\nYou selected: {selected_category}\n")    
    
    
    
    tests_csvs = os.path.join(tests_folder, selected_category)

    # List all CSV files in the test directory
    files = list_csv_files(tests_csvs)
    if not files:
        print("No CSV test files found in the test directory.")
        return
    
    print("Select a test from the following files:\n")
    for idx, filename in enumerate(files, start=1):
        print(f"{idx}. {filename}")
    
    try:
        selection = int(input("\nEnter the number of the test you'd like to take: ").strip())
        if selection < 1 or selection > len(files):
            print("Invalid selection. Please try again.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    selected_file = files[selection - 1]
    print(f"\nYou selected: {selected_file}\n")
    
    # Load the test from the selected CSV file
    test_data = load_test(os.path.join(tests_csvs, selected_file))
    if test_data:
        run_test(test_data)
    else:
        print("The selected test file is empty or could not be loaded.")

if __name__ == '__main__':
    main()