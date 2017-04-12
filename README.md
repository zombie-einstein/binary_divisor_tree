# binary_divisor_tree
## Binary tree based on node divisors

Each node has has left and right children based on whether the node is/isn't a divisor of child, in a similar manner to the children of nodes in a regular binary tree being larger/smaller than the node. 

For example starting from a root value 2 then inserting the next 7 integers 3...9 results in

    __2__
   /     \
  4       3
 / \     / \
8   6   9   5
             \
              7

Currently this is only a basic implementation. A couple of things are easy to spot
* Iterating down right children will return list of (relative to root) primes
* Iterating down left children will return powers of root
Not actually wholly sure if this is practically useful or just fun twist on b-tree (though some cool stuff has come from things that just seemed interesting!). 