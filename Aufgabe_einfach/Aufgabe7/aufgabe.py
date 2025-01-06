def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(arr):
    prime_count = 0
    for num in arr:
        if is_prime(num):
            prime_count += 1
    return prime_count

if __name__ == "__main__":
    input_numbers = list(map(int, input("Bitte geben Sie die Zahlen ein: ").split()))
    prime_count = count_primes(input_numbers)
    print(f"Die Anzahl der Primzahlen im Array ist: {prime_count}")