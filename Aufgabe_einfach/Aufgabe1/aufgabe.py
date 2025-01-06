def sum_of_odd_numbers(arr):
    return sum(x for x in arr if x % 2 != 0)

# Beispiel
a = [1, 2, 3, 4, 5]
output = sum_of_odd_numbers(a)
print(output)  # Erwartete Ausgabe: 9