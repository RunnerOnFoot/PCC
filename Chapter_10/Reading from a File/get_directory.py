"""
How to get a "directory" and "filename" from the file I am using?
This is the way :D
"""

import os

# Get the directory of the current Python script or notebook
current_directory = os.path.dirname(os.path.abspath(__file__))

# Get the file name
file_name = os.path.basename(__file__)

print("Directory:", current_directory)
print("File Name:", file_name)
