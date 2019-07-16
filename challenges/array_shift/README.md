# Challenge Summary
Coding Challenge question for inserting data into the middle of an array 
## Challenge Description
Create a function that accepts two parameters:
- Array
- Value
The function will return an array with the value inserted into the halfway point of the array.  If the array's length is odd numbered, the halfway index will be rounded up.

 e.g. [1,2], 3    =>  [1,2,3]
 e.g. [1,2,3], 4 =>   [1,2,4,3]

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The approach I took capitalizes on the Python math module, as well as Python's ability to concatenate strings.

Big O space time for this approach is good, assuming that the split method is not loop oriented.

## Solution
<!-- Embedded whiteboard image -->
![Alt text](arrayShift.jpg?raw=true "Title")