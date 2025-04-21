import csv
import os

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
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                questions.append(row)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return questions

def strip_answer(answer):
    """
    Formats the answer so that it can be properly read.
    
    """
    correct_answer_list = answer.split("-")
    correct_answer_formatted = correct_answer_list[0].strip()

    return correct_answer_formatted


def run_test(test_data):
    """
    Iterates over the test questions, displays them, and checks the user's answers.
    """
    score = 0
    for i, question in enumerate(test_data, start=1):
        print(f"\nQuestion {i}: {question[0]}\n")
        # Display each multiple-choice option
        options = {
            'A': question[1],
            'B': question[2],
            'C': question[3],
            'D': question[4]
        }
        for key, text in options.items():
            print(f"  {key}. {text}")
        
        user_answer = input("\nYour answer (A, B, C, D): ").strip().upper()
        correct_answer = question[5].strip().upper()

        if user_answer == strip_answer(correct_answer):
            print("\nCorrect!")
            score += 1
        else:
            print(f"\nIncorrect. The correct answer is {correct_answer}.")
        
        print("Explanation:", question[6])
        print("-" * 50)

    print(f"\nTest completed! Your score: {score}/{len(test_data)}\n")

def main():
    print("Welcome to the CSV Test Generator!\n")

    tests_folder = os.path.join(".", "tests")
    
    # List all CSV files in the test directory
    files = list_csv_files(tests_folder)
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
    test_data = load_test(os.path.join(tests_folder, selected_file))
    if test_data:
        run_test(test_data)
    else:
        print("The selected test file is empty or could not be loaded.")

if __name__ == '__main__':
    main()