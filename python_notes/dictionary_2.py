countries = {
    "England":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome",
}

countries.setdefault("Ethiopia","Addis Ababa") #amharic
countries.setdefault("Peru","Lima")

# print(countries) # a way of printing a whole dictionary

# for i in countries.items():
#     print(i)

# print(list(countries))

for k, v in countries.items():
    print(k + " : " + v)

for x in countries.keys():
    print(x + " : " + countries[x])

countries.update({"England":"English",
    "France":"French",
    "Germany":"German",
    "Spain":"Spanish",
    "Italy":"Italian",
    "Ethiopia":"Amharic",
    "Peru":"Spanish"
})

print(countries)

fav_songs = [{
    "Artist":"My Chemical Romance",
    "Song Name":"Sleep",
    "Genre":"Pop Punk",
    "Release Year":"2006"
},
{
    "Artist":"Killing Joke",
    "Song Name":"The Raven King",
    "Genre":"Post-Punk",
    "Release Year":"2010"
},
{
    "Artist":"Radiohead",
    "Song Name":"15 Step",
    "Genre":"Art Rock",
    "Release Year":"2007"
}]

print(fav_songs[1])

fav_songs.append(    {
    "Artist":"Bahaus",
    "Song Name":"She's in Parties",
    "Genre":"Goth",
    "Release Year":"Dunno"
})

print(fav_songs)

# del (fav_songs[1])
# fav_songs.pop(2)

print(fav_songs)

fav_songs[2].update({"Song Name":"Jigsaw Falling Into Place"})

print(fav_songs)