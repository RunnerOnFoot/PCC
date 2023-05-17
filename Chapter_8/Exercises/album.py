"""Exercise 8-7"""


def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dict = {'artist': artist.title(), 'title': title.title()}
    return album_dict


album = make_album('mehrad hidden', 'Toonel vol.1')
print(album)

album = make_album('bahram', 'Eshtebahe Khoob')
print(album)

album = make_album('metallica', 'ride the lightning')
print(album)
