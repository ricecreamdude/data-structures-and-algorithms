# Hashtables
<!-- Short summary or background information -->
Hash tables are a common data structure used by compaines for testing prospective employees and are useful for processing data sets with repetitions. 

## Challenge
<!-- Description of the challenge -->
Create a hash table with the methods contains, get, hash, and add.

This hash table should handle collions and should be able to handle data points with identical keys

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Big O - Space
Space of this the size of the bucket, plus linked lists. (N + 1024?)

Big O - Time 
Initialization takes the longest time in this process, at 1024. Other than that, time is likely N, depending on the amount of data currently inside the linked list - Will have to review in class to know 

## API
<!-- Description of each method publicly available in each of your hashtable -->

contains - Detects if key exists within the hash table

get - Fetches values based on key - detects collisions

hash - Hashes values of keys

add - Adds values based on hashed key, and detects collions (multiple keys with identical hash values)

#TODO
Upgrade CONTAINS to detect keys