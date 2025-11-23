● BMI CALCULATOR
● Overview of the project:
The code is a well-structured Python script designed to calculate a user's Body Mass Index (BMI) and classify their weight status based on World Health Organization 
(WHO) standards. It emphasizes modularity and robust error handling.
● Features :
This BMI calculator code is characterized by its modularity, robust error handling, and adherence to standards:
1)Modular Design: The program is divided into three distinct, single-purpose functions for calculation, classification (using WHO standards), and execution/user interface.
2)Strong Error Handling: It includes effective input validation to catch non-numeric entries and uses a ValueError exception to prevent calculation when the height is 
zero or negative.
3)Code Quality: It uses type hinting and docstrings for clarity and adherence to good Python programming practices.

● Technologies/tools used: 
The BMI calculator is a standalone script written entirely in the Python  programming language.
Python: The core language used for all logic, functions, and execution.
Standard Python Features: Relies exclusively on built-in language features like float() for input conversion, the try...except structure for robust error handling, 
and Type Hinting for code clarity.
● Steps to install & run the project :
1)Setup Prerequisites:
Ensure you have Python installed on your computer. The code works with Python 3.x.
Download and install Python from python.org if not already installed.
2)Prepare the Project:
Create a new folder for your BMI calculator project.
Inside this folder, create a new Python script file, e.g., bmi_calculator.py.
Copy the full BMI calculator code you provided into this file and save it.
3)Run the Project:
Open a terminal or command prompt.
Navigate to the folder where bmi_calculator.py is saved using the cd command.
Run the script, the program will prompt you to enter weight (in kilograms) and height (in meters).
Input the values as requested, and the program will calculate and display your BMI and classification.
4)Notes:
The project does not require installation of any external libraries because it uses basic Python functions.
Input validation and error handling are already included, so the user will be prompted if entries are invalid.
You can run the program multiple times in the terminal by re-executing the command above.

● Instructions for testing :
1)Manual Testing:
Run the program in a terminal or command prompt.
Enter various combinations of valid inputs for weight (kg) and height (m).
Confirm the output BMI and classification are correct according to BMI ranges:
   Underweight: BMI < 18.5
   Normal Weight: 18.5 ≤ BMI < 25.0
   Overweight: 25.0 ≤ BMI < 30.0
   Obese: BMI ≥ 30.0
Test boundary values such as exactly 18.5, 25.0, and 30.0 to ensure proper classification.
Enter invalid inputs for height (e.g., 0, negative numbers) or weight (negative) to verify error handling.
2)Automated Unit Testing:
Write unit tests for compute_body_mass_index with various valid and invalid inputs to check correct BMI values and exception raising on invalid height.
Write unit tests for determine_bmi_classification to verify it returns correct classifications for BMI values around each boundary.
Use Python's built-in unittest or pytest modules to run these tests automatically.
3)Additional Checks:
Test user inputs for various formats and invalid types to verify input validation in the interactive function.
Try edge cases such as very high or low but realistic weights and heights.

● Screenshots:
Input Code:
<img width="831" height="646" alt="Screenshot 2025-11-23 233345" src="https://github.com/user-attachments/assets/670023fa-57b4-4726-ab6d-b9aa51e22088" />
<img width="865" height="682" alt="Screenshot 2025-11-23 233406" src="https://github.com/user-attachments/assets/e9988645-afd3-48df-9b72-fcdd14abfaa7" />
<img width="849" height="463" alt="Screenshot 2025-11-23 233449" src="https://github.com/user-attachments/assets/809e9d21-f85b-4c0c-907c-f3a3fc45dfeb" />
Output:
<img width="668" height="175" alt="Screenshot 2025-11-23 233556" src="https://github.com/user-attachments/assets/5a26ef17-c0a3-4816-a600-07503728a23a" />











