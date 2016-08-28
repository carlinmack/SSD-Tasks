# Carlin MacKenzie, 25/08 -

# Fibonacci - iterative
prompt = int(input("range: "))  # asks for a number of sequence to go up to
digit1 = 0 
digit2 = 1
fibsum = 1
print("0")
for counter in range(prompt-1):  # iterates until it reaches the range
    print(fibsum)
    fibsum = digit1 + digit2  # calculates new value
    digit1 = digit2  # updates variables
    digit2 = fibsum

# Fibonacci - recursion
def fibonnaci(n):
    if n < 2:
        return n  # if the value asked for is 0 or 1, return them
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)  # finds the next lowest value

for counter in range(prompt):
    print (fibonnaci(counter))  # asks it to find the counter-th term of fibonnaci

# Factorial - recursive
def factorial(m):
    if m == 0:
        return 1
    if m == 1:
        return 1
    else:
        return factorial(m-1) * factorial(m-2)

#for counter2 in range(prompt):
print(factorial(5))
