# 7-9
sandwich_orders = ['pastrami', 'Limburger', 'Lobster roll', 'pastrami',
                   'Luther', 'Bacon', 'pastrami', 'tuna', 'veggie',
                   'grilled cheese', 'turkey', 'pastrami', 'roast beef']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami!")


while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich.title()} sandwich.")
