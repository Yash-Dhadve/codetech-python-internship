# Q1_MeanEndAnalysis_StringTransform.py
# Means-End Analysis algorithm to transform one string into another

def mean_end_analysis(start, goal):
    steps = []

    i = 0
    j = 0

    # Process both strings
    while i < len(start) and j < len(goal):
        if start[i] == goal[j]:
            # Characters match → move forward
            i += 1
            j += 1
        else:
            # Characters differ → REPLACE operation
            steps.append(f"Replace '{start[i]}' with '{goal[j]}' at position {i}")
            i += 1
            j += 1

    # If start string has extra characters → DELETE them
    while i < len(start):
        steps.append(f"Delete '{start[i]}' from position {i}")
        i += 1

    # If goal string has extra characters → INSERT them
    while j < len(goal):
        steps.append(f"Insert '{goal[j]}' at position {i}")
        j += 1
        i += 1

    return steps


# -------- USER INPUT --------
start_str = input("Enter start string: ")   
goal_str = input("Enter goal string: ")

operations = mean_end_analysis(start_str, goal_str)

print("\nSteps to transform using Means-End Analysis:\n")
for step in operations:
    print(step)


"""
Enter start string: cat
Enter goal string: cars
"""

