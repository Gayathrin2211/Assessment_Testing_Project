# Assessment Automation Project

This project demonstrates a simple *automation framework* for testing different modules of a web-based assessment system.  
It includes automation for the following pages:

- *Dashboard*
- *Template*
- *Test Module*
- *Question Library*

---


## Features

- Uses *Selenium WebDriver* to automate browser actions.
- Supports *positive and negative test cases* for all modules.
- Demonstrates page object model (POM) design.
- Simple HTML pages for demo purposes.
- Prints success messages for each action to verify test execution.

---

## How to Run

1. Clone the repository:

```bash

cd Assessment_Testing_Project

2. Install required packages:



pip install -r requirements.txt

3. Run the tests using pytest:



python -m pytest tests/test_dashboard.py -v
python -m pytest tests/test_template.py -v
python -m pytest tests/test_test_module.py -v
python -m pytest tests/test_question_library.py -v

You will see output in the command prompt confirming that tests passed.


---

Demo Video

Watch the working demo here: https://drive.google.com/file/d/1vf-_gyOLN8yD1Y4Mo9brPYjr0ncswk1z/view?usp=drivesdk


---

Notes

This is a demo project, so the HTML pages are static.

Designed for assessment submission purposes.

The project structure follows Page Object Model (POM) to separate test logic from page actions.



---

Author

Gayathri.N

