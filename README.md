# EasyPay

EasyPay is a Python-based hourly pay calculator created as a midterm project for CIT-115-Z02: Information Technology Fundamentals.

The program accepts basic employee and pay information, calculates regular and overtime pay, applies a simplified estimated deduction rate, and displays a formatted pay summary.

<img width="578" height="603" alt="image" src="https://github.com/user-attachments/assets/67ae561d-1655-4c7c-a620-45887c5305cd" />

## Features

EasyPay allows the user to enter:

- Employee name
- Hours worked
- Hourly rate
- Marital status

The program then calculates:

- Regular hours
- Overtime hours
- Regular pay
- Overtime rate
- Overtime pay
- Gross pay
- Estimated deductions
- Net pay

The final results are displayed using currency formatting with dollar signs, comma separators, and two decimal places.

## Input Validation

EasyPay includes validation to help prevent invalid entries.

The program:

- Rejects non-numeric entries for hours worked
- Rejects negative hours
- Rejects more than 168 hours in a pay period
- Rejects non-numeric hourly rates
- Rejects hourly rates of $0 or less
- Rejects hourly rates greater than $500
- Accepts marital status regardless of capitalization
- Removes extra spaces from marital-status input
- Re-prompts the user when an invalid marital status is entered

## Python Concepts Demonstrated

This project uses several Python concepts covered during the course and through additional project research, including:

- Variables
- User input
- Type conversion
- Arithmetic operators
- `if`, `elif`, and `else` statements
- `while` loops
- `try` / `except` error handling
- Comparison operators
- String methods such as `.strip()` and `.lower()`
- f-strings
- Numeric formatting
- Functions
- `main()` program structure
- Comments and PEP 8 formatting conventions

## Running the Program

EasyPay was written in Python 3 and developed using Thonny.

To run the program:

1. Download or clone this repository.
2. Open `EasyPay.py` in a Python 3 environment.
3. Run the program.
4. Follow the prompts in the console.

No additional Python packages are required.

## Testing

The final version of EasyPay was tested using multiple scenarios, including:

- Zero hours worked
- Exactly 40 hours
- Overtime
- Decimal hours and hourly rates
- Maximum accepted values
- Negative numbers
- Nonnumeric input
- Invalid marital-status entries
- Different capitalization and extra spaces
- Normal end-to-end use

All final test scenarios completed successfully.

## Important Note

The deduction percentages used by EasyPay are simplified estimated deduction rates created for demonstration purposes.

They are **not actual payroll tax calculations or withholding rates** and should not be used to calculate real employee payroll.

## Development

The project was developed incrementally through:

- Python coursework and Khan Academy practice
- Python documentation and PEP 8 research
- Hands-on coding and debugging
- Structured testing
- AI-assisted tutoring for concept explanation and troubleshooting

The program itself was written, tested, and debugged by the student. AI-assisted tutoring for this project was confirmed by the instructor as a permissible and responsible use of AI.

## Author

Teresa Zimmermann  
CIT-115-Z02: Information Technology Fundamentals
