# We’ll loop through the names in the dictionary as we did previously,
# but when the name matches one of our friends,
# we’ll display a message about their favorite language:
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# "\t" is a tab!
