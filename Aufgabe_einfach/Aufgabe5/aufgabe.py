def find_min_max(arr):
    if not arr:
        return None, None

    min_val = arr[0]
    max_val = arr[0]

    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements separated by space: ").split()))
    min_val, max_val = find_min_max(arr)
    print(f"The minimum value is: {min_val}")
    print(f"The maximum value is: {max_val}")