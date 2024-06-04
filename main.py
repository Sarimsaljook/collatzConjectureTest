def collatz_sequence(n, cache):
    if n in cache:
        return cache[n]

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    cache[sequence[0]] = sequence  # Store the sequence in the cache
    return sequence

def find_non_converging_collatz(starting_number, max_iterations=1000000):
    current_number = starting_number
    iterations = 0
    cache = {}  # Cache to store computed sequences

    while iterations < max_iterations:
        sequence = collatz_sequence(current_number, cache)

        # Check if the sequence reaches 1 or gets stuck in the 4-2-1 loop
        if sequence[-1] != 1:
            print(f"Found a number that doesn't converge: {current_number}")
            print(f"Collatz sequence for {current_number}: {sequence}")
            break

        current_number += 1
        iterations += 1

    if iterations == max_iterations:
        print(f"After {max_iterations} iterations, none found.")

# Example: Find a number that doesn't get stuck in the 4-2-1 loop
find_non_converging_collatz(1)
