***
#	Crash Course in python

***
##	Module 1
###	Objectives

+ Define the terms computer program, programming language, script, and automation 
+ Use the print() function to output data to the screen
+ Explain the difference between the syntax and semantics of a programming language
+ List some of the characteristics of the Python language
Utilize basic Python arithmetic operators to obtain the results of mathematical expressions


###	Content

+ Introduction to python
+ Using the [Print function()](./01_Hello_Python/hello.py) to print Hello world on the screen
+ Basic Mathematical [Arithmetic Operation](./01_Hello_Python/hello.py) in Python

***

##	Module 2
###	Objectives

+ Differentiate and convert between different data types utilizing variables
+ Define and call functions utilizing parameters and return data
+ Refactor code and write comments to reduce complexity and enhance code readability and code reuse
+ Compare values using equality operators and logical operators
+ Build complex branching scripts utilizing if, else and elif statements


###	Content
+	**Basic python Syntax**
	+ Basic Python syntax
	+ Python Data Types
	+ Naming variables
	+ Expressions, numbers and types conversions
	+ Implicit and explicit conversion

+ **Functions**
	+ Defining Functions and inbuilt functions
	+ Returning values
	+ Principle of code reuse
	+ Code Style  

+ **Conditionals**
	+ Comparism Operators with Equations and strings
	+ Logical Operators
	+ Branching with if and else statements
	+ Else if statements
	+ Complex branching with elif statment

+ **Object-oriented Programing**
	+ Instance Methods
	+ Constructors and Other Special Methods
	+ Special Method and Operators
	+ Class and Methods

***

##	Module 3
###	Objectives:
-	Implement while loops to continuously execute code while a condition is true
-	Identify and fix infinite loops when using while loops
-	Utilize for loops to iterate over a block of code
-	Use the range() function to control for loops
-	Use nested while and for loops with if statements
-	Identify and correct common errors when using loops

###	Content
-	**While loops**
A while loop executes the body of the loop while a specified condition remains True. They are commonly [used](./03_loops/1.while_loop.py) when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration. 
	-	The syntax
	while specified condition is True:
	body of loop

- 	**For Loops**
For loops are [suited](./03_loops/2.for_Loop.py) for objects that have iterable structures. So lists, strings, ranges of integers. Individual integers are not iterable, but can be looped over by the use of the range() function. 
	-	The sytax
	for variable in sequence:
    body of loop
	
For loops and while loops share several characteristics. Both loops can be used with a variety of data types, both can be nested, and both can be used with the keywords break and continue. However, there are important differences between the two types of loops: 

**while** loops are used when a segment of code needs to execute repeatedly while a condition is true

**for loops** iterate over a sequence of elements, executing the body of the loop for each element in the sequence

-	A recursive function must include a recursive case and base case. The recursive case calls the function again, with a different value. The base case returns a value without calling the same function.
A recursive function will usually have this structure:
	-	def recursive_function(parameters):
    		if base_case_condition(parameters):
    		return base_case_value
    		recursive_function(modified_parameters)
