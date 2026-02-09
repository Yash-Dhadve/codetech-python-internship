# Q1_TowerOfHanoi.py
# Program to implement Tower of Hanoi in Python

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# -------- USER INPUT --------
n = int(input("Enter number of disks: "))

print("\nTower of Hanoi solution:\n")
tower_of_hanoi(n, "A", "B", "C")

"""
Enter number of disks: 3

Tower of Hanoi solution:

Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
"""
