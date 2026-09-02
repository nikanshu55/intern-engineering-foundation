# Intern Profile Program - Internal Workflow

## Overview

The program is a simple Python application that stores an intern's basic
information and displays it when the program is executed.

## Internal Working

1. The program first stores the intern's name, role, department, and skills
   in separate variables.

2. The skills are stored in a Python list so multiple skills can be maintained
   together.

3. The `print_profile()` function is responsible for displaying the intern's
   complete profile.

4. When `print_profile()` is called, it reads the stored profile values and
   prints them to the terminal.

5. The skills list is converted into a readable comma-separated string before
   it is displayed.

6. The `if __name__ == "__main__":` block ensures that the profile is printed
   when the file is executed directly.

## Program Flow

```text
Program starts
      ↓
Load intern profile data
      ↓
Store name, role, department and skills
      ↓
Call print_profile()
      ↓
Read profile data
      ↓
Format skills list
      ↓
Display profile in terminal
      ↓
Program ends