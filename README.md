# Entry Fee Calculator Game

This is an interactive **Entry Fee Calculator** game built using Python's **Turtle Graphics** library. It allows users to input their gender and age to determine the corresponding entry fee in a fun and visually engaging way.

## Features

- **Graphical Interface**: Utilizes Turtle Graphics to display dynamic message boxes and an appealing UI.
- **Interactive Inputs**: Prompts users for gender and age using popup dialogs.
- **Error Feedback**: Displays clear error messages for invalid inputs directly on the Turtle canvas.
- **Customizable**: Designed with modularity to easily modify fee rules or extend functionality.

## How It Works

1. The program welcomes the user with a graphical message box.
2. The user is prompted to enter their gender (`M` for Male, `F` for Female).
3. The user is then prompted to enter their age.
4. Based on the inputs, the program calculates the entry fee using predefined rules:
   - **Male (M)**:
     - Age < 10: Free entry.
     - Age 11–20: Entry fee is 30RS.
     - Age 21–80: Entry fee is 50RS.
   - **Female (F)**:
     - Age < 10: Free entry.
     - Age 11–20: Entry fee is 20RS.
     - Age 21–80: Entry fee is 40RS.
5. The result is displayed in a dynamic message box with appropriate colors.
6. Invalid inputs (e.g., negative age or incorrect gender) trigger error messages.

## Prerequisites

- Python 3.7 or later
- **Turtle Graphics** (built-in with Python)

## Installation

No additional installations are required as Turtle Graphics is part of the Python standard library. Simply ensure Python is installed on your system.

## Running the Game

1. Copy the code into a file named `entry_fee_calculator.py`.
2. Run the program:
   ```bash
   python entry_fee_calculator.py
   ```
3. Follow the prompts and interact with the graphical interface.

## Example Interaction

### Input:

- Gender: `M`
- Age: `25`

### Output:

- A message box displays: **"Your entry fee is 50RS."** in blue text.

### Error Example:

- Input: Age `-5`
- Output: A message box displays: **"Age must be a positive number."** in red text.

## Customization

The entry fee rules can be customized in the `calculate_entry_fee` function. Modify the conditions to add new rules or change existing ones.

## Acknowledgments

- Built with Python’s **Turtle Graphics** library.
- Designed for learning and fun with an engaging graphical interface.
