from PIL import Image
import os

def resize_image(file, width, height):
    """Resizes the given image file to the specified width and height."""
    try:
        # Open the image file
        image = Image.open(file)

        # Display current size
        print(f"Current size: {image.size}")

        # Resize the image
        resized_image = image.resize((width, height))

        # Generate the output file name
        base_name, ext = os.path.splitext(file)
        output_file = f"{base_name}_resized_{width}x{height}{ext}"

        # Save the resized image
        resized_image.save(output_file)
        print(f"Image resized successfully! Saved as: {output_file}")
    except FileNotFoundError:
        print("Error: The file was not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to handle user inputs and resizing process."""
    file_name = input('Enter file name (with extension): ')
    
    try:
        width = int(input('Enter new width: '))
        height = int(input('Enter new height: '))
    except ValueError:
        print("Error: Width and height must be integers. Please try again.")
        return

    resize_image(file_name, width, height)

if __name__ == '__main__':
    main()
