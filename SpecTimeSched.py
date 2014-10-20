from GenSched import Schedule, Theater_Room

class SpecTimeSchedule(Schedule):
	def __init__(self):
		#Doesn't need to do anything in here. Type in anything to make sure indentation doesn't messes up.
		1

	def schedule(self, name, lower_time, upper_time):
		for j  in range(lower_time, upper_time + 1):
			for i in range(0, len(self.theaters)):
				if(self.theaters[i].fill_in_time_slot(name, j) == name):
					return "Scheduled " + name + " at " + str(j) + " for movie: " + self.theaters[i].get_name() + " using SpecTimeSchedule at: " + str(j)
		return "Could not schedule " + name + " at all" + " for a movie between times: " + str(lower_time) + " and " + str(upper_time) + " using SpecTimeSchedule"

#Test cases
if __name__ == "__main__":
	s = Schedule([("The Little Mermaid", "Family"), ("Saw 3", "Horror"), ("Kung Fu Panda", "Family")])
	g = SpecTimeSchedule()
	for i in range(0, 22):
		print(g.schedule("Bobby", 10, 16))
	s.print_theaters()
