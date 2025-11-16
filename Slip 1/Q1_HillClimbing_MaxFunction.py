# Hill Climbing to find maximum of a function
# Function: f(x) = -x^2 + 4x

import random

# Define the mathematical function
def f(x):
    return -x**2 + 4*x

# Hill Climbing Algorithm
def hill_climbing(start_x, step_size=0.1, max_iterations=100):
    current_x = start_x
    current_value = f(current_x)

    for i in range(max_iterations):
        # Generate neighbor points
        next_x1 = current_x + step_size
        next_x2 = current_x - step_size

        # Evaluate neighbors
        f1 = f(next_x1)
        f2 = f(next_x2)

        # Move to better neighbor
        if f1 > current_value:
            current_x = next_x1
            current_value = f1
        elif f2 > current_value:
            current_x = next_x2
            current_value = f2
        else:
            break   # No better neighbor → local maximum reached

    return current_x, current_value

# Starting point (random between -5 to 5)
start = random.uniform(-5, 5)
best_x, best_value = hill_climbing(start)

print("Starting point:", start)
print("Best x value:", best_x)
print("Maximum value of f(x):", best_value)
