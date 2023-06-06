import pdb
from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repository as artist_repository

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row["artist"])
        album = Album(row["title"],row["genre"], artist)
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist =  artist_repository.select(result["artist"])
        album = Album(
            result['title'],
            result['genre'],
            artist
        )
    return album 
    
# def save(album):
#     sql = "INSERT INTO albums (album_name, album_genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
#     artist =  artist_repository.select(result["artist_id"])
#     values = [album.album_name, album.album_genre, artist]
#     result = run_sql(sql, values)
#     id = result[0]["id"]
#     album.id = id
#     return album


def save(album):
    # pdb.set_trace()
    sql = 'INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *'
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

