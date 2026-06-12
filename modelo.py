class DiscoveryModel:
    def __init__(self):

        #base de datos local mínima de 3 canciones - para testear antes de incorporar apis
        self.local_songs = [
            # --- GRUNGE ---
            {
                'title': 'Black',
                'artist': {'id': 101, 'name': 'Pearl Jam'},
                'album': {'title': 'Ten'},
                'genre': 'Grunge',
                'lyrics': (
                    "Sheets of empty canvas, untouched sheets of clay\n"
                    "Laid spread out before me as her body once did\n"
                    "All five horizons revolved around her soul\n"
                    "As the earth to the sun\n"
                    "Now the air I tasted and breathed has taken a turn\n"
                    "And all I taught her was everything\n"
                    "Ooh, I know she gave me all that she wore\n"
                    "And now my bitter hands chafe beneath the clouds\n"
                    "Of what was everything?\n"
                    "Oh, the pictures have all been washed in black, tattooed everything..."
                )
            },
            {
                'title': 'Smells Like Teen Spirit',
                'artist': {'id': 102, 'name': 'Nirvana'},
                'album': {'title': 'Nevermind'},
                'genre': 'Grunge',
                'lyrics': (
                    "Load up on guns, bring your friends\n"
                    "It's fun to lose and to pretend\n"
                    "She's over-bored and self-assured\n"
                    "Oh no, I know a dirty word\n\n"
                    "Hello, hello, hello, how low?\n"
                    "Hello, hello, hello, how low?\n"
                    "Hello, hello, hello, how low?\n"
                    "Hello, hello, hello\n\n"
                    "With the lights out, it's less dangerous\n"
                    "Here we are now, entertain us\n"
                    "I feel stupid and contagious\n"
                    "Here we are now, entertain us\n"
                    "A mulatto, an albino, a mosquito, my libido\n"
                    "Yeah, hey..."
                )
            },
            {
                'title': 'Black Hole Sun',
                'artist': {'id': 103, 'name': 'Soundgarden'},
                'album': {'title': 'Superunknown'},
                'genre': 'Grunge',
                'lyrics': (
                    "In my eyes, indisposed\n"
                    "In disguises no one knows\n"
                    "Hides the face, lies the snake\n"
                    "In the sun in my disgrace\n"
                    "Boiling heat, summer stench\n"
                    "'Neath the black the sky looks dead\n"
                    "Call my name through the cream\n"
                    "And I'll hear you scream again\n\n"
                    "Black hole sun, won't you come\n"
                    "And wash away the rain?\n"
                    "Black hole sun, won't you come\n"
                    "Won't you come?..."
                )
            },
            {
                'title': 'Nutshell',
                'artist': {'id': 104, 'name': 'Alice in Chains'},
                'album': {'title': 'Jar of Flies'},
                'genre': 'Grunge',
                'lyrics': (
                    "We chase misprinted lies\n"
                    "We face the path of time\n"
                    "And yet I fight, and yet I fight\n"
                    "This battle all alone\n"
                    "No one to cry to\n"
                    "No place to call home\n\n"
                    "Oooh...\n"
                    "Oooh...\n\n"
                    "My gift of self is raped\n"
                    "My privacy is raked\n"
                    "And yet I find, and yet I find\n"
                    "Repeating in my head\n"
                    "If I can't be my own\n"
                    "I'd feel better dead"
                )
            },
            # --- PROGRESSIVE ROCK ---
            {
                'title': 'Time',
                'artist': {'id': 201, 'name': 'Pink Floyd'},
                'album': {'title': 'The Dark Side of the Moon'},
                'genre': 'Progressive Rock',
                'lyrics': (
                    "Ticking away the moments that make up a dull day\n"
                    "Fritter and waste the hours in an offhand way\n"
                    "Kicking around on a piece of ground in your hometown\n"
                    "Waiting for someone or something to show you the way\n\n"
                    "Tired of lying in the sunshine, staying home to watch the rain\n"
                    "You are young and life is long, and there is time to kill today\n"
                    "And then one day you find ten years have got behind you\n"
                    "No one told you when to run, you missed the starting gun..."
                )
            },
            {
                'title': 'Tom Sawyer',
                'artist': {'id': 202, 'name': 'Rush'},
                'album': {'title': 'Moving Pictures'},
                'genre': 'Progressive Rock',
                'lyrics': (
                    "A modern-day warrior\n"
                    "Mean, mean stride\n"
                    "Today's Tom Sawyer\n"
                    "Mean, mean pride\n\n"
                    "Though his mind is not for rent\n"
                    "Don't put him down as arrogant\n"
                    "His reserve, a quiet defense\n"
                    "Riding out the day's events\n"
                    "The river..."
                )
            },
            {
                'title': 'Roundabout',
                'artist': {'id': 203, 'name': 'Yes'},
                'album': {'title': 'Fragile'},
                'genre': 'Progressive Rock',
                'lyrics': (
                    "I'll be the roundabout\n"
                    "The words will make you out 'n' out\n"
                    "I spend the day your way\n"
                    "Call it morning driving through the sound and\n"
                    "In and out the valley\n\n"
                    "In and around the lake\n"
                    "Mountains come out of the sky and they stand there\n"
                    "One mile over we'll be there and clean out of sight\n"
                    "In and around the lake\n"
                    "Mountains come out of the sky and they stand there..."
                )
            },
            {
                'title': 'Achilles Last Stand',
                'artist': {'id': 204, 'name': 'Led Zeppelin'},
                'album': {'title': 'Presence'},
                'genre': 'Progressive Rock',
                'lyrics': (
                    "It was an April morning when they told us we should go\n"
                    "And as I turned to you, you smiled at me\n"
                    "How could we say no?\n\n"
                    "Oh, the fun to have, the music play, the breeze in the hair\n"
                    "To think of more that we could do, our lives to share\n\n"
                    "Days went by and hours passed, and still the road went on\n"
                    "A journey to the land of ice, the setting of the sun"
                )
            },
            # --- NU METAL ---
            {
                'title': 'In the End',
                'artist': {'id': 301, 'name': 'Linkin Park'},
                'album': {'title': 'Hybrid Theory'},
                'genre': 'Nu Metal',
                'lyrics': (
                    "It starts with one thing, I don't know why\n"
                    "It doesn't even matter how hard you try\n"
                    "Keep that in mind, I designed this rhyme\n"
                    "To explain in due time\n"
                    "All I know\n"
                    "Time is a valuable thing\n"
                    "Watch it fly by as the pendulum swings\n"
                    "Watch it count down to the end of the day\n"
                    "The clock ticks life away\n"
                    "It's so unreal..."
                )
            },
            {
                'title': 'Freak on a Leash',
                'artist': {'id': 302, 'name': 'Korn'},
                'album': {'title': 'Follow the Leader'},
                'genre': 'Nu Metal',
                'lyrics': (
                    "Something takes a part of me\n"
                    "Something lost and never seen\n"
                    "Every time I start to believe\n"
                    "Something's raped and taken from me...\n\n"
                    "Feeling like a freak on a leash\n"
                    "Feeling like I have no release\n"
                    "How many times have I felt disease?\n"
                    "Nothing seems to be key..."
                )
            },
            {
                'title': 'Chop Suey!',
                'artist': {'id': 303, 'name': 'System of a Down'},
                'album': {'title': 'Toxicity'},
                'genre': 'Nu Metal',
                'lyrics': (
                    "Wake up! (Wake up!)\n"
                    "Grab a brush and put a little makeup!\n"
                    "Hide the scars to fade away the shakeup!\n"
                    "(Hide the scars to fade away the...)\n"
                    "Why'd you leave the keys upon the table?\n"
                    "Here you go create another fable!\n\n"
                    "You wanted to!\n"
                    "Grab a brush and put a little makeup!\n"
                    "You wanted to!\n"
                    "Hide the scars to fade away the shakeup!\n"
                    "You wanted to!\n"
                    "Why'd you leave the keys upon the table?\n"
                    "You wanted to!..."
                )
            },
            {
                'title': 'My Own Summer',
                'artist': {'id': 304, 'name': 'Deftones'},
                'album': {'title': 'Around the Fur'},
                'genre': 'Nu Metal',
                'lyrics': (
                    "Hey you, big star, tell me when it's over\n"
                    "Hey you, big star, tell me when it's over\n"
                    "Cloud, come shove it, shove it, shove it\n"
                    "Shove it aside\n\n"
                    "I think God is moving the tongue\n"
                    "There are no crowds in the street\n"
                    "And no sun in my own summer\n\n"
                    "Shove it, shove it, shove it\n"
                    "Shove it aside"
                )
            }
        ]

    #busca coincidencias en la base de datos local (insensible a mayúsculas). Luego devuelve una lista de canciones que coincidan en el título, artista o álbum
    
    def buscar_cancion(self, query):
        query_clean = query.strip().lower()
        if not query_clean:
            return []
            
        tokens = query_clean.split()
        if not tokens:
            return []
            
        resultados = []
        for song in self.local_songs:
            match_all = True
            for token in tokens:
                token_match = (
                    token in song['title'].lower() or
                    token in song['artist']['name'].lower() or
                    token in song['album']['title'].lower() or
                    token in song['genre'].lower()
                )
                if not token_match:
                    match_all = False
                    break
            if match_all:
                resultados.append(song) #el buen append nunca falla
        return resultados

    def obtener_recomendaciones(self, artist_id):
        target_song = None
        for song in self.local_songs:
            if song['artist']['id'] == artist_id:
                target_song = song
                break
                
        if not target_song:
            return []
            
        genre = target_song['genre']
        title = target_song['title']
        
        recs = [s for s in self.local_songs if s['genre'].lower() == genre.lower() and s['title'].lower() != title.lower()]
        
        if len(recs) < 3:
            for s in self.local_songs:
                if s not in recs and s['title'].lower() != title.lower():
                    recs.append(s)
                if len(recs) == 3:
                    break
        return recs[:3]

    def obtener_letras(self, artist, title):
        for song in self.local_songs:
            if song['title'].lower() == title.lower():
                return song['lyrics']
        return "Letra no encontrada en la base de datos local."