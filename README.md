# practice_test_generator
A simple application that is intended to run through generated practice questions for certification exams. The questions were not created by the owners of the certification exams, nor did they contribute to the making of this. It may or may not be accurate.

This application is simply to aid in studying for the exams by making it easier to run through practice questions that one may generate using AI tools like Copilot, ChatGPT, or Gemini.

The requirements.txt file is only required if you wish to validate the practice test csv files. To install the requirements, run the below command:
```
    py -m pip install -r requirements.txt
```
## Table of Contents
- [practice\_test\_generator](#practice_test_generator)
  - [Table of Contents](#table-of-contents)
  - [To add a new test, do one of the following:](#to-add-a-new-test-do-one-of-the-following)
  - [To ensure the practice tests have the correct formatting:](#to-ensure-the-practice-tests-have-the-correct-formatting)

## To add a new test, do one of the following:
- Add it to the appropriate category folder in the tests/ folder 
- Make a new test category folder and place it in there.

The below is the format that the tests need to be in.
| Question | Option A | Option B | Option C | Option D | Correct Answer | Explanation |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | 
| What is the best animal? | Cats | Dogs | Birds | All of them | All of them | Because they are all amazing! |

**Advice:** Use a generative AI tool like Gemini, Copilot, or ChatGPT to generate practice tests. Ask it to format it in the above format without the answers being labeled (A, B, C, D). When done, place them in the practice_tests folder.

## To ensure the practice tests have the correct formatting:
Sometimes the AI can mess up the formatting of the CSV files. This section shows you how to validate the csv files to ensure it works correctly.

1. Ensure any new tests are in a category folder in the practice_tests/ directory
2. Run the below code to install the requirements (this only needs to be done once).

```
    py -m pip install --upgrade pip
    py -m pip install -r requirements.txt
```
3. Run the below command to run the unit tests.
```
    py -m pytest unit_tests/ 
```