#Jewels and Stones
##Description
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

##Approach

My strategy is to split the function into two seperate parts:
1. Function: From the 'stones' string, create an object/dictionary that lists the number of times a specific character appears in the provided string. 
2. From the 'jewels' string, split into an array.  Use the stones object to retrieve stone count.  Sum the stone count values from the jewels array and return.  


##Big O Time and Space

Unfortunately this approach is O(n^2), since we are converting two strings into arrays and iterating through each of them.  We save some computational time by using a dictionary method to calculate total number of jewels, with the alternative being a nested for loop. 

Space complexity increases with each array that I create from the strings as well