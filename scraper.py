import requests
from bs4 import BeautifulSoup
import time
import json
#import this package if you have encoding errors
# import sys
# sys.setdefaultencoding('utf8')

### extract the HTML into text

r = requests.get('https://www.imdb.com/title/tt0071853/')
print(r)
r_unparsed = r.text
#print(r_unparsed)
start = time.time()
b = BeautifulSoup(r_unparsed,'lxml')
end = time.time()
print(end-start)

title = b.title.text
# print(title)
print(b.find('h1').text)
# ### now make some Soup using Beautiful Soup and XML parser
description = b.find('div','summary_text').text.strip()
print(description)

#print b

# ### extract the title and save it into a variable
##### you can use some specific methods of Beautiful Soup or follow the tree
#### print b.find('h1').text


#print(title)

# ### if there was more than 1 title it would have to be


#print(title)

# ### extract the description and save it into a variable

#print(desc)

# ### extract the Rating eg: R and save into a variable




## extract the actors
#actors = json.loads(b.find('script', type='application/ld+json').text)['actor']




# ## create a function that extracts this information of any IMDB movie of your choosing
# ## ^ into the form of a dictionary

#def movie_info(id):
	### FILL IN YOUR FUNCTION with what you learned above
#	return movie_dict

#Adrift = movie_info('tt6306064')
#pprint(Adrift)