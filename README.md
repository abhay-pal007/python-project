# Attendance Calculator

## Project Overview

Attendance Calculator is a simple Python-based console program that calculates a student's attendance percentage from the total number of classes conducted and the number of classes attended.

The program also displays a remark and eligibility status according to the calculated attendance. If attendance is below 75%, it calculates the number of consecutive classes the student needs to attend to reach 75%.

## Features

- Takes student name as input.
- Takes subject name as input.
- Takes total number of classes conducted.
- Takes classes attended.
- Validates attendance details.
- Calculates attendance percentage.
- Displays a remark and eligibility status.
- Calculates additional consecutive classes required to reach 75% when attendance is below 75%.

## Requirements

- Python 3.x
- No external libraries are required.

## How to Run

1. Save the program as `attendance_calculator.py`.
2. Open a terminal/command prompt in the project folder.
3. Run:

```text
python attendance_calculator.py
```

## How It Works

The program calculates attendance using:

```text
Attendance = (Classes Attended / Total Classes) × 100
```

The result is then classified using the following conditions:

| Attendance | Remark | Status |
|---|---|---|
| 90% or above | Excellent | Eligible |
| 85% to below 90% | Good | Eligible |
| 75% to below 85% | Satisfactory-can be improved | Eligible |
| 65% to below 75% | low Attendance | Not Eligible |
| Below 65% | Very Low Attendance | Not Eligible |

If attendance is below 75%, a `while` loop increases the number of additional classes one at a time until the attendance reaches 75%.

## Input Validation

The program checks:

- Total classes must be greater than 0.
- Attended classes cannot be negative.
- Attended classes cannot be greater than total classes.

## Example

```text
==================================
      ATTENDANCE CALCULATOR
==================================
Enter student name: Abhay
enter subject name: Python
Enter total number of classes conducted: 40
Enter classes you attended: 30

---------- RESULT ----------
Student Name: Abhay
subject: Python
Total Classes: 40
Classes attended: 30
Attendance: 75.0 %

Remark: Satisfactory-can be improved
Status: Eligible
```

## Concepts Used

- `print()`
- `input()`
- Variables
- Integer data type
- Arithmetic operators
- Comparison operators
- Logical operators
- `if`, `elif`, `else`
- `while` loop

## Limitations

- Handles one student and one subject at a time.
- Does not store data permanently.
- Uses command-line interaction.
- Attendance criteria are fixed in the program.
- No graphical user interface is included.

## Future Scope

The project can be extended with a GUI, multiple students and subjects, file/database storage, attendance record management, report generation, and configurable attendance criteria.

## Conclusion

Attendance Calculator demonstrates how basic Python programming concepts can be combined to solve a simple real-world problem involving attendance calculation and eligibility.
