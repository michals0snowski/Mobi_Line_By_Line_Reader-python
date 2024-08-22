# MOBI File Line-by-Line Reader

This Python program reads a `.mobi` file and displays its content line by line in the console. Users can navigate through the text by pressing the `Enter` key, check the last displayed line number by pressing `l`, or quit the program by pressing `q`. Additionally, the program allows users to start reading from a specific line number.

## Features

- **Line-by-Line Navigation:** Press `Enter` to display the next line of the MOBI file.
- **Display Last Line Number:** Press `l` to see the line number of the last line displayed.
- **Quit Program:** Press `q` to exit the program at any time.
- **Start from Specific Line:** On startup, the program asks if the user wants to begin reading from a specific line.

## Prerequisites

- Python 3.x
- Install the necessary Python packages:
- mobi
- html2text

You can install the required packages using pip:

```
pip install mobi html2text
```

# Usage
Edit and provide your MOBI file path and name in the file.
Run the script:

```
python reader.py
```

The program will display instructions on how to navigate through the text.

You'll be asked if you want to start from a specific line. Enter a number to skip to that line or 0 to start from the beginning.

Use the following keys while navigating the text:

Press Enter to display the next line.
Press l to display the last line number.
Press q to quit the program.

```
Instructions:
- Press 'Enter' to display the next line.
- Press 'l' to print the number of the last line displayed.
- Press 'q' to quit the program.

Enter a line number to start from (0 to start from the beginning): 50
<line 50 text>
<line 51 text>
Last line number displayed: 51
Exiting the program.
```

## License
This project is licensed under the MIT License.
