'''Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument).'''

import sys

# The first argument is always the script name, so we subtract 1
num_arguments = len(sys.argv) - 1

print(f"Number of arguments provided: {num_arguments}")
