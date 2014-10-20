from GenSched import Schedule, Theater_Room

class SpecGenreSchedule(Schedule):
	def __init__(self):
		#Doesn't need to do anything in here. Type in anything to make sure indentation doesn't messes up.
		1

	def schedule(self, name, genre):
		for i in range(0, len(self.theaters)):
			if(self.theaters[i].get_genre() == genre):
				for j  in range(0, 24):
					if(self.theaters[i].fill_in_time_slot(name, j) != False):
						return "Scheduled " + name + " at " + str(j) + " for movie: " + self.theaters[i].get_name() + " using SpecGenreSchedule of type: " + self.theaters[i].get_genre()
		return "Could not schedule " + name + " at all" + " for a movie of type: " + not_genre + " using SpecGenreSchedule"

#Test cases
if __name__ == "__main__":
	s = Schedule([("The Little Mermaid", "Family"), ("Saw 3", "Horror"), ("Kung Fu Panda", "Family")])
	g = SpecGenreSchedule()
	for i in range(0, 25):
		print(g.schedule("Bobby", "Family"))
	print(g.schedule("Davey", "Family"))
	print(g.schedule("Davey", "Family"))
	print(g.schedule("Davey", "Horror"))
	s.print_theaters()
