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
                    "Hey-hey-hey\n"
                    "Yeah-ah\n\n"
                    "Sheets of empty canvas, untouched sheets of clay\n"
                    "Her lace spread out before me, as her body once did\n"
                    "All five horizons revolved around her soul, as the Earth to the Sun\n"
                    "Now the air I tasted and breathed has taken a turn\n\n"
                    "Ooh-oh, and all I taught her was everything\n"
                    "Mmm, oh, I know she gave me all that she wore\n\n"
                    "And now my bitter hands chafe beneath the clouds\n"
                    "Of what was everything\n"
                    "All the pictures have all been washed in black\n"
                    "Tattooed everything\n\n"
                    "I take a walk outside, I'm surrounded by some kids at play\n"
                    "I can feel their laughter, so why do I see her?\n\n"
                    "Mmm-hmm, all the twisted thoughts that spin 'round my head\n"
                    "I'm spinnin', oh, I'm spinnin'\n"
                    "How quick the Sun can drop away\n\n"
                    "And now my bitter hands cradle broken glass\n"
                    "Of what was everything\n"
                    "All the pictures have all been washed in black\n"
                    "Tattooed everything\n\n"
                    "All the love gone bad, turned my world to black\n"
                    "Tattooed all I see, all that I am, all that I'll be, yeah\n"
                    "Uh-huh (Uh-huh, ooh)\n\n"
                    "I know someday you'll have a beautiful life, I know you'll be a star\n"
                    "In somebody else's sky, but why?\n"
                    "Why? Why can't it be? Oh, can't it be mine?\n"
                    "(Doo-doo-doo-doo, doo-doo-doo)\n"
                    "Ooh, ah, yeah\n"
                    "Ah, ooh-ooh\n\n"
                    "(Doo-doo-doo-doo, doo-doo-doo)\n"
                    "Doo-doo-doo-doo, doo-doo-doo\n"
                    "Doo-doo-doo-doo, doo-doo-doo\n"
                    "Doo-doo-doo-doo, doo-doo-doo\n"
                    "Doo-doo-doo-doo, doo-doo-doo\n"
                    "Doo-doo-doo-doo, doo-doo-doo\n"
                    "Doo-doo-doo-doo, doo-doo-doo\n"
                    "Doo-doo-doo-doo, doo-doo-doo\n"
                    "Doo-doo-doo-doo, doo-doo-doo (Oh, oh-yeah)\n"
                    "Doo-doo-doo-doo, doo-doo-doo"
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
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello\n\n"
                    "With the lights out, it's less dangerous\n"
                    "Here we are now, entertain us\n"
                    "I feel stupid and contagious\n"
                    "Here we are now, entertain us\n"
                    "A mulatto, an albino, a mosquito, my libido\n"
                    "Yeah, hey, yay\n\n"
                    "I'm worse at what I do best\n"
                    "And for this gift, I feel blessed\n"
                    "Our little group has always been\n"
                    "And always will until the end\n\n"
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello\n\n"
                    "With the lights out, it's less dangerous\n"
                    "Here we are now, entertain us\n"
                    "I feel stupid and contagious\n"
                    "Here we are now, entertain us\n"
                    "A mulatto, an albino, a mosquito, my libido\n"
                    "Yeah, hey, yay\n\n"
                    "And I forget just why I taste\n"
                    "Oh yeah, I guess it makes me smile\n"
                    "I found it hard, it's hard to find\n"
                    "Oh well, whatever, never mind\n\n"
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello, how low\n"
                    "Hello, hello, hello\n\n"
                    "With the lights out, it's less dangerous\n"
                    "Here we are now, entertain us\n"
                    "I feel stupid and contagious\n"
                    "Here we are now, entertain us\n"
                    "A mulatto, an albino, a mosquito, my libido\n"
                    "Yeah, hey, yay"
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
                    "Won't you come?\n\n"
                    "Stuttering, cold and damp\n"
                    "Steal the warm wind, tired friend\n"
                    "Times are gone for honest men\n"
                    "And sometimes far too long for snakes\n"
                    "In my shoes, walking sleep\n"
                    "In my youth, I pray to keep\n"
                    "Heaven send Hell away\n"
                    "No one sings like you anymore\n\n"
                    "Black hole sun, won't you come\n"
                    "And wash away the rain?\n"
                    "Black hole sun, won't you come\n"
                    "Won't you come?\n\n"
                    "(Black hole sun, black hole sun)\n"
                    "Won't you come?\n"
                    "(Black hole sun, black hole sun)\n"
                    "Won't you come?\n"
                    "(Black hole sun, black hole sun)\n"
                    "Won't you come?\n"
                    "(Black hole sun, black hole sun)\n\n"
                    "Hang my head, drown my fear\n"
                    "Till you all just disappear\n\n"
                    "Black hole sun, won't you come\n"
                    "And wash away the rain?\n"
                    "Black hole sun, won't you come\n"
                    "Won't you come?\n\n"
                    "Black hole sun, won't you come\n"
                    "And wash away the rain?\n"
                    "Black hole sun, won't you come\n"
                    "Won't you come?\n\n"
                    "(Black hole sun, black hole sun)\n"
                    "Won't you come?\n"
                    "(Black hole sun, black hole sun)\n"
                    "Won't you come?\n"
                    "(Black hole sun, black hole sun)\n"
                    "Won't you come?\n"
                    "(Black hole sun, black hole sun)\n"
                    "Won't you come?\n"
                    "(Black hole sun, black hole sun)\n"
                    "Won't you come?\n"
                    "Won't you come?"
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
                    "I'd feel better dead\n\n"
                    "Oooh...\n"
                    "Oooh..."
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
                    "You fritter and waste the hours in an offhand way\n"
                    "Kicking around on a piece of ground in your home town\n"
                    "Waiting for someone or something to show you the way\n\n"
                    "Tired of lying in the sunshine staying home to watch the rain\n"
                    "You are young and life is long and there is time to kill today\n"
                    "And then one day you find ten years have got behind you\n"
                    "No one told you when to run, you missed the starting gun\n\n"
                    "And you run and you run to catch up with the sun but it's sinking\n"
                    "Racing around to come up behind you again\n"
                    "The sun is the same in a relative way but you're older\n"
                    "Shorter of breath and one day closer to death\n\n"
                    "Every year is getting shorter, never seem to find the time\n"
                    "Plans that either come to naught or half a page of scribbled lines\n"
                    "Hanging on in quiet desperation is the English way\n"
                    "The time is gone, the song is over, thought I'd something more to say\n\n"
                    "Home, home again\n"
                    "I like to be here when I can\n"
                    "When I come home cold and tired\n"
                    "It's good to warm my bones beside the fire\n"
                    "Far away across the field\n"
                    "The tolling of the iron bell\n"
                    "Calls the faithful to their knees\n"
                    "To hear the softly spoken magic spells"
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
                    "Riding out the day's events\n\n"
                    "The river\n"
                    "And what you say about his company\n"
                    "Is what you say about society\n"
                    "Catch the mist, catch the myth\n"
                    "Catch the mystery, catch the drift\n\n"
                    "The world is, the world is\n"
                    "Love and life are deep\n"
                    "Maybe as his skies are wide\n\n"
                    "Today's Tom Sawyer\n"
                    "He gets high on you\n"
                    "And the space he invades\n"
                    "He gets by on you\n\n"
                    "No, his mind is not for rent\n"
                    "To any god or government\n"
                    "Always hopeful, yet discontent\n"
                    "He knows changes aren't permanent\n"
                    "But change is\n\n"
                    "And what you say about his company\n"
                    "Is what you say about society\n"
                    "Catch the witness, catch the wit\n"
                    "Catch the spirit, catch the spit\n\n"
                    "The world is, the world is\n"
                    "Love and life are deep\n"
                    "Maybe as his eyes are wide\n\n"
                    "Exit the warrior\n"
                    "Today's Tom Sawyer\n"
                    "He gets high on you\n"
                    "And the energy you trade\n"
                    "He saves..."
                )
            },
            {
                'title': 'Roundabout',
                'artist': {'id': 203, 'name': 'Yes'},
                'album': {'title': 'Fragile'},
                'genre': 'Progressive Rock',
                'lyrics': (
                    "I'll be the roundabout\n"
                    "The words will make you out and out\n"
                    "I spend the day your way\n"
                    "Call it morning driving through the sound\n"
                    "And in and out the valley\n"
                    "The music dance and sing\n"
                    "They make the children really ring\n"
                    "I spend the day your way\n"
                    "Call it morning driving through the sound\n"
                    "And in and out the valley\n"
                    "In and around the lake\n\n"
                    "Mountains come out of the sky and they stand there\n"
                    "One mile over we'll be there and we'll see you\n"
                    "Ten true summers we'll be there and laughing, too\n"
                    "24 before my love you'll see\n"
                    "I'll be there with you\n\n"
                    "I will remember you\n"
                    "Your silhouette will charge the view\n"
                    "Of distant atmosphere\n"
                    "Call it morning driving through the sound\n"
                    "And even in the valley\n"
                    "In and around the lake\n\n"
                    "Mountains come out of the sky and they stand there\n"
                    "One mile over we'll be there and we'll see you\n"
                    "Ten true summers we'll be there and laughing, too\n"
                    "24 before my love you'll see\n"
                    "I'll be there with you\n\n"
                    "Along the drifting cloud\n"
                    "The eagle searching down on the land\n"
                    "Catching the swirling wind\n"
                    "The sailor sees the rim of the land\n"
                    "The eagles dancing wings\n"
                    "Create as weather spins out of hand\n"
                    "Go closer hold the land\n"
                    "Feel partly no more than grains of sand\n"
                    "We stand to lose all time\n"
                    "A thousand answers by in our hand\n"
                    "Next to your deeper fears\n"
                    "We stand surrounded by a millions years\n\n"
                    "I'll be the roundabout\n"
                    "The words will make you out and out\n"
                    "I'll be the roundabout\n"
                    "The words will make you out and out\n"
                    "In and around the lake\n"
                    "Mountains come out of the sky and they stand there\n"
                    "24 before my love and I'll be there\n\n"
                    "I'll be the roundabout\n"
                    "The words will make you out and out\n"
                    "You spent the day your way\n"
                    "Call it morning driving through the sound\n"
                    "And in and out the valley\n"
                    "In and around the lake\n"
                    "Mountains come out of the sky and they stand there\n"
                    "One mile over we'll be there and we'll see you\n"
                    "Ten true summers we'll be there and laughing, too\n"
                    "24 before my love you'll see\n"
                    "I'll be there with you"
                )
            },
            {
                'title': 'Achilles Last Stand',
                'artist': {'id': 204, 'name': 'Led Zeppelin'},
                'album': {'title': 'Presence'},
                'genre': 'Progressive Rock',
                'lyrics': (
                    "It was an April morning when they told us we should go\n"
                    "As I turned to you, you smiled at me\n"
                    "How could we say no?\n"
                    "Oh, the fun to have, the music play, the breeze in the hair\n"
                    "To think of more that we could do, our lives to share\n\n"
                    "Days went by and hours passed, and still the road went on\n"
                    "A journey to the land of ice, the setting of the sun\n"
                    "As we carried on and on, our minds were quite at ease\n"
                    "We talked of things we'd left behind, and what we hoped to see\n\n"
                    "Oh, the fun to have, the music play, the breeze in the hair\n"
                    "To think of more that we could do, our lives to share\n"
                    "Ah, the fun to have, the music play, the breeze in the hair\n"
                    "To think of more that we could do, our lives to share\n\n"
                    "Mellow is the greeting of the ones who'd gone before\n"
                    "Their smiles were warm and friendly as they opened up the door\n"
                    "They had a place for everyone, a table and a chair\n"
                    "And the music played all through the night, and laughter filled the air\n\n"
                    "Oh, the fun to have, the music play, the breeze in the hair\n"
                    "To think of more that we could do, our lives to share\n\n"
                    "It was a time of magic, it was a time of song\n"
                    "And as the evening faded out, we knew we must go on\n"
                    "So off we went into the night, the wind was in our face\n"
                    "We left behind the magic, and we left behind the place\n\n"
                    "Oh, the fun to have, the music play, the breeze in the hair\n"
                    "To think of more that we could do, our lives to share"
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
                    "To explain in due time all I know\n"
                    "Time is a valuable thing\n"
                    "Watch it fly by as the pendulum swings\n"
                    "Watch it count down to the end of the day\n"
                    "The clock ticks life away\n"
                    "It's so unreal\n"
                    "Didn't look out below\n"
                    "Watch the time go right out the window\n"
                    "Trying to hold on, but didn't even know\n"
                    "I wasted it all just to watch you go\n\n"
                    "I kept everything inside and even though I tried, it all fell apart\n"
                    "What it meant to me will eventually be a memory of a time when\n"
                    "I tried so hard and got so far\n"
                    "But in the end, it doesn't even matter\n"
                    "I had to fall to lose it all\n"
                    "But in the end, it doesn't even matter\n\n"
                    "One thing, I don't know why\n"
                    "It doesn't even matter how hard you try\n"
                    "Keep that in mind, I designed this rhyme\n"
                    "To remind myself how I tried so hard\n"
                    "In spite of the way you were mocking me\n"
                    "Acting like I was part of your property\n"
                    "Remembering all the times you fought with me\n"
                    "I'm surprised it got so far\n"
                    "Things aren't the way they were before\n"
                    "You wouldn't even recognize me anymore\n"
                    "Not that you knew me back then\n"
                    "But it all comes back to me in the end\n\n"
                    "I kept everything inside and even though I tried, it all fell apart\n"
                    "What it meant to me will eventually be a memory of a time when\n"
                    "I tried so hard and got so far\n"
                    "But in the end, it doesn't even matter\n"
                    "I had to fall to lose it all\n"
                    "But in the end, it doesn't even matter\n\n"
                    "I've put my trust in you\n"
                    "Pushed as far as I can go\n"
                    "For all this, there's only one thing you should know\n"
                    "I've put my trust in you\n"
                    "Pushed as far as I can go\n"
                    "For all this, there's only one thing you should know\n\n"
                    "I tried so hard and got so far\n"
                    "But in the end, it doesn't even matter\n"
                    "I had to fall to lose it all\n"
                    "But in the end, it doesn't even matter"
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
                    "Something's raped and taken from me, from me\n\n"
                    "Life's gotta always be messin' with me (You wanna see the light)\n"
                    "Can't they chill and let me be free? (So do I)\n"
                    "Can't I take away all this pain? (You wanna see the light)\n"
                    "I try to every night, all in vain, in vain\n\n"
                    "Sometimes, I cannot take this place\n"
                    "Sometimes, it's my life I can't taste\n"
                    "Sometimes, I cannot feel my face\n"
                    "You'll never see me fall from grace\n\n"
                    "Something takes a part of me\n"
                    "You and I weren't meant to be\n"
                    "A cheap fuck for me to lay\n"
                    "Something takes a part of me\n\n"
                    "Feelin' like a freak on a leash (You wanna see the light)\n"
                    "Feeling like I have no release (So do I)\n"
                    "How many times have I felt diseased? (You wanna see the light)\n"
                    "Nothing in my life is free, is free\n\n"
                    "Sometimes, I cannot take this place\n"
                    "Sometimes, it's my life I can't taste\n"
                    "Sometimes, I cannot feel my face\n"
                    "You'll never see me fall from grace\n\n"
                    "Something takes a part of me\n"
                    "You and I weren't meant to be\n"
                    "A cheap fuck for me to lay\n"
                    "Something takes a part of me\n\n"
                    "Something takes a part of me\n"
                    "Something takes a part of me\n"
                    "Something takes a part of me\n"
                    "(Da boom, da-da-da-dum)\n"
                    "(Da boom, da-da-da-dum)\n"
                    "(Da boom, da-da-da-dum)\n"
                    "(Da boom, da-da-da-dum)\n"
                    "(Da boom, da-da-da-dum)\n\n"
                    "Go!\n\n"
                    "Feelin' like a freak on a leash\n"
                    "Feeling like I have no release\n"
                    "How many times have I felt diseased?\n"
                    "Nothing in my life is free, is free\n\n"
                    "Sometimes, I cannot take this place\n"
                    "Sometimes, it's my life I can't taste\n"
                    "Sometimes, I cannot feel my face\n"
                    "You'll never see me fall from grace\n\n"
                    "Something takes a part of me\n"
                    "You and I weren't meant to be\n"
                    "A cheap fuck for me to lay\n"
                    "Something takes a part of me\n\n"
                    "Something takes a part of me\n"
                    "Something takes a part of me\n"
                    "Something takes a part of me"
                )
            },
            {
                'title': 'Chop Suey!',
                'artist': {'id': 303, 'name': 'System of a Down'},
                'album': {'title': 'Toxicity'},
                'genre': 'Nu Metal',
                'lyrics': (
                    "Wake up! (wake up)\n"
                    "Grab a brush and put a little make-up\n"
                    "Hide the scars to fade away the shake-up\n"
                    "Why'd you leave the keys upon the table?\n"
                    "Here you go, create another fable\n\n"
                    "You wanted to\n"
                    "Grab a brush and put a little make-up\n"
                    "You wanted to\n"
                    "Hide the scars to fade away the shake-up\n"
                    "You wanted to\n"
                    "Why'd you leave the keys upon the table?\n"
                    "You wanted to\n\n"
                    "I don't think you trust\n"
                    "In my self-righteous suicide\n"
                    "I cry when angels deserve to die\n\n"
                    "Wake up (wake up)\n"
                    "Grab a brush and put a little make-up\n"
                    "Hide the scars to fade away (hide the scars to fade away the shake-up)\n"
                    "Why'd you leave the keys upon the table?\n"
                    "Here you go, create another fable\n"
                    "You wanted to\n"
                    "Grab a brush and put a little make-up\n"
                    "You wanted to\n"
                    "Hide the scars to fade away the shake-up\n"
                    "You wanted to\n"
                    "Why'd you leave the keys upon the table?\n"
                    "You wanted to\n\n"
                    "I don't think you trust\n"
                    "In my self-righteous suicide\n"
                    "I cry when angels deserve to die\n\n"
                    "In my self-righteous suicide\n"
                    "I cry when angels deserve to die\n\n"
                    "Father (father)\n"
                    "Father (father)\n"
                    "Father (father)\n"
                    "Father (father)\n\n"
                    "Father, into your hands, I commend my spirit\n"
                    "Father, into your hands\n"
                    "Why have you forsaken me?\n"
                    "In your eyes, forsaken me\n"
                    "In your thoughts, forsaken me\n"
                    "In your heart, forsaken me, oh\n\n"
                    "Trust in my self-righteous suicide\n"
                    "I cry when angels deserve to die\n\n"
                    "In my self-righteous suicide\n"
                    "I cry when angels deserve to die"
                )
            },
            {
                'title': 'My Own Summer',
                'artist': {'id': 304, 'name': 'Deftones'},
                'album': {'title': 'Around the Fur'},
                'genre': 'Nu Metal',
                'lyrics': (
                    "Hey you, big star\n"
                    "Tell me when it's over (Cloud)\n\n"
                    "Hey you, big mood\n"
                    "Guide me to shelter\n"
                    "'Cause I'm through\n"
                    "When the two\n"
                    "Hits the six and it's summer (Cloud)\n\n"
                    "(Come)\n"
                    "Shove it, shove it, shove it\n"
                    "(Shove)\n"
                    "Shove it, shove it, shove it\n"
                    "(The sun)\n"
                    "Shove it, shove it, shove it\n"
                    "(Aside)\n"
                    "Shove it aside\n\n"
                    "I think God is moving its tongue\n"
                    "There's no crowds in the street and no sun\n"
                    "In my own summer\n\n"
                    "The shade is a tool\n"
                    "A device, a savior\n"
                    "See, I try and look up\n"
                    "To the sky, but my eyes burn (Cloud)\n\n"
                    "(Come)\n"
                    "Shove it, shove it, shove it\n"
                    "(Shove)\n"
                    "Shove it, shove it, shove it\n"
                    "(The sun)\n"
                    "Shove it, shove it, shove it\n"
                    "(Aside)\n"
                    "Shove it aside\n\n"
                    "(Come)\n"
                    "Shove it, shove it, shove it\n"
                    "(Shove)\n"
                    "Shove it, shove it, shove it\n"
                    "(The sun)\n"
                    "Shove it, shove it, shove it\n"
                    "(Aside)\n"
                    "Shove it aside\n\n"
                    "I think God is moving its tongue\n"
                    "There's no crowd in the streets and no sun\n"
                    "In my own summer\n\n"
                    "(Come)\n"
                    "Shove it, shove it, shove it\n"
                    "(Shove)\n"
                    "Shove it, shove it, shove it\n"
                    "(The sun)\n"
                    "Shove it, shove it, shove it\n"
                    "(Aside)\n"
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