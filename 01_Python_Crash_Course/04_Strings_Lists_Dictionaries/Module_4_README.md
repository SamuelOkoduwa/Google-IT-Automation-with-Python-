<h1 style:text-align="center"> Module 4: Strings, Lists and Dictionaries </h1>
This module is to dive into more advanced ways to manipulate strings using indexing, slicing, and advanced formatting. You'll also explore the more advanced data types: lists, tuples, and dictionaries. You'll learn to store, reference, and manipulate data in these structures, as well as combine them to store complex data structures.

**Learning Objectives**
- Manipulate strings using indexing, slicing, and formatting
- Use lists and tuples to store, reference, and manipulate data
- Leverage dictionaries to store more complex data, reference - data by keys, and manipulate data stored
- Combine the String, List, and Dictionary data types to construct complex data structures

[**String Method**](./1.strings.py)
	A method is a function of a class or an object
[**String Formatting**](./1.strings.py)
You can use the format method on strings to concatenate and format strings in all kinds of powerful ways. To do this, create a string containing curly brackets, {}, as a placeholder, to be replaced. Then call the format method on the string using .format() and pass variables as parameters. The variables passed to the method will then be used to replace the curly bracket placeholders. This method automatically handles any conversion between data types for us. 

If the curly brackets are empty, they’ll be populated with the variables passed in the order in which they're passed. However, you can put certain expressions inside the curly brackets to do even more powerful string formatting operations. You can put the name of a variable into the curly brackets, then use the names in the parameters. This allows for more easily readable code, and for more flexibility with the order of variables.

You can also put a formatting expression inside the curly brackets, which lets you alter the way the string is formatted. For example, the formatting expression {:.2f} means that you’d format this as a float number, with two digits after the decimal dot. The colon acts as a separator from the field name, if you had specified one. You can also specify text alignment using the greater than operator: >. For example, the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places. String formatting can be very handy for outputting easy-to-read textual output.

[**List Defined**](./2.lists_tuple.py)
Lists in Python are defined using square brackets, with the elements stored in the list separated by commas: list = ["This", "is", "a", "list"]. You can use the len() function to return the number of elements in a list: len(list) would return 4. You can also use the in keyword to check if a list contains a certain element. If the element is present, it will return a True boolean. If the element is not found in the list, it will return False. For example, "This" in list would return True in our example. Similar to strings, lists can also use indexing to access specific elements in a list based on their position. You can access the first element in a list by doing list[0], which would allow you to access the string "This".

In Python, lists and strings are quite similar. They’re both examples of sequences of data. Sequences have similar properties, like (1) being able to iterate over them using for loops; (2) support indexing; (3) using the len function to find the length of the sequence; (4) using the plus operator + in order to concatenate; and (5) using the in keyword to check if the sequence contains a value.

[**Tuple**](./2.lists_tuple.py)
Strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable. Lists are sequences of elements of any data type, and are mutable. The third sequence type is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. They’re specified using parentheses instead of square brackets.

Tuples can be useful when we need to ensure that an element is in a certain position and will not change. Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.

**Iterating Over Lists using enumerate**
When we covered for loops, we showed the example of iterating over a list. This lets you iterate over each element in the list, exposing the element to the for loop as a variable. But what if you want to access the elements in a list, along with the index of the element in question? You can do this using the enumerate() function. The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.

[**List Comprehension**](./2.lists_tuple.py)
A list comprehension allows you to create a new list from an iterable in a single line. This line achieves the same result as the previous for loop, but in a more concise way.
You can also use conditionals with list comprehensions to build even more complex and powerful statements. You can do this by appending an if statement to the end of the list comprehension. For example, [ x for x in range(1,101) if x % 10 == 0 ] generates a new list containing all the integers divisible by 10 from 1 to 100. The if statement evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, the number is added to a new list.