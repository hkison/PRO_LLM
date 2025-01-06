def is_palindrome(s: str) -> bool:
    # Remove any spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print(is_palindrome(input_string))