'''Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them.'''
import sys

# Get all the arguments excluding the script name
arguments = sys.argv[1:]

# Check if there are any arguments provided
if arguments:
    # Sort the arguments by length and pick the first one (shortest)
    shortest_argument = sorted(arguments, key=len)[0]
    print(f"The shortest argument is: {shortest_argument}")
else:
    print("No arguments were provided.")