# Tree-of-Life
02assignment_cs582

# Algorithm
This algorithm can be split in several steps:

1. put all the values(matrix) to a list 
2. use the function distance to calculate all the distances.
3. use the min to choose the samllest and use pop remove these two tuples and append the new value by using the function "position"(which is to get the middle position)
4. becasue we knwo that in every level, we only need to cluster two tuples in one loop.


# draw the tree

When the global variable is more than 2, it will draw the node again and again until there are only two nodes left. The x axis position is decide by the the order from the data. Thx y axis position is decide by the global variable. 

# tree 
 ![](https://github.com/qijiepan/Tree-of-Life/blob/master/tree.png)
 the red polygon is from the data, and the white polygon is combined by two nodes.

# Additions
From the bio: it could be easier for person to distinguish from each animal from the tree.(Based on the column have the same weight, if not, we could choose weigh different column in different value) Here I assume all the column's weight are same, so we don't need to normalize it.

From the CS: it would be easier to understand the all the code by using different functions.

# How to run
download the tree of life. and open it with processing (python).
