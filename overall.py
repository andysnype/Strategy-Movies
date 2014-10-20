#all the imports

from GenSched import Schedule, Theater_Room
from RegularSchedule import RegularSchedule
from DontWantSched import DontWantSchedule
from SpecGenreSched import SpecGenreSchedule
from SpecTimeSched import SpecTimeSchedule


#Make initial database
s = Schedule([("The Little Mermaid", "Family"), ("Saw 3", "Horror"), ("The Hangover", "Comedy"), ("Requiem For A Dream", "Drama"), ("2001: A Space Odyssey", "Sci-Fi"), ("Forgetting Sarah Marshall", "Romantic Comedy")])

print("Welcome to Sturman Studios!")

while(1):
	genre = ""
	response = ""
	num1 = 0
	num2 = 0
	moviename = ""
	#print("Movies: " + s.get_names() + "Genres: " + s.get_genres())
	print("Movies: " + s.get_names() + "Genres: Family\t\t\tHorror\tComedy\t\tDrama\t\t\tSci-Fi\t\t\tRomantic Comedy")
	while(response.upper() != "A" and response.upper() != "B" and response.upper() != "C" and response.upper() != "D"):
		response = input("What would you like to do? \n A: Watch a specific movie at a specific time\n B: Watch a specific Genre\n C: Avoid a Specific Genre\n D: Watch anything within a specific time range\n\n Enter the appropriate letter: ")
	person_name = input("Enter your name: ")
	while((response.upper() == "B" or response.upper() == "C") and (genre.lower() != "horror" and genre.lower() != "family" and genre.lower() != "comedy" and genre.lower() != "drama" and genre.lower() != "romantic comedy" and genre.lower() != "sci-fi")):
		genre = input("Please enter a genre: Horror, Family, Comedy, Drama, Romantic Comedy, Sci-Fi: ")
	
	if(response.upper() == "A"):
		moviename = input("Enter what movie you're looking for: ")
		try:
			num1 = int(input("Enter what time you're looking for (military hours): "))
		except ValueError:
			print("bad input. Try again.")
		s = RegularSchedule()
		print(s.schedule(person_name, num1, moviename))

	elif(response.upper() == "B"):
		s = SpecGenreSchedule()
		print(s.schedule(person_name, genre))

	elif(response.upper() == "C"):
		s = DontWantSchedule()
		print(s.schedule(person_name, genre))

	elif(response.upper() == "D"):
		#while(num1 <= num2 or num2 <0 or num1 < 0):
		try:
			num1 = int(input("Enter the beginning time in your range that you're looking for (military hours): "))
		except ValueError:
			print("bad input. Try again.")
		try:
			num2 = int(input("Enter the ending time in your range that you're looking for (military hours): "))
		except ValueError:
			print("bad input. Try again.")
		s = SpecTimeSchedule()
		print(s.schedule(person_name, num1, num2))


	if(input("Do you want to print the schedules out so far? Type Y for yes, anything else if you don't: ").lower() == 'y'):
		s.print_theaters()

	response = input("Do you want to quit? Type Q if you do, anything else if you don't: ")
	if(response == "Q" or response == "q"):
		print("K pce.\n")
		exit(0)
	print("\n")