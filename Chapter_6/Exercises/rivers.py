# 6-5

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n")
for river in rivers:
    print(river.title())
# OR #
# for river in rivers.keys():
#    print(river.title())

print("\n")
for country in rivers.values():
    print(country.title())
