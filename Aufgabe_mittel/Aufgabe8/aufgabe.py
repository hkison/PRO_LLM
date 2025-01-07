def count_unique_elements(n, arr):
    element_count = {}
    
    # Count the occurrences of each element
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    
    # Count the number of unique elements
    unique_count = 0
    for count in element_count.values():
        if count == 1:
            unique_count += 1
    
    return unique_count

# Example usage
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_unique_elements(n, arr))