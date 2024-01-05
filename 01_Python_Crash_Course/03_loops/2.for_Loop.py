#!/usr/bin/bash

'''# Basic for loop using range
for x in range(5):
    print(x)
# print(x)


# More For Loops
product = 1
for n in range(1,10):
    # product = product * n
    # print(n)

print(product)'''

# Intervals
def to_celcius(x):
    return (x - 32) * 5/9

for x in range(0, 101, 10):
    print(x, to_celcius(x))
    

# Nested loops
teams = [ 'Dragons', 'Wolves', 'Manchester United', 'Chelsea']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)



'''For Loop Quiz'''
# 1) 
'''
    Question 1
How are while loops and for loops different in Python?

Solution below
'''
# while loops iterate while a condition is true; for loops iterate through a sequence of elements.


# 2)
'''
    Question 2
Which option would fix this for loop to print the numbers 12, 18, 24, 30, 36?

The solution below
'''
# for n in range(6,18+1,3):
#   print(n*2)


# 3)
'''Question 3
Which for loops will print all even numbers from 0 to 18? Select all that apply.

The solution below
'''
# for n in range(19):
#     if n % 2 == 0:
#         print(n)

# for n in range(10):
#     print(n+n)    

# 4)
'''
    Question 4
Fill in the blanks so that the for loop will print the first 10 cube numbers (x**3) in a range that starts with x=1 and ends with x=10.
for __ in range(__,__):
  print(___)

The solution below
''' 
# for x in range(1, 10+1):
#   print(x**3)

# 5)
'''
    Question 5
Write a for loop with a three parameter range() function that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7. 
for ___: 
    print(___)

The solution below
'''
# for x in range(0, 100+1, 7): 
#     print(x)


# 6)
'''
    Question 6
Which of these options would output just the vowels from the following string? Select all that apply.

The solution below
'''
# for c in input:
#   if c.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print(c)
    
# print([c for c in input if c.lower() in ['a', 'e', 'i', 'o', 'u']])


# 7)
'''
    Question 7
Which of these statements is true about slicing strings?

The solution below
'''
# If the starting index is negative, Python counts backward from the end of the string.