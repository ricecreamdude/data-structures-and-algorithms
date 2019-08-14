# Get Max Tree Value
Take a binary tree (unsorted) and return the largest value in that tree

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
We need to make sure that each node is compared to in order for this to work. This means that our traversal
method needs to emcompass each node.

I used a recursive walk function in order to check each value. When the algorithm encounters
a value that is higher than the saved max value, it is updated.

## Solution
<!-- Embedded whiteboard image -->
![Find Max Tree](findMaxTree.jpg?raw=true "Title")

