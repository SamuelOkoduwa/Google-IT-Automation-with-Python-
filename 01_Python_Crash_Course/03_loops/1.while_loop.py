#!/usr/bin/python3

'''
	
while loops tell the computer to repeatedly execute a set of instructions while a condition is true.
'''

x = 0	#Initial value
while x < 5:	# Range of values
    print("not there yet, x=" + str(x))	#Iterated values
    print(x)	# Interated values
    x = x + 1 	# Increase by 1
# print("x=" + str(x))


# While loop inside a function
def attempts(n):
    x = 1
    while x < n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(7)

