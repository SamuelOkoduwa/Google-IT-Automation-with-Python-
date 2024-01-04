#!/usr/bin/python3

# Instance methods
 
class Piglet:
    name = "juicy"
    def speak(self):
        print("oink oink oink, I am {} Oink!" .format(self.name))

hamlet = Piglet()
hamlet.name = "Sammy"
hamlet.speak()

# Instance Methods that returns a value

class Returns:
    years = 0
    def pig_years(self):
        return self.years * 8

piggy = Returns()
print(piggy.pig_years())
piggy.years = 5
print(piggy.pig_years())

'''
Constructors and Other special methods
'''
# Creating an instance of a class
"""class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrip = Apple()
print(honeycrip.color, honeycrip.flavor)"""

# Modifying variables of similar instance as above
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
honeycrisp = Apple("green", "salty")
fuji = Apple("red", "sweet")
print("Honeycrisp is", honeycrisp.flavor, "and the color is", honeycrisp.color)
print("Fugi is", fuji.flavor, "and the color is", fuji.color)