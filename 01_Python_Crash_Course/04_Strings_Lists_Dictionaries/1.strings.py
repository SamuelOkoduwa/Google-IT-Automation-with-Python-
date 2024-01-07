#!/usr/bin/python3

# Strings in python are characters embedded in quotation marks. Strings are immutable

# There are lots of string method. These include
'''
.index()
.len()
.strip => removes lines or characters or element you may not need
	including white spaces either from the right using .rstrip() or from 
	the left using .lstript()
 .count()
 .endswith()
 .isnumeric
 .join()
 .split()
'''


# Creating a new string
message = "Can you modufy a string"
# Since strings are immutable, a new string is created,
# Let's say, we wanr to correct "modufy to modify", which
# has an index of 11, we can assign a new variable by

# Slicing

print(message, message[11])
new_message = message[:11] + "i" + message[12:] 
print(new_message)

# creating a new variable be redeclaring a new variable
message = "Can you modify the string"
print(message)

# How to know the index of a character? you use the index() method.
city = "New York is in USA"
the_index = city.index("w")
print(the_index)


'''# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
  fruit, weight, unit_price = item
  subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625  # 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("Total:", total)'''



# Using the format method
'''
fruit = "peaches"
weight = 3.0
per_pound = 2.99


output = "You are buying {} pounds of {} at {} per pound.".format(weight, fruit, per_pound)
print(output)


# Print the receipt for the customer. The format string ":10,.2f" 
# works as follows:
#   - ":10" makes the output 10 characters wide.
#   - "," inserts thousands separators between groups of digits.
#   - ".2" limits the output to two digits after the decimal.
#   - "f" tells Python to expect a floating-point number.
#
print("Subtotal:     ${:10,.2f}".format(subtotal))
print("Sales Tax:    ${:10,.2f}".format(tax_amt))
print("Total:        ${:10,.2f}".format(total))
'''


# ##########QUIZ##############
# 1)
'''
	Question 1
Fill in the blanks to complete the is_palindrome function. This function checks if a given string is a palindrome. A palindrome is a string that contains the same letters in the same order, whether the word is read from left to right or right to left. Examples of palindromes are words like kayak and radar, and phrases like "Never Odd or Even". The function should ignore blank spaces and capitalization when checking if the given string is a palindrome. Complete this function to return True if the passed string is a palindrome, False if not. 

def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for ___:

        # The if-statement checks if the "letter" is not a space.
        if letter != " ":

            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string = ___
            reverse_string = ___

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code. 
    if ___:

        # If True, the "input_string" contains a palindrome.
        return True
		
    # Otherwise, return False.
    return False


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

The solution below
'''
# The solution has a little defect

# def is_palindrome(input_string):
#     # Two variables are initialized as string date types using empty 
#     # quotes: "reverse_string" to hold the "input_string" in reverse
#     # order and "new_string" to hold the "input_string" minus the 
#     # spaces between words, if any are found.
#     new_string = ""
#     reverse_string = ""

#     # Complete the for loop to iterate through each letter of the
#     # "input_string"
#     for letter in input_string:
#         # The if-statement checks if the "letter" is not a space.
#         if letter != " ":

#             # If True, add the "letter" to the end of "new_string" and
#             # to the front of "reverse_string". If False (if a space
#             # is detected), no action is needed. Exit the if-block.
#             new_string = new_string + letter
#             reverse_string = letter + reverse_string

#     # Complete the if-statement to compare the "new_string" to the
#     # "reverse_string". Remember that Python is case-sensitive when
#     # creating the string comparison code. 
#     if new_string == reverse_string:
#         # If True, the "input_string" contains a palindrome.
#         return True
		
#     # Otherwise, return False.
#     return False


# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

# 2)
'''
	Question 2
Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {___} km".___
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

The solution below
'''
# def convert_distance(miles):
#     km = miles * 1.6 
#     result = "{} miles equals {:.1f} km".format(miles, km)
#     return result


# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


# 3)
'''
    Question 3
If we have a string variable named Weather = "Rainfall", which of the following will print the substring "Rain" or all characters before the "f"?

The solution below
'''
# The answer => print(Weather[:4])

# 4)
'''
    Question 4
Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
    return("___.".format(___))


print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

The solution below
'''
# def nametag(first_name, last_name):
#     return("{} {}.".format(first_name, last_name[0]))


# print(nametag("Jane", "Smith")) 
# # Should display "Jane S." 
# print(nametag("Francesco", "Rinaldi")) 
# # Should display "Francesco R." 
# print(nametag("Jean-Luc", "Grand-Pierre")) 
# # Should display "Jean-Luc G." 


# 5)
'''
    Question 5
The replace_ending function replaces a specified substring at the end of a given sentence with a new substring. If the specified substring does not appear at the end of the given sentence, no action is performed and the original sentence is returned. If there is more than one occurrence of the specified substring in the sentence, only the substring at the end of the sentence is replaced. For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made). 
    
def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    if ___:
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = ___
        new_sentence = ___
        return new_sentence


    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

The solution below
'''
# def replace_ending(sentence, old, new):
#     # Check if the old substring is at the end of the sentence 
#     if sentence.endswith(old):
#         # Using i as the slicing index, combine the part
#         # of the sentence up to the matched string at the 
#         # end with the new string
#         i = len(sentence) - len(old)
#         new_sentence = sentence[:i] + new
#         return new_sentence

#     # Return the original sentence if there is no match 
#     return sentence

# print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april")) 
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April")) 
# # Should display "The weather is nice in April"
