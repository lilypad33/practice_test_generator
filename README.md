# practice_test_generator
A simple application that is intended to run through generated practice questions for certification exams. The questions were not created by the owners of the certification exams, nor did they contribute to the making of this. It may or may not be accurate.

## To add a new test do one of the following:
- Add it to the appropriate category folder in the tests/ folder 
- Make a new test category folder and place it in there.

The below is the format that the tests need to be in.
| Question | Option A | Option B | Option C | Option D | Correct Answer | Explanation |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | 
| What is the best animal? | Cats | Dogs | Birds | All of them | All of them | Because they are all amazing! |

## To ensure the practice tests have the correct formatting:

1. Ensure any new tests are in a category folder in the practice_tests/ directory
2. Run the below code to run the unit tests.

```
    py -m pip install --upgrade pip
    py -m pip install -r requirements.txt
    py -m pytest tests/ 
```