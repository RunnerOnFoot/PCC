"""
This program reads numeric values from a file, 
converts them to floats,
and performs basic numerical operations on the data.

The program assumes that the file 'numbers.txt' exists and contains one numeric value per line.

The converted values are stored in list ('floats') and used to calculate the 
average of floats ('average_float').

The final results are printed to the console.
"""

# Read the file
with open(r'C:\\Users\\parsa\\VSCode\\PCC\\Chapter_10\\Reading from a File\\numeric_file_processing\\numbers.txt', encoding='utf-8') as file:
    lines = file.readlines()

# Convert the values to floats
floats = [float(line.strip()) for line in lines]

# Perform numerical operations
sum_float = sum(floats)
average_float = sum_float / len(floats)

# Print the results
print("Numbers (as floats):", floats)
print("Sum of numbers:", sum_float)
print("Average of numbers:", average_float)
