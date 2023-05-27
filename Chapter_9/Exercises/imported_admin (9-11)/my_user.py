"""Exercise 9-11"""


from user import Admin

alex = Admin('alex', 'armstrong', 18, 'manager', 'white', 'turkey, istanbul')
alex.describe_user()

alex.privileges.show_privileges()

alex_privileges = [
    'can add post', 'can delete post', 'can ban user',
    'can un-ban user', 'can add comments', 'can edit comments',
    'can delete comments', 'can reset passwords',
    'can moderate discussions', 'can suspend accounts',
]
alex.privileges.privileges = alex_privileges

print(
    f'\nThe admin "{alex.first_name} {alex.last_name}" has these privileges:')
alex.privileges.show_privileges()
