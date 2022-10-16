from imdb import Cinemagoer
import time


# create an instance of the Cinemagoer class
ia = Cinemagoer()

names = []
searches = []
persons = []
lists = []

answer = 'y'

print("~~~~~~~~~ What was that movie again? ~~~~~~~~~")
print("Ever remember the actors and actresses who played in a movie,")
print("but can't remember what the name of the movie was?")
print("All you have to do is enter the number of actors who you know played together")
print("and their names! ~")

while answer == 'y' or answer == 'Y':

    num = int(input("How many actors played what? (enter number of actors to check): "))

    for i in range(0, num):
        names.append(input("Enter actor name: "))

    print("Please wait...")

    for actor in range(0, num):
        searches.append(ia.search_person(names[actor]))   
        while (len(searches[actor]) == 0):
            searches.pop()
            time.sleep(6)
            print("Loading...")
            searches.append(ia.search_person(names[actor]))
        persons.append(ia.get_person(searches[actor][0].personID))

        templist = []
        try:
            for i in persons[actor].data["filmography"]["actor"]:
                templist.append(i.movieID)
        except KeyError:
            try:
                for i in persons[actor].data["filmography"]["actress"]:
                    templist.append(i.movieID)
            except KeyError:
                break
            
        lists.append(templist)

    if (len(lists) == 0):
        print("No actor found!")
        break

    matches = set(lists[0])

    for i in range(1, num):
        matches = matches.intersection(lists[i])    

    if len(matches) == 0:
        print("These actors haven't played in a movie together, or the actor names were misspelled!")
    else:
        print("These actors played in:")
        for i in matches:
            movie = ia.get_movie(i)
            print(movie)

    names.clear()
    searches.clear()
    persons.clear()
    lists.clear()
    answer = input("Would you like to continue? (y/n): ")

