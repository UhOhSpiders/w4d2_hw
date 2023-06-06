import pdb
from models.artist import Artist
from models.album import Album 
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository



# creates and saves artists
# artist_1 = Artist("Johnny Cash")
# artist_repository.save(artist_1)
# artist_2 = Artist("Alice Coltrane")
# artist_repository.save(artist_1)
# results = artist_repository.select_all()


# creates and saves albums
# pdb.set_trace()
artist_1 = Artist("Johnny Cash")
album_1 = Album("At Folsom Prison", "country", artist_1)
album_2 = Album("At Folsom Prison", "country", artist_1)
album_repository.save(album_1)
album_repository.save(album_2)
results = album_repository.select_all()