#!/usr/bin/python3

# Module 3 Assessment

# 1) 
'''
	Question 1
Fill in the blanks to print the numbers from 15 to 5, counting down by fives.
number = ___ # Initialize the variable
while ___ # Complete the while loop condition
    print(number, end=" ")
    number ___ # Increment the variable

# Should print 15 10 5 

The solution below
'''
number = 15 # Initialize the variable
while number > 5: # Complete the while loop condition
    print(number, end=" ")
    number = number - 5 # Increment the variable
# Should print 15 10 5 


# 2) 
'''
	Question 2
Find and correct the error in the for loop.  The loop should print every number from 5 to 0 in descending order.

for number in range(5,-1):
    print(number)

# Should print:
# 5
# 4
# 3
# 2
# 1
# 0

The solution below
'''
# for number in range(5,-1,-1):
#     print(number)

# # Should print:
# # 5
# # 4
# # 3
# # 2
# # 1
# # 0


# 3)
'''
	Question 3
Fill in the blanks to complete the function “even_numbers(n)”. This function should count how many even numbers exist in a sequence from 0 to the given “n”number, where 0 counts as an even number.  For example, even_numbers(25) should return 13, and even_numbers(6) should return 4.

def even_numbers(n):
    count = 0
    current_number = 0
    while ___ # Complete the while loop condition
        if current_number % 2 == 0::
            ___ # Increment the appropriate variable
        ___ # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1

The solution below
'''
# def even_numbers(n):
#     count = 0
#     current_number = 0
#     while current_number <= n: # Complete the while loop condition
#         if current_number % 2 == 0:
#             count += 1 # Increment the appropriate variable
#         current_number += 1 # Increment the appropriate variable
#     return count
    
# print(even_numbers(25))   # Should print 13
# print(even_numbers(144))  # Should print 73
# print(even_numbers(1000)) # Should print 501
# print(even_numbers(0))    # Should print 1


# 4)
'''
	Question 4
Fill in the blanks to complete the “sequence” function. This function should print a sequence of numbers in descending order, from the given "high" variable to the given "low" variable.  The range should make the loop run two times. Complete the range sequences in the nested loops so that the “sequence(1, 3)” function call prints the following:

3, 2, 1

3, 2, 1

def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(___): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(___): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.

The solution below
'''
def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low - 1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.


# 5)
'''
	Question 5
Fill in the blanks to complete the “counter” function. This function should count down from the “start” to “stop” variables when “start” is bigger than “stop”. Otherwise, it should count up from “start” to “stop”. Complete the code so that a function call like “counter(3, 1)” will return “Counting down: 3, 2, 1” and “counter(2, 5)” will return “Counting up: 2, 3, 4, 5”.

def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while ___ # Complete the while loop
            ___ # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            ___ # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while ___ # Complete the while loop
            ___ # Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            ___ # Increment the appropriate variable
    return return_string


print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

The solution below
'''
# def counter(start, stop):
#     if start > stop:
#         return_string = "Counting down: "
#         while start >= stop:  # Complete the while loop condition
#             return_string += str(start)  # Add the numbers to the "return_string"
#             if start > stop:
#                 return_string += ","
#             start -= 1  # Decrement the appropriate variable
#     else:
#         return_string = "Counting up: "
#         while start <= stop:  # Complete the while loop condition
#             return_string += str(start)  # Add the numbers to the "return_string"
#             if start < stop:
#                 return_string += ","
#             start += 1  # Increment the appropriate variable
#     return return_string


# print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1))   # Should be "Counting down: 2,1"
# print(counter(5, 5))   # Should be "Counting up: 5"


# 6)
'''
	Question 6
Fill in the blanks to complete the “even_numbers” function. This function should return a space-separated string of all positive even numbers, excluding 0, up to and including the “maximum” variable that's passed into the function. Complete the for loop so that a function call like “even_numbers(6)” will return the numbers “2 4 6”. 

def even_numbers(maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for ___: 

        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        ___  

    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

The solution below 
'''
def even_numbers(maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for number in range(2, maximum + 1, 2): 

        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        return_string += str(number) + " "

    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


# 7)
'''
	Question 7
What happens when the Python interpreter executes a loop where a variable used inside the loop is not initialized?

The solution below
'''
# The answer => Will produce a NameError stating the variable is not defined


# 8)
'''
	Question 8
What is the final value of “x” at the end of this for loop? Your answer should be only one number.

The solution below
'''
# The answer => 7


# 9)
'''
	.
	Question 9
What is the final value of "y" at the end of the following nested loop code? Your answer should be only one number.

The solution below
'''
# The answer => 8


# 10)
'''
	Question 10
The following code causes an infinite loop. Can you figure out what is incorrect?

The solution below
'''
# The answer => When called with 0, it triggers an infinite loop