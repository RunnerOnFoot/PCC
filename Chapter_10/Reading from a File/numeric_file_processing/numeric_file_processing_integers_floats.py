"""
Numeric File Processing

This program reads numeric values from a text file and performs numerical operations on them.
It supports both integers and floats in the file. The program converts the values to integers
if possible, otherwise to floats, and then calculates the sum and average.

The file should contain one numeric value per line. Non-numeric values will be skipped.
"""

with open(r'C:\Users\parsa\VSCode\PCC\Chapter_10\Reading from a File\numeric_file_processing\numbers.txt', encoding='utf-8') as file:
    lines = file.readlines()

# Convert the values to integers and floats
numbers = []
floats = []
for line in lines:
    stripped_line = line.strip()
    try:
        value = int(stripped_line)
        numbers.append(value)
    except ValueError:
        try:
            value = float(stripped_line)
            floats.append(value)
        except ValueError:
            pass

# Perform numerical operations
sum_int = sum(numbers)
average_int = sum_int / len(numbers) if numbers else None

sum_float = sum(floats)
average_float = sum_float / len(floats) if floats else None

combined_numbers = numbers + floats
sum_combined = sum(combined_numbers)
average_combined = sum_combined / \
    len(combined_numbers) if combined_numbers else None

# Print the results
print("\nNumbers (as integers):", numbers)
print("Sum of integers:", sum_int)
print("Average of integers:", average_int)

print("\nNumbers (as floats):", floats)
print("Sum of floats:", sum_float)
print("Average of floats:", average_float)

print("\nNumbers (combined):", combined_numbers)
print("Sum of combined numbers:", sum_combined)
print("Average of combined numbers:", average_combined)
