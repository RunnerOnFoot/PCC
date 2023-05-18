"""Exercise 8-8"""


def make_album(artist, title, num_songs=0):
    """Build a dictionary containing information about an album."""
    album_dict = {'artist': artist.title(),
                  'title': title.title()
                  }
    if num_songs:
        album_dict['num_songs'] = num_songs
    return album_dict


# Prepare the prompts.
TITLE_PROMPT = "\nWhat album are you thinking of? "
ARTIST_PROMPT = "Who's the artist? "
NUM_PROMPT = "How many song are in the album? "

# Let the user know how to quit.
print("enter 'quit' at any time to stop.")


while True:
    title_name = input(TITLE_PROMPT)
    if title_name == 'quit':
        break

    artist_name = input(ARTIST_PROMPT)
    if artist_name == 'quit':
        break

    number_of_songs = int(input(NUM_PROMPT))
    if number_of_songs == 0:
        make_album(artist_name, title_name, num_songs=0)
    elif number_of_songs == 'quit':
        break

    print("\n")
    album = make_album(artist_name, title_name, number_of_songs)
    print(album)
