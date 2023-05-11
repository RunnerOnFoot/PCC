# 7-8
sandwich_orders = ['Limburger', 'Lobster roll', 'Luther', 'Bacon',
                   'tuna', 'veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich.title()} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nI made these sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
