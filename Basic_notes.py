# print("hello")

# age = 22
# print(age)
# print(type(age))

# Collection-a generic term for container types.
# Iterable-means a collectionthat can be iterated over using a loop.
# Sequenceis the generic term for an ordered collection.
# Immutable-means unchangeablecollection.
# Mutable-means changeablecollection

# String -ordered collection, immutable, iterable.
# List -ordered collection, mutable, iterable.
# Tuple -ordered collection, immutable, iterable.
# Set -unordered collection, mutable, iterable.
# Dictionary -unordered collection, mutable, iterable.

#  ***********Indentation matters! Don’t use it casually. Following code will report *****************
# anerror'Unexpected indent'.
# a = 20 
#     b =45 


# ********************Operator****************************
# 1.Arithmetic operator
# 2. Assignment Operator
# 3. Comparision Operator
# 4. Logical Operator
# 5. Membership Operator
# 6. Identity Operator

#swap two number

# a = 5
# b = 6

# a , b = b , a

# print("a=" , a)
# print("b=", b)

# #with third variable

# a = 50
# b = 60

# temp = a
# a = b
# b = temp
# print("a=" , a)
# print("b=", b)



# REPL use : direct write code into terminal and execute it directly 
# start REPL : write python in terminal, it run automatic

 #walrus operator (:=) - only use in REPL
 #assing variable in print(name:= Saiman pal) - here assign varibale in one line

#mini maths with pow() round() divmod()

# print(pow(2,3))
# print(round(3.2435674, 3))
# print(divmod(10, 4))






# ************x Sequence of execution of instructions in a program can be altered using:*************
# (a) Decision control instruction
# (b) Repetition control instruction

# ************************Decision Control Instruction********************
# x Three ways for taking decisions in a program:
# 1 (first)
# if condition :
# statement1 
# statement2

# 2 (Second)
# if condition :
# statement1 
# else :
# statement3

# 3(Third)
# if condition1 :
# statement1 
# elif condition2 :
# statement2
# elif condition3 :
# statement3
# else : 
# statement4

# *************************Conditional Expressions***************
# x Python supports one additional decision-making entity called a 
# conditional expression.
# <expr1> if <conditional expression> else <expr2>
# <conditional expression>is evaluated first. If it is true, the 
# expression evaluates to<expr1>. If it is false, the expression 
# evaluates to<expr2>.


#*************************Repetition control instruction******************
#  It helps us a repeat a set of statements in a program. There are two 
# types of repetition control instructions:
# (a) while 
# (b) for 

# Usage of while loop
#  A while loop can be used in following three situations:
# -Repeat a set of statements till a condition remains True.
# -Repeat a set of statements a finite number of times.
# -Iterate through a string, list and tuple.

# Usage of forloop
# x A forloop can be used in following two situations:
# -Repeat a set of statements a finite number of times.
# -Iterate through a string, list, tuple, set or dictionary

#  To repeat a set of statements a finite number of times abuilt-in 
# functionrange( )is used.
#  range( ) function generatesa sequence of integers.
# range(10) -generates numbers from 0 to 9.
# range(10, 20) -generates numbers from 10 to 19.
# range(10, 20, 2) -generates numbers from 10 to 19 in steps of 2.
# range(20, 10, -3) -generates numbers from 20 to 9 in steps of -3.
# Note that range( )cannot generate a sequence of floats.
# x In general, 
# range(start, stop, step)


# Problem 6.1
# Write a program that receives 3 sets of values of p, n and r and calculates simple interest for each.
# print("-------------------------------")
# i = 1
# while i <= 3 : 
#     p = float(input('Enter value of p: '))
#     n = int(input('Enter value of n: '))
#     r = float(input('Enter value of r: '))
#     si = p * n * r / 100
#     print('Simple interest = Rs. ' + str (si))
#     i: int = i + 1