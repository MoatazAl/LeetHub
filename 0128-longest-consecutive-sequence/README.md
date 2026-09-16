# 128. Longest Consecutive Sequence

LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/

## Approach
Store all numbers in an `unordered_set` so membership checks are average `O(1)`.

Only start counting a sequence from a number whose predecessor (`num - 1`) is not in the set. From that starting point, keep checking `current + 1` until the consecutive sequence ends.

This avoids repeatedly traversing the same sequence from every element.

## Complexity
- Time: `O(n)` average
- Space: `O(n)`

## Key insight
A number is the start of a consecutive sequence only if `num - 1` does not exist in the set.
