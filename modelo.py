class DiscoveryModel:
    def __init__(self):

        #base de datos local mínima de 3 canciones - para testear antes de incorporar apis
        self.local_songs = [
            {
                'title': 'Black',
                'artist': {'id': 101, 'name': 'Pearl Jam'},
                'album': {'title': 'Ten'},
                'genre': 'Grunge',
                'lyrics': "Sheets of empty canvas, untouched sheets of clay..."
            },
            {
                'title': 'Time',
                'artist': {'id': 201, 'name': 'Pink Floyd'},
                'album': {'title': 'The Dark Side of the Moon'},
                'genre': 'Progressive Rock',
                'lyrics': "Ticking away the moments that make up a dull day..."
            },
            {
                'title': 'In the End',
                'artist': {'id': 301, 'name': 'Linkin Park'},
                'album': {'title': 'Hybrid Theory'},
                'genre': 'Nu Metal',
                'lyrics': "It starts with one thing, I don't know why..."
            }
        ]

    #busca coincidencias en la base de datos local (insensible a mayúsculas). Luego devuelve una lista de canciones que coincidan en el título, artista o álbum.
    def buscar_cancion(self, query):
        query_clean = query.strip().lower()
        if not query_clean:
            return []
            
        resultados = []
        for song in self.local_songs:
            if (query_clean in song['title'].lower() or
                query_clean in song['artist']['name'].lower() or
                query_clean in song['album']['title'].lower()):
                resultados.append(song) #el buen append nunca falla
        return resultados