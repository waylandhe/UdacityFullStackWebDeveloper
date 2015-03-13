import urllib

def readText():
	quotes = open(r"/Users/waylandhe/UdacityFullStackWebDeveloper/ProgrammingFoundationsWithPython/05_ProfanityChecker/movie_quotes.txt")
	contentsOfFile = quotes.read()
	quotes.close()
	translateToPirate(contentsOfFile)

def translateToPirate(text):
	connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text)
	output = connection.read()
	print(output)
	connection.close()

readText()
