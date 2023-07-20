def calculate_sum(numbers):
    try:
        # We want to Split the input by spaces and convert each part to a float number
        number_list = [float(num) for num in numbers.split()]

        # To Calculate the sum of all numbers in the list
        total_sum = sum(number_list)
        return total_sum
    except ValueError:
        return None  # Return None if the input cannot be converted to numbers


def main():
    while True:
        input_numbers = input("Enter a series of numbers separated by spaces: ")
        total_sum = calculate_sum(input_numbers)

        if total_sum is not None:
            print("The sum of the numbers is:", total_sum)
            break  # We want to Exit the loop if the input is valid and calculated
        else:
            print("Invalid input. Please enter numbers separated by spaces.")

if __name__ == "__main__":
    main()
