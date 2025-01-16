'''Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!'''

import sys

def process_temperatures(args):
    if len(args) == 0:
        print("No temperature readings provided. Please provide values as arguments.")
        return

    try:
        # Convert arguments to a list of floats
        temperatures = [float(temp) for temp in args]
        
        # Calculate max, min, and mean
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        
        # Display results
        print(f"Maximum temperature: {max_temp:.2f}")
        print(f"Minimum temperature: {min_temp:.2f}")
        print(f"Mean temperature: {mean_temp:.2f}")
    except ValueError:
        print("Invalid input. Please provide numeric values only.")

if __name__ == "__main__":
    # Exclude the script name from the arguments
    process_temperatures(sys.argv[1:])
