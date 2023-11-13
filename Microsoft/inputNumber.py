# You probably meant for this program to answer you with 7 instead of 34. 
# So what went wrong?

# The explanation is that first_number and second_number are strings. 
# For the calculation to work correctly, you need to change those strings to 
# numbers by using the int() function.

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)