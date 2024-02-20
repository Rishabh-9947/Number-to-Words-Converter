from num2words import num2words


# Convert a number to words
def number_to_words(number):
    return num2words(number)


# Main code
if __name__ == "__main__":
    # Input from the user
    number_input = int(input("Enter a number: "))

    # Convert the number to words
    words = number_to_words(number_input)

    # Output the result
    print(f"The number in words is: {words}")

