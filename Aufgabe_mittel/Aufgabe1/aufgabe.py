n = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]
m = [2, 3, 4, 5, 6, 2, 3, 5, 4, 3]
output = n + m

def new_list(output):
    new_output = list(set(output))
    return new_output

print(new_list(output))

# dauert 10:40.45 ohne LLM

