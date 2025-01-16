from collections import Counter

def most_common_letters(message):
    # Initialize the dictionary for letter counts (case-insensitive)
    letter_counts = Counter(char.lower() for char in message if char.isalpha())

    # Get the six most common letters
    most_common = letter_counts.most_common(6)

    # Print the results
    print("The six most common letters and their frequencies:")
    for letter, count in most_common:
        print(f"'{letter}': {count}")

if __name__ == "__main__":
    # Input message to analyze
    message = input("Enter the message: ")
    most_common_letters(message)
