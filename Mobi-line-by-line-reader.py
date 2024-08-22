import mobi
import html2text

tempdir, filepath = mobi.extract("</FILE>.mobi")
file = open(filepath, "r")
content=file.read()
lines = html2text.html2text(content).splitlines()

def print_line_by_line(lines, start_line=0):
    current_line = start_line
    while current_line < len(lines):
        user_input = input(" ").strip().lower()
        
        if user_input == 'q':
            print("Exiting the program.")
            break
        elif user_input == 'l':
            print(f"Last line number displayed: {current_line}")
        else:
            print(lines[current_line])
            current_line += 1

def main():
    # Display info about special keys
    print("Couple of basics:")
    print("- Press 'Enter' to display the next line.")
    print("- Press 'l' to print the number of the last line displayed.")
    print("- Press 'q' to quit the program.\n")

    # Ask the user if they want to skip to a certain line
    try:
        start_line = int(input("Enter a line number to start from (0 to start from the beginning): "))
    except ValueError:
        print("Invalid input, starting from the beginning.")
        start_line = 0

    # Print the file line by line, waiting for the Enter key
    print_line_by_line(lines, start_line)

if __name__ == "__main__":
    main()