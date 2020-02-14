class Song(object):
	# Creating the initialize function
	def __init__(self, lyrics):
		#Here we set self.lyrics to lyrics so that the self (initialise variable) knows which variable to work with
		self.lyrics = lyrics


	def Sing_me_a_song(self):  # Here we work with the next function N.B we must always pass self as an arguement
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
"With pockets full of shells"])



happy_bday.Sing_me_a_song()   # two ways of using our class, the first is by using the variable as the instatiation

Song.Sing_me_a_song(bulls_on_parade) # The second is by passing the variable as an instantiation