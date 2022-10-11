# -*- coding: utf-8 -*-
"""Assignment_2_Oct_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DG_Wf8OfTK9RMZhSS3gIkSW6MuTsaBsk

###1. What is indentation error? Why indentation is important? Give one simple example?

Indentation is nothing but blank spaces at the beginning of line of code.
Indentation error occurs when a particular group of code is not together or is outside the group due to incorrect spaces at the beginning of code line. Each group of code has to be segregated.  
In python indentaion is used to show or indicate a particular block of code and according to it python executes a block of code.
Therefore indentation is very important in Python. Also unlike other programming languages we do not use curly braces at start and end of block of code here. Therefore indentation becomes important in python.
"""

# Examples of indentaion error

car = False
bike = False

if car or bike:
print("I can travel") # Here we have to add space at the beginning
else:
  print("I cannot travel")

"""###2. Correct the following code and write the comment where you made the correction?"""

class_started = bool(int(input("Hey friend, is class started?: [0-False/1-True]")))
# We are accepting input from the user in form of string but in numeric form
# therefore we have to convert it to int and then to bool
if class_started:
    print("Since class started...")
    print("Lets concentrate")
else:
    print("Since class is not started...")
    print("let's revise")

"""###3. Use if else condition to verify that dataype of `input()` method in python is always string."""

a = input("Enter a Number:- ")
if type(a) == int or type(a) == bool or type(a) == float:
  print("data type of input is not string")
else:
  print("data type of input is always string")

"""###4. Take 3 variables and assign integer values to them. Find the largest variable, by only using the if and else conditions."""

num1 = int(input("Enter first Number:- "))
num2 = int(input("Enter second Number:- "))
num3 = int(input("Enter third Number:- "))

if num1 > num2 > num3 or num1 > num3 > num2:
  print(f"num1 is largest number which is {num1}")
if num2 > num3 > num1 or num2 > num1 > num3:
  print(f"num2 is largest number which is {num2}")
if num3 > num2 > num1 or num3 > num1 > num2:
  print(f"num3 is largest number which is {num3}")

"""###5. What would be the solution?
    1. True
    2. False

    ```python
    a = 6
    b = 10
    print( not ( not a == 10 or not b == 10) )
    ```
"""

a = 6
b = 10
print( not ( not a == 10 or not b == 10) )
# The solution would be false

"""###6. Find the answer as well as find out the reason behind the result? -
    - case 1:
        ```python
        A = 5.0
        B = 10/2
        print(A is B)
        ```
    - case 2:
        ```python
        A = 5.0
        B = int(10/2)
        print(A is B)
        ```
    - case 3:
        ```python
        A = 5.0
        B = float(10/2)
        print(A is B)
        ```
"""

#case 1
A = 5.0
B = 10/2
print(A is B)
print(id(A))
print(id(B))
# The result is false 
# because they are stored at different memory locations and have different identities

#case 2
A = 5.0
B = int(10/2)
print(A is B)
print(id(A))
print(id(B))
# The result is false 
# because they are stored at different memory locations and have different identities
# floats and integers are different objects in Python.

#case 3
A = 5.0
B = float(10/2)
print(A is B)
print(id(A))
print(id(B))
# The result is false 
# because they are stored at different memory locations and have different identities

"""###7. Write a program that asks the user to enter a number. You should print out a message to the user, either “That number is divisible by either 3 or 5”, or “That number is not divisible by either 3 or 5”. Be sure to consider the data type of the input you are taking in from the user. Use a single if/else block to solve this problem."""

num = float(input("Enter a number:- "))

if num % 5 == 0 or num % 3 == 0:
   print(f"The entered number {num} is divisible by 3 or 5")
   
else:
  print(f"The entered number {num} is not divisible by 3 or 5")

"""###8. Take user input for length and width. Then calculate the area of rectangle. Also print as per length and width whether its a square of rectangle."""

length = float(input("Enter length in cm:- "))
width = float(input("Enter width in cm:- "))

area = length * width
print(f"The area of shape is {area} cm2")

if length == width:
  print("The shape is square")
else:
  print("The shape is rectangle")

"""###9. Take two variable radius_1 and radius_2 and calculate the area of circle_1 and circle_2. Also print which circle has large area. If area is equal then print area is equal."""

radius_1 = float(input("Enter radius of Circle_1:- "))
radius_2 = float(input("Enter radius of Circle_2:- "))

circle_1_area = 3.14*(radius_1**2)
circle_2_area = 3.14*(radius_2**2)

print(f"Area of Circle_1 is:- {circle_1_area}")
print(f"Area of Circle_2 is:- {circle_2_area}")

if circle_1_area > circle_2_area:
  print("Circle_1 has larger area")
elif circle_2_area > circle_1_area:
  print("Circle_2 has larger area")
else:
  print("Circle_1 and Circle_2 have equal area")

"""###10. Check whether a year is leap year or not. Use nested if...else to solve this problem. A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400."""

year = int(input("Enter year:- "))

if year % 100 == 0 and year % 400 == 0:
  print("The year is a leap year")
elif year % 4 == 0 and year %100 != 0:
  print("The year is a leap year")
else:
  print("The year is not a leap year")