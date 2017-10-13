#Victor Bianchi - Software Design - Fall 2017
#Mini-Project #3
#Wikipedia trivia: if you take any article, click on the first link in the article text
#not in parentheses or italics, and then repeat, you will eventually end up at ‘Philosophy’.

import urllib
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

user_choice = ' '.join(sys.argv[1:])
if user_choice == '':
	start = input("Please enter the name of the first article (leave blank for random) : ")
	link = "http://en.wikipedia.org/wiki/" + start
else: #choose random page
	link = "http://en.wikipedia.org/wiki/Special:Random"
url = urllib.request.urlopen(link)

visited_urls = []
current = ""
goal = "Philosophy"
steps = 0
print ('\n' + start + '\n -->')
while (current != goal):
	BS  = BeautifulSoup(url, "lxml")
	link = BS.find("div", {"id":"mw-content-text"})
	path = link.find("p").find_all("a")

	for links in path:
		if (str(links.get("title")) == "None" or (str(links.get("title")) == path)):
			pass
		else:
			z = str(links.get("title"))
			if (len(z.split()) >= 2):
				name = ''
				for current in range(len(z.split())):
					name += z.split()[current]
					if (current != (len(z.split())-1)):
						name += "_"
				z = name

			next_link = "http://en.wikipedia.org/wiki/" + z

			#print next_link
			current = str(links.get("title"))
			visited_urls.append(current)
			print (current)
			steps += 1
			if (current != goal):
				print (" --> ")
			if (steps == 50 ):
				print ("This is taking too long. I quit")
				sys.exit(1)
			url = urllib.request.urlopen(next_link)
			break
print ('\nTo get from ' + start + ' to ' + goal + ', it took %i clicks.' %steps)
