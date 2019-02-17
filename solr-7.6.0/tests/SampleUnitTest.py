import pysolr
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def inc_dict(query_dict, query_len):
	if query_dict.get(len_query) == None:
		query_dict[len_query] = 1
	else:
		query_dict[len_query] += 1

# solr = pysolr.Solr("http://ec2-3-80-214-110.compute-1.amazonaws.com:8983/solr/my_core", timeout=10)
solr = pysolr.Solr("http://localhost:8983/solr/my_core", timeout=10)
count = 0
good_query = {}
bad_query = {}
with open("turk_data/goldStandardNoSeries.txt") as fi:
	lines = fi.readlines()
	for line in lines:
		chars_to_replace = ['[', ']', '"']
		for char in chars_to_replace:
			line = line.replace(char, "")
		query_list = line.split(",")
		user_query = query_list[0]
		user_list = user_query.split(" ")
		len_query = len(user_list)
		turk_result = query_list[2][1:].replace("\n", "")
		solr_results = solr.search(user_query)
		found = False
		for res in solr_results:
			if turk_result.lower().strip() == res['title'][0].lower().strip():
				count += 1
				inc_dict(good_query,len_query)
				found = True
				break
		
		if found == False:
			inc_dict(bad_query, len_query)


classes = ['Not Found', 'Found']
class_colours = ['r','b']
recs = []
for i in range(0,len(class_colours)):
    recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))

plt.legend(recs,classes,loc=4)
plt.scatter(good_query.keys(),good_query.values(),color='blue')
plt.scatter(bad_query.keys(),bad_query.values(),color='red')
x = good_query.keys()

plt.title('Query Results vs Length of Query used')
plt.show()
print("Accuracy of Solr: " + str(count / len(lines)))
	

