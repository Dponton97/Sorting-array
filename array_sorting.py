import array as arr
from typing import Type, List, Union

array1 = []
print("Hello this is the organizer program, which organizes the user inputs in ascending order \nor descending order, depending on user preference")
print("\n")
size = int(input("How many numbers would you like to have in the array?"+" ")) ## determines size of the array
print("please input the integers for the array")
for i in range (0,size): ## inputs a value at the same number as the size specified by user
    arraynumb = int(input())
    array1.append(arraynumb)

userpref = int(input("Would you like the array to be in ascending order or descending order? \nenter 1 for ascending and 2 for descending"))

if userpref == 1:
        array1.sort()
        print(array1)
elif userpref == 2:
        array1.sort(reverse=True)
        print(array1)
else:
        print("Invalid input! Please try again")
