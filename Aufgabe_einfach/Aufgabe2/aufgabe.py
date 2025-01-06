def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print(count_vowels(input_string))