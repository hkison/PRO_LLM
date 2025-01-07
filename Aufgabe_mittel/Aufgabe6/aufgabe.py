def rotate_array(n, k, arr):
    k = k % n  # In case k is greater than n
    rotated_arr = arr[-k:] + arr[:-k]
    return rotated_arr

if __name__ == "__main__":
    # Read input
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Rotate array
    result = rotate_array(n, k, arr)
    
    # Print result
    print(" ".join(map(str, result)))