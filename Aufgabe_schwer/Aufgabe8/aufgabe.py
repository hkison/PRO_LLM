def length_of_lis(arr):
    if not arr:
        return 0

    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(length_of_lis(arr))