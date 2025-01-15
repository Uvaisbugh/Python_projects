def binary_search(lst, element):
    """
    Performs binary search on a sorted list to find the index of a given element.

    Args:
        lst (list): The sorted list to search in.
        element (int): The element to search for.

    Returns:
        int: The index of the element if found, otherwise -1.
    """

    # Initialize variables for the start and end of the search range.
    start = 0
    end = len(lst) - 1  # Set to len(lst) - 1 as indices are zero-based.
    steps = 0  # Counter to track the number of steps (iterations).

    # Continue searching until the start index is greater than the end index.
    while start <= end:
        print(f"Step {steps}: {str(lst[start:end+1])}")  # Display the current search range.
        steps += 1  # Increment the step counter.

        # Calculate the middle index of the current search range.
        middle = (start + end) // 2

        # Check if the element at the middle index matches the target.
        if element == lst[middle]:
            return middle  # Element found, return its index.

        # If the target element is smaller, adjust the end index.
        if element < lst[middle]:
            end = middle - 1
        # If the target element is larger, adjust the start index.
        else:
            start = middle + 1

    # If the loop ends, the element is not in the list.
    return -1


# Example usage:
# Define a sorted list.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Prompt the user to enter the target element.
target = int(input("Enter the target number: "))

# Perform the binary search and capture the result.
result = binary_search(my_list, target)

# Display the result.
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found.")
