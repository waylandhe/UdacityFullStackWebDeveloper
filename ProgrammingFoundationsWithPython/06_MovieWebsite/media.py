import webbrowser

class Movie():
	""" A class for storing information relevant to movies """
	valid_ratings = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_image_url, trailer_youtube_url ):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	#opens a web browser and shows relevant trailer to the movie
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

