class Schedule:
	
	theaters = []
	def __init__(self, movies):

		for i in range(0, len(movies)):
			self.theaters.append(Theater_Room(movies[i][0], movies[i][1]))
	
	def print_theaters(self):
		for theater in self.theaters:
			theater.print_sched()

	def r_get_theater(self, name):
		for theater in self.theaters:
			if (theater.get_name() == name):
				return theater
		return "No theater found playing movie: " + name

	def delete_time(self, name, movie_name, time):
		for i in range(0, len(self.theaters)):
			if(self.theaters[i].get_name() == movie_name):
				self.theaters[i].remove_reservation(name, time)
		return "name removed from Time: " + time + " shit"

	def get_names(self):
		ans = ""
		for theater in self.theaters:
			ans = ans + theater.get_name() + "\t"
		ans = ans + "\n"
		return ans
	def get_genres(self):
		ans = ""
		for theater in self.theaters:
			ans = ans + theater.get_genre() + "\t\t\t"
		ans = ans + "\n"
		return ans
class Theater_Room:
	'''
		Has one movie per room.

	'''
	def __init__(self, name = "", genre = "N/A"):
		self.times = {}
		self.name = name
		self.genre = genre
		for i in range(0, 24):
			self.times[i] = "Empty"

	def make_theater_movie(self, m_movie="", m_genre="Any"):
		self.make_theater_name(m_movie)
		self.make_theater_genre(m_genre)


	def make_theater_name(self, m_movie=""):
		self.name = m_movie

	def make_theater_genre(self, m_genre=""):
		self.genre = m_genre

	def fill_in_time_slot(self, name, pos):
		if(self.times[pos] == "Empty"):
			self.times[pos] = name
			return name
		else:
			return False

	def remove_reservation(self, name, time=-1):
		if(time != -1):
			if(self.times[time] == name):
				self.times[time] = "Empty"
				return
		for i in range(0, len(self.times)):
			if(self.times[i] == name):
				self.times[i] = "Empty"

	def happening_at_time(self, time):
		return self.times[time]

	def print_sched(self):
		print("Movie: " + self.get_name() +"  Genre: " + self.get_genre())
		for i in range(0, len(self.times)):
			print("Time: " + str(i) + " " + self.times[i])
		print("\n")

	def get_name(self):
		return self.name

	def get_genre(self):
		return self.genre




if __name__ == "__main__":
	t = Theater_Room("The Little Mermaid", "Family")
	t.print_sched()
	t.fill_in_time_slot("Dave", 8)
	t.fill_in_time_slot("Bob", 9)
	t.remove_reservation("Bob")
	t.print_sched()