
## Python Problems ##


-1. Create a python problem to perform the following:
- If X is a string:
-1. Please collect the full length of string

 -2. Please count total vowel and consonant in the given string.
 
-3. Write the string in the reverse from end to top
 
-4. Write each word in reverse string (pig-lattin) mode in the string
 
 Solution:
 
 ```
 def reverse_a_string(input_string):
    stringLength=len(input_string)
    reverseString=input_string[stringLength::-1]
    return reverseString
    
user_string = input("Please enter your string")
print("The user string length is ", len(user_string))
print("The reverse of the given string is ", reverse_a_string(user_string))'    
 ```
