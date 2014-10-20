from GenSched import Schedule, Theater_Room

class DontWantSchedule(Schedule):
	def __init__(self):
		#Doesn't need to do anything in here. Type in anything to make sure nothing messes up.
		1

	def schedule(self, name, not_genre):
		for i in range(0, len(self.theaters)):
			if(self.theaters[i].get_genre() != not_genre):
				for j  in range(0, 24):
					if(self.theaters[i].fill_in_time_slot(name, j) != False):
						return "Scheduled " + name + " at " + str(j) + " for movie: " + self.theaters[i].get_name() + " using DontWantSchedule of type: " + self.theaters[i].get_genre()
		return "Could not schedule " + name + " at all" + " for a movie not of type: " + not_genre + " using DontWantSchedule"

#Test cases
if __name__ == "__main__":
	s = Schedule([("The Little Mermaid", "Family"), ("Saw 3", "Horror")])
	d = DontWantSchedule()
	for i in range(0, 25):
		print(d.schedule("Bobby", "Family"))
	print(d.schedule("Davey", "Family"))
	print(d.schedule("Davey", "Family"))
	print(d.schedule("Davey", "Horror"))
	s.print_theaters()
