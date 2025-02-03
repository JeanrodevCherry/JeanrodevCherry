Certainly! Here’s a simple Python function to calculate Fibonacci numbers using a recursive approach as well as an iterative approach.

### Recursive Approach

```python
def fibonacci_recursive(n):
    """Return the n-th Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage of the recursive function
print(fibonacci_recursive(10))  # Output: 55
```

### Iterative Approach

The recursive approach can be inefficient for larger values of `n` due to repeated calculations. Here’s an iterative approach which is much more efficient:

```python
def fibonacci_iterative(n):
    """Return the n-th Fibonacci number using iteration."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Example usage of the iterative function
print(fibonacci_iterative(10))  # Output: 55
```

### Using Dynamic Programming

You can also store previously calculated Fibonacci numbers to avoid redundant calculations as shown below:

```python
def fibonacci_dp(n):
    """Return the n-th Fibonacci number using dynamic programming."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    fib = [0] * (n + 1)
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Example usage of the dynamic programming function
print(fibonacci_dp(10))  # Output: 55
```

You can choose any of these methods according to your needs. The iterative and dynamic programming methods are generally preferred for larger values of `n` due to their efficiency.