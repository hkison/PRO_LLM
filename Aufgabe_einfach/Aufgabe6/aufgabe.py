def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)

if __name__ == "__main__":
    # Read input from the user
    print("Enter numbers separated by spaces:")
    numbers = list(map(int, input().split()))
    # Calculate the sum of squares
    result = sum_of_squares(numbers)
    # Print the result
    print("The sum of squares is:", result)