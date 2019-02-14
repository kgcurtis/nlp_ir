import pysolr

# solr = pysolr.Solr("http://ec2-3-80-214-110.compute-1.amazonaws.com:8983/solr/my_core", timeout=10)
solr = pysolr.Solr("http://localhost:8983/solr/my_core", timeout=10)
count = 0

with open("turk_data/goldStandardNoSeries.txt") as fi:
	lines = fi.readlines()
	for line in lines:
		chars_to_replace = ['[', ']', '"']
		for char in chars_to_replace:
			line = line.replace(char, "")
		query_list = line.split(",")
		user_query = query_list[0]
		turk_result = query_list[2][1:].replace("\n", "")
		solr_results = solr.search(user_query)
		for res in solr_results:
			if turk_result.lower().strip() == res['title'][0].lower().strip():
				count += 1
				break

print("Accuracy of Solr: " + str(count / len(lines)))
	

