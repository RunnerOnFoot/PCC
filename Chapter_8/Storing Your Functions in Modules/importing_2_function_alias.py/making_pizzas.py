"""Using as to Give a Function an Alias"""


from pizza import make_pizza as mp


mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# The general syntax for providing an alias is:
# from module_name import function_name as fn
