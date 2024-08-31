#test.py


import string_utils

#getting input from the user
sample_string = input("Enter your string:")

print("Original:", sample_string)
print("Reversed:", string_utils.reverse_string(sample_string))
print("Capitalized:", string_utils.capitalize_string(sample_string))
print("Uppercase:", string_utils.to_uppercase(sample_string))
print("Lowercase:", string_utils.to_lowercase(sample_string))
print("Is Palindrome:", string_utils.is_palindrome(sample_string))
