def double_elements(arr):
    return [2 * x for x in arr]

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    doubled_arr = double_elements(arr)
    print(" ".join(map(str, doubled_arr)))