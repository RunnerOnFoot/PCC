"""Modifying a List in a Function"""


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


designs = ['phone case', 'robot pendant', 'dodecahedron']
all_models = []

print_models(designs[:], all_models)
show_completed_models(all_models)
print(designs)

# In this case, your designs list will be empty:
# print_models(designs, all_models)
# show_completed_models(all_models)
# print(designs)

# BUT In this case, if you give a copy of your list to the function;
# You'll be able to use the original list again!
# and also the function working with a copy of the original list :D
# print_models(designs[:], all_models)
# show_completed_models(all_models)
# print(designs)
