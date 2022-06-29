countries = {
    "England":"London",
    "France":"Paris",
    "Germany":"Berlin",
    "Spain":"Madrid",
    "Italy":"Rome",
}

countries.setdefault("Ethiopia","Addis Ababa") #amharic
countries.setdefault("Peru","Lima")
print(countries)

# for x, y in countries.items():
#     print(x,y)

# for x in countries.keys():
#     print(x + " : " + countries[x])
    
countries["England"]="English"
countries.update({"France":"French"})

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

fav_songs.append(
    {
    "Artist":"Bahaus",
    "Song Name":"She's in Parties",
    "Genre":"Goth",
    "Release Year":"Dunno"
}
)

print(fav_songs)

fav_songs.pop()

print(fav_songs)

fav_songs[2].update({"Song Name":"Jigsaw"})

print(fav_songs)

for dictionary in fav_songs:
    for k,v in dictionary.items():
        print(k + " : " + v)
    print("------")