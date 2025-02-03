You can calculate Fibonacci numbers using recursion in Python. Here's how you can create a function to do it:

```python
def fibonacci(n): 
    if n <= 0: 
        return "Input should be positive integer"
    elif n == 1: 
        return 0
    elif n == 2: 
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
```

This function works by calling itself to calculate the two previous Fibonacci numbers and adding them together. 

Note: This method is not very efficient for large numbers because it does a lot of repeated calculations. If you want to calculate Fibonacci numbers for large inputs, you could use a method that iterates over the numbers instead. For instance:

```python
def fibonacci(n):
    if n <= 0:
        return "Input should be positive integer"
    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n-1]
```

This second function stores all the Fibonacci numbers up to `n` in a list, so each number is only calculated once.