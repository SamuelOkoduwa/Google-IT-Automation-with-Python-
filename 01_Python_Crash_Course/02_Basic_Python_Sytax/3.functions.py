#!/bin/python3

'''Area of a trangle using function'''
def area_triangle(base, height):
    return (base * height) / 2

area = area_triangle(38, 6)
print(area)

# Return the sum of area of about two or more triangles
area_one = area_triangle(4,3)
area_two = area_triangle(7,3)
area_three = area_triangle(5,4)
sum_area = area_one + area_two + area_three
# print("The sum of the three areas is " + str(sum_area))




# Quiz Questions
"""
A. Conversion to meters 
"""
# 1) Complete the code to return the result of the conversion
def convert_distance(km):
	m = km * 1000  # exactly 1000 meters in 1 kilometer
	return m


# Do not indent any of the following lines of code as they are
# meant to be located outside of the function above


my_trip_kilometers = 55


# 2) Convert my_trip_kilometers to meters by calling the function above
my_trip_meters = convert_distance(my_trip_kilometers)


# 3) Fill in the blank to print the result of converting my_trip_kilometers
print("The distance in meters is " + str(my_trip_meters))



"""
B. Decalaring three parameters
"""
def print_seconds(hours, minutes, seconds):
    print(hours*3600+minutes*60+seconds)


print_seconds(1,2,3)