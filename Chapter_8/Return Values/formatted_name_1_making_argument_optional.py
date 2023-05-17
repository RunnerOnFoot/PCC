"""Making an Argument Optional - first version"""

# A first attempt to include middle names might look like this:


def get_formatted_name(first_name, middle_name, last_name):
    """Return a fullname, neatly formatted."""
    fullname = f"{first_name} {middle_name} {last_name}"
    return fullname.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
