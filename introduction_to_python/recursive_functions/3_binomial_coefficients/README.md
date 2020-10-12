# Binomial Coefficients

## Motivation
A binomial coefficient `B(n, k)` represents the number of ways to choose `k` elements from a set of `n` elements. This is a commonly used mathematical concept in probability and statistics. The formula for computing `B(n,k)` can be written as `B(n, k) = n choose k = n!/(k (n-k)!)`. However, using this formula, we may get an integer overflow because the factorials can grow large very quickly. Another way to define `B(n, k)` is `n choose k = (n-1 choose k-1) + (n-1 choose k)`.

## Problem Description
Define a recursive Python function named `binomial_coeff`, that consumes two non-negative integers, `n` and `k`, where `n >= k`, which returns the binomial coefficient `B(n,k)`.

## Examples
```
B(5,1) == 5
B(6,2) == 15
B(2,0) == 1
```
## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solutions* subdirectory within this directory
