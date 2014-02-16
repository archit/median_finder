## README

This library implements a median finder algorithm that is eventually
distributable. 

## Requirements

Depends on python3, nosetests

## How to run?

```
$ git clone github.com:archit/median_finder.git
$ cd median_finder
$ python3 -m median_finder
Usage: python3 -m median_finder [bucket_size] [input_file]
$ python3 -m median_finder 5 tests/input1.txt
```

## Runtime Analysis

This python package implements finding the median of a stream of given
numbers using two strategies.

### NaiveMedianFinder

The NaiveMedianFinder implements a simple in-memory array strategy.
The algorithm is
  1. Add numbers to an array
  2. Sort the array
  3. Reference the median using array access.

The run time efficiency is thus O(n) + O(n.log(n)) = O(n.log(n))

### SophisticatedMedianFinder

The SophisticatedMedianFinder strategy uses Binary Search Tree, where
each node consists of a `bucket`. Each bucket is an array of numbers
that is limited to a pre-defined size |B| (This is done to simulate
finding the median of a large stream of numbers, which could out do
the memory limit on a single processing machine). 

When inserting an element it follows the same strategy as a Binary
Search Tree. At each node the algorithm checks if there is space in
the bucket. If so, it inserts the number using an insertion sort
algorithm.. In the event the bucket is full, the algorithm takes the
following decision,
1. If the number falls in the range of the current bucket, it inserts
the number in the bucket and removes either the min or the max number
from the bucket, and then recursively calls insert for the new
orphaned number in either the left or the right child tree, based on
the ordering of the number with respect to the bucket.
2. If the number is smaller than the minimum of the bucket, it
recursively goes down the left child tree, to find a bucket with
available capacity.
3. If the number is greater than the maximum of the bucket, it
recursively goes down the right child tree, to find a bucket with
available capacity.

The time complexity of these insertion step
average case: O(n.log(n/|B|)) where |B| is size of the bucket
worst case:   O(n^2)

Once the BST is setup, finding the median is relatively easy. The
algorithm uses an in-order traversal to find the bucket containing the
median of all the numbers, and then returns the median from that
bucket. The time complexity of this find step
average case: O(log(n/|B|)) where |B| is size of the bucket
worst case:   O(n)

The overall algorithm complexity is
average case: O(n.log(n/|B|)) where |B| is size of the bucket
worst case:   O(n^2)

## Suggested Improvements

To improve the worst case performance of the BST, we can switch to a
Red-Black Tree, so as to keep the tree balanced, resulting in worst
case complexity being the same as average case complexity. 
