
## Python Problems ##

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
 
 def check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    return (len(final)) 
    return (final) 
       
string = user_string 
vowels = "AaEeIiOoUu"

def check_Con(string, vowels): 
    final1 = [each for each in string1 if each in Consonants] 
    return (len(final1)) 
    return (final1) 
    
string1 = user_string
Consonants = "QqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"

def pig_Latin(input_string):
    input_string_array = (input_string.split(" "))
    len_string_array = len(input_string_array)
    for each_word in input_string_array:
        print("The reverse of ", each_word, " is ", reverse_a_string(each_word))


user_string = input("Please enter your string")
print("The user string length is ", len(user_string))
print("The reverse of the given string is ", reverse_a_string(user_string))
print(" the number or vowles is", check_Vow(user_string, "AaEeIiOoUu"))
print(" the number or vowles is", check_Con(user_string, "QqWwRrTtYyIiPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"))
pig_Latin(user_string)
 ```

## Improved Version:

```
def reverse_a_string(input_string):
    stringLength=len(input_string)
    reverseString=input_string[stringLength::-1]
    return reverseString
 
 def check_vowel_or_Con(string, vc_type):
    vowels = "AaEeIiOoUu"
    Consonants = "QqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
    if vc_type == 'v' or vc_type == 'V':
         result = [each for each in string if each in vowels] 
    elif vc_type == 'c' or vc_type == 'C':
         result = [each for each in string if each in Consonants] 
    else:
        print('Wrong choice...')
    return result, len(result) 

def pig_Latin(input_string):
    input_string_array = (input_string.split(" "))
    len_string_array = len(input_string_array)
    for each_word in input_string_array:
        print("The reverse of ", each_word, " is ", reverse_a_string(each_word))


user_string = input("Please enter your string")
print("The user string length is ", len(user_string))
print("The reverse of the given string is ", reverse_a_string(user_string))
v_list, v_len = check_vowel_or_Con(user_string, "v")
print(" the number or vowles is ", v_len, " and the list of vowels are ", v_list)
c_list, c_len = check_vowel_or_Con(user_string, "C")
print(" the number or Consonents is ", c_len, " and the list of Consonents are ", c_list)

pig_Latin(user_string)
```
