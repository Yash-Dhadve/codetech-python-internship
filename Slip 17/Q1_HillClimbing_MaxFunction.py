# Q1_HillClimbing_MaxFunction.py
# Hill Climbing to find maximum of a mathematical function
# Example function: f(x) = -x^2 + 4x

import random

# Function to maximize
def f(x):
    return -x**2 + 4*x

# Hill Climbing Algorithm
def hill_climb(start_x, step=0.1, max_iter=100):
    current_x = start_x
    current_val = f(current_x)

    for i in range(max_iter):
        # Two neighbor points
        next_x1 = current_x + step
        next_x2 = current_x - step

        f1 = f(next_x1)
        f2 = f(next_x2)

        print(f"Iteration {i+1}: x = {current_x:.3f}, f(x) = {current_val:.3f}")

        # Move to better neighbor
        if f1 > current_val:
            current_x, current_val = next_x1, f1
        elif f2 > current_val:
            current_x, current_val = next_x2, f2
        else:
            break   # local maximum reached

    return current_x, current_val


# -------- RUNNING THE ALGORITHM --------
start = random.uniform(-5, 5)
print("Starting point =", start)

best_x, best_val = hill_climb(start)

print("\nMaximum found:")
print("x =", best_x)
print("f(x) =", best_val)


