class Schedule:
	def __init__(self):
		self.theaters = {}
		self.theaters.append(Theater_Room)




class Theater_Room:
	'''
		Has a specific movie inside each room. Can pass in when stuff is open.

	'''
	def __init__(self, lower_bound =0, upper_bound=24):
		self.movie = Movie("", "N/A")
		self.times = {}
		for i in range(0, 24):
			self.times[i] = "Closed"
		for i in range(lower_bound, upper_bound):
			self.times[i] = "Empty"

	def make_theater_movie(self, m_movie, m_genre):
		self.movie = Movie(m_movie)
		print(self.getName())

	def fill_in_time_slot(self, name, pos):
		if(self.times[pos] == "Empty"):
			self.times[pos] = name
		else:
			return False

	def remove_reservation(self, name):
		for val in self.times:
			if(val == name):
				val = "Empty"

	def print_sched(self):
		print("Movie: " + self.movie.get_name() +"  Genre: \n")
		for i in range(0, 24):
			print("Time: " + str(i) + " " + self.times[i])

class Movie:
	def __init__(self, title, genre):
		self.name = title
		self.genre = genre

	def get_name(self):
		return self.name

	def get_genre(self):
		return self.genre

t = Theater_Room(5, 23)
t.make_theater_movie
t.print_sched()