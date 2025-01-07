def is_valid_bracket_sequence(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

# Test the function with the example input
input_string = "({[]})"
print(is_valid_bracket_sequence(input_string))  # Output: True