#Reverse Numbers Alogirthm on Leetcode

##Question
Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

##Approach
My approach is to, by step:
Convert the input integer a string 
Convert the new string into a list
Rerverse the new list
Join the reversed list into a string
And finally return the newly joined string.

We also need to check that the provided value lies within 32-bit range, and to check whether or not the input is a negative number.  If the input is negative, remove the negative during the split and append the value later on.

##Big O Time
O(n) - we are using a 'for' loop within the split function to create a new list

##Big O Space
Space is not a focus for our algorithm - we define a lot of variables by creating and removing lists/strings. 

##Notes
This question uses a couple of interesting concepts that I have not encountered before:

*32-bit signed integer range* - [−2^31,  2^31 − 1]:  
This means that the output (or input?) of the method needs to lie within this range of numbers.  This is a hardware issue that I am not too familiar with

*Converting a number into a string includes the negative sign*:
str(-1) = '-1'.

