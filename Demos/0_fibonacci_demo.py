"""

Print all "fibonacci numbers", (The Fibonacci sequence is the series of numbers where each number
is the sum of the two preceding numbers.), 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

- No easy way to calculate how many numbers there will be - loop until you reach a limit

- Need to remember at least two numbers

"""

old = 0
current = 1
print(old)
print(current)
next = old + current

while next < 500:
    print(next)
    old = current
    current = next
    next = old + current
    
print("End of data")
print(next)