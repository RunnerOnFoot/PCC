# You can use individual values from a list just as you would any other variable.
# For example, you can use f-strings to create a message based on a value from a list.
# Let’s try pulling the first bicycle from the list and composing a message using that value:

bicycles = ['trek', 'connondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}. "

print(message)
# We build a sentence using the value at bicycles[0] and assign it to the variable message.
# The output is a simple sentence about the first bicycle in the list.
