# Consider a URL with the common prefix https://. We want to remove this prefix,
# so we can focus on just the part of the URL that users need to enter into an address bar. Here’s how to do that:
# Enter the name of the variable followed by a dot, and then the method removeprefix(). Inside the parentheses,
# enter the prefix you want to remove from the original string.
nostarch_url = 'https://www.nostarch.com'
print(nostarch_url.removeprefix('https://'))

# Like the methods for removing whitespace, removeprefix() leaves the original string unchanged.
# If you want to keep the new value with the prefix removed,
# either reassign it to the original variable or assign it to a new variable:
nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)
