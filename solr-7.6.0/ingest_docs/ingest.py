import json
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/my_collection/', timeout=10)

tmdb_data = open('tmdb.json').read()
tmdb = json.loads(tmdb_data)

tmdbArr = []
for id in tmdb:
    tmdbArr.append(tmdb[id])

solr.add(tmdbArr)
solr.commit()
