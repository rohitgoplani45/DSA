#LIST-COMPREHENSIONS

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)


# The pattern is 
#[expression for item in iterable]

#Create a list containing the squares of all numbers from 1 to 5.
def generate_squares():
    squares=[i*i for i in range(1,6)]

    return squares
    pass

#Create a list containing only the even numbers from 1 to 10.
def get_even_numbers():
    even_numbers=[i for i in range(1,11) if i%2==0]
    return even_numbers
    pass


Big-O = How running time grows as input size grows
n = 10   → 10 operations
n = 100  → 100 operations
n = 1000 → 1000 operations

We call the time complexity = O(n)

The 3 Complexities You Must Recognize First

O(1) — Constant Time
x = arr[0]
no matter what array size is

#O(n) — Linear Time
for i in arr:
    print(i)

#O(n²) — Quadratic Time
for i in arr:
    for j in arr:
        print(i, j)


Rule 3: Side-by-Side Loops
O(n) + O(n) → O(2n) → O(n)

(drop constants)

Rule 4: Keep Largest Term
O(n + n²) → O(n²)