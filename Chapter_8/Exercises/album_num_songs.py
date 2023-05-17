"""Exercise 8-7"""


def make_album(artist, title, num_songs=None):
    """Build a dictionary containing information about an album."""
    album_dict = {'artist': artist.title(),
                  'title': title.title()
                  }
    if num_songs:
        album_dict['num_songs'] = num_songs
    else:
        album_dict = {'artist': artist.title(), 'title': title.title()}
    return album_dict


artist_info = make_album('mehrad hidden', 'Toonel vol.1')
print(artist_info)

artist_info = make_album('bahram', 'Eshtebahe Khoob', 16)
print(artist_info)
