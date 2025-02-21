from datetime import date  # Importing the 'date' class from the 'datetime' module.

# Getting the current date using 'date.today()' method.
date.today()  

# Printing the current date to the console.
print(date.today())  
# Example output: 2025-02-17 (format is YYYY-MM-DD)

# Concatenating and printing a message along with the current date.
print("Today's date is: " + str(date.today()))  
# Example output: Today's date is: 2025-02-17

# Assigning the value 11 to the variable 'parsecs' (representing distance in parsecs).
parsecs = 11  

# Converting parsecs to lightyears (1 parsec = 3.26 lightyears).
lightyears = parsecs * 3.26  

# Printing the conversion result using string concatenation.
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")  
# Output: 11 parsecs is 35.86 lightyears
