# *********************************String_In_Python***************************************

# x Python string is a collection of Unicode characters.
# x Python strings can be enclosed in single, double or triple quotes.
# 'BlindSpot'
# "BlindSpot"
# ' ' 'BlindSpot' ' '
# """Blindspot"""

#  A sub-string can be sliced out of a string.
# s[start : end] -extract from start to end -1.
# s[start :] -extract from start to end.
# s[: end] -extract from start to end -1.
# s[-start :] -extract from -start (included) to end.
# s[: -end] -extract from beginning to -end -1.

#  **********************************Sting_Methods****************

# -----------------content test functions 
# isalpha( ) -checks if all characters in string are alphabets.
# isdigit( ) -checks if all characters in string are digits.
# isalnum()-checks if all characters in string are alphabets or digits.
# islower() -checks if all characters in string are lowercase alphabets.
# isupper() -checks ifall characters in string are uppercase alphabets.
# startswith()-checks if string starts with a value.
# endswith()-checks if string ends with a value.


# ----------------- search and replace
# find( )-searches for a value, returns its position.
# replace( )-replace onevalue with another.

# ------------------trims whitespace
# lstrip( ) -removes whitespace from the left of string including \t.
# rstrip( )-removes whitespace from the right of string including \t.
# strip( ) -removes whitespace from left and right

# --------------------split and partition
# split( )-split the string at a specified separator string.
# partition( ) -partitions string into 3 parts at first occurrence of 
# specified string.

# ---------------join 
# -different than concatenation. It joins string to each element of string1 except last. 
# join(string1) 

# *********************************************String_Conversion********************************

# ------------------------string methods:
# upper( ) -converts string to uppercase. 
# lower( ) -converts string to uppercase.
# capitalize()-converts first character of string to uppercase.
# title( ) -converts first character of each word to uppercase.
# swapcase()-swap cases in the string.
# str( ) -converts an int, float or complex to string
# int( ) -converts a numeric string to int
# float( ) -converts a numeric string to float
# complex( ) -converts a numeric string to complex


# *********************************************String_Comparision********************************
#  Two strings can be compared using operators ==, !=, <, >, <=, >=.
# Result of comparison operation is either True or False