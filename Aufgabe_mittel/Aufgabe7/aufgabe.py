def longest_common_prefix(strings):
    if not strings:
        return "-1"
    
    # Find the shortest string in the list
    shortest_str = min(strings, key=len)
    
    for i, char in enumerate(shortest_str):
        for other in strings:
            if other[i] != char:
                return shortest_str[:i] if i > 0 else "-1"
    
    return shortest_str

if __name__ == "__main__":
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    result = longest_common_prefix(strings)
    print(result)