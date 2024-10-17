The homework consists of several tasks. You need to submit an archive with the solutions for these tasks.

If done completely, this homework is worth 15 points.

# Task 1: LLVM Primes (9 points)

Using `llvmlite`, you need to write two functions with LLVM IR which compile to native code. Each function is worth 4 points.

In `task1.py` provided alongside with the statements, you can find the template which prepares LLVM and runs your functions for testing, so you just need to fill in the code which constructs the required functions and adds them to the module. You need to submit a modified `task1.py` file.

The first function is `is_prime(i64) -> bool`. It takes `i64` and returns `bool` (essentially, `bool` is just a one-bit integer, thus `i1`). This function returns `true` if and only if the provided integer is prime. Use an `O(sqrt N)` algorithm to solve this problem.

The second function is `sum_primes(i64*, i64) -> void`. It takes a pointer to the first element of the array as the first argument and array size as the second argument. Then, the function calculates the sum of all the primes in the array and prints this sum using the predefined function `print(i64)`.

If you want to skip the second part of the task, just create an empty `sum_primes(i64*, i64)` which does nothing.

# Task 2: Finding a Clique in MiniZinc (3 points)

You are given a graph of N vertices as an adjacency matrix (i.e. an NxN matrix `a` filled with zeroes and ones, in which there is an edge between vertices `i` and `j` if an only if `a[i][j] == 1`).

_A clique_ in the graph is a subset of vertices such that there is a direct edge between each pair of vertices in the subset.

You need to find the clique of maximum size using MiniZinc. Submit the file `task2.mzn` as an answer.

## Example

_Input:_

```
[| 0, 0, 1, 0, 1, 1, 1, 0
 | 0, 0, 0, 1, 1, 1, 1, 1
 | 1, 0, 0, 0, 1, 1, 1, 1
 | 0, 1, 0, 0, 1, 1, 1, 1
 | 1, 1, 1, 1, 0, 1, 1, 1
 | 1, 1, 1, 1, 1, 0, 0, 0
 | 1, 1, 1, 1, 1, 0, 0, 1
 | 0, 1, 1, 1, 1, 0, 1, 0 |];
```

_Output:_

```
5 [2, 4, 5, 7, 8]
```

# Task 3: Chips (3 points)

105 white and black chips are arranged in a row. Among any five sequential chips there are at least two black ones. Find the maximum possible amount of white chips in the row.

Of course, use MiniZinc to solve the task. Submit the file `task3.mzn` as an answer.
