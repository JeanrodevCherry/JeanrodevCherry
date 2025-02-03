Sure, here is the Python function to calculate Fibonacci numbers.

```python
def fibonacci(n):
    if n <= 0:
        return "Input should be positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0,1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[len(fib_sequence) - 1] + fib_sequence[len(fib_sequence) - 2])
        return fib_sequence[n-1]

print(fibonacci(9))  # it will print 21 as result
```
This function `fibonacci(n)` works as follows:

1. If `n` is less than or equal to 0, then it returns a message "Input should be positive integer".
2. If `n` is 1, it returns 0, since the Fibonacci sequence starts with 0.
3. If `n` is 2, it returns 1, since the second number in the Fibonacci sequence is 1.
4. If `n` is greater than 2, it calculates the Fibonacci number as the sum of the previous two numbers in the Fibonacci sequence.

Remember Fibonacci sequence is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....etc. It always start with 0 and 1, and each subsequent number in the sequence is the sum of the previous two.