# if you use an apostrophe within single quotes, you’ll produce an error.
# This happens because Python interprets everything between the first single quote and the apostrophe as a string.
# It then tries to interpret the rest of the text as Python code, which causes errors.
# Here’s how to use single and double quotes correctly:
message = "One of Python's strengths is its diverse community"
print(message)
# The apostrophe appears inside a set of double quotes,
# so the Python interpreter has no trouble reading the string correctly.
