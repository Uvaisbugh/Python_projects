import os


def read_file(filename):
    """
    Reads the content of the specified file.
    Args:
        filename (str): The name of the file to read.
    Returns:
        str: The content of the file.
    """
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"[INFO] File '{filename}' does not exist yet.")
        return ""
    except Exception as e:
        print(f"[ERROR] Could not read file '{filename}': {e}")
        return ""


def write_file(filename, text):
    """
    Writes the given text to the specified file.
    Args:
        filename (str): The name of the file to write.
        text (str): The content to write to the file.
    """
    try:
        with open(filename, 'w') as f:
            f.write(text)
        print(f"[SUCCESS] File '{filename}' saved.")
    except Exception as e:
        print(f"[ERROR] Could not write to file '{filename}': {e}")


def append_file(filename, text):
    """
    Appends the given text to the specified file.
    Args:
        filename (str): The name of the file to append to.
        text (str): The content to append to the file.
    """
    try:
        with open(filename, 'a') as f:
            f.write("\n" + text)
        print(f"[SUCCESS] Content appended to file '{filename}'.")
    except Exception as e:
        print(f"[ERROR] Could not append to file '{filename}': {e}")


def get_user_input(initial_content=None):
    """
    Collects multi-line input from the user until 'SAVE' is entered.
    Args:
        initial_content (str): Optional initial content to display.
    Returns:
        str: The user's input as a single string.
    """
    if initial_content:
        print(f"\n[INFO] Current content:\n{initial_content}\n")

    print("Enter your text (type 'SAVE' on a new line to save and exit):")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "SAVE":
            break
        lines.append(line)

    return "\n".join(lines)


def display_menu():
    """
    Displays the main menu options for the user.
    """
    print("\n=== File Editor ===")
    print("1. Read file")
    print("2. Write to file (overwrite)")
    print("3. Append to file")
    print("4. Exit")


def main():
    """
    Main function to drive the file editor.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == "1":
            # Read a file
            filename = input("Enter the filename to read: ").strip()
            content = read_file(filename)
            if content:
                print(f"\n[FILE CONTENT] '{filename}':\n{content}")
            else:
                print(f"\n[INFO] '{filename}' is empty or does not exist.")

        elif choice == "2":
            # Write to a file (overwrite)
            filename = input("Enter the filename to write to: ").strip()
            content = get_user_input()
            write_file(filename, content)

        elif choice == "3":
            # Append to a file
            filename = input("Enter the filename to append to: ").strip()
            existing_content = read_file(filename)
            new_content = get_user_input(initial_content=existing_content)
            append_file(filename, new_content)

        elif choice == "4":
            # Exit
            print("[INFO] Exiting the program.")
            break

        else:
            print("[ERROR] Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
