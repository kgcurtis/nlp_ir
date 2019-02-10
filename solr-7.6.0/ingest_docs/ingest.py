import json
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/my_core/', timeout=10)

tmdb_data = open('tmdb.json').read()
tmdb = json.loads(tmdb_data)

tmdbArr = []
name_array = []
char_array = []

for id in tmdb:
    #tmdbArr.append(tmdb[id])
    movie = tmdb[id]
    name_array = []
    char_array = []
    for item in tmdb[id]['cast']:
        name_array.append(item['name'])
        char_array.append(item['character'])
    
    movie['actors'] = name_array
    movie['characters'] = char_array[0:5]
    tmdbArr.append(movie)

solr.add(tmdbArr)
solr.commit()
