'''Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on.'''

def main():
    # A dictionary to store countries and their capitals
    capitals = {
        "france": "paris",
        "germany": "berlin",
        "italy": "rome",
        "spain": "madrid",
        "japan": "tokyo",
    }

    print("Welcome to the country-capital program!")
    print("Enter 'exit' to quit the program.")

    while True:
        # Ask the user to input a country
        country = input("Enter a country name: ").strip().lower()

        # Exit the program if the user types 'exit'
        if country == 'exit':
            print("Goodbye!")
            break

        # Check if the country is already in the dictionary
        if country in capitals:
            print(f"The capital of {country.title()} is {capitals[country].title()}.")
        else:
            # If the capital is not known, prompt the user to input it
            capital = input(f"I don't know the capital of {country.title()}. Please enter it: ").strip().lower()
            capitals[country] = capital  # Add the new country and capital to the dictionary
            print(f"Thank you! The capital of {country.title()} is now recorded as {capital.title()}.")

if __name__ == "__main__":
    main()
