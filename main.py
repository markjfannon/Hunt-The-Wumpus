from random import randint

#sets up room network data structure. Arranged "Room, left, right, centre"
rooms = ["1,2,8,5", "2,10,1,3", "10,11,2,9", "11,8,10,20", "8,1,11,7", "7,6,17,8", "6,5,7,15", "5,4,6,1", "4,3,5,14", "3,12,4,2", "12,9,3,13", "9,19,12,10", "19,20,9,18", "20,17,19,11", "17,7,20,16", "16,15,18,17", "15,14,16,6", "14,13,15,4", "13,18,14,12", "18,16,13,19"]

#defines where wumpus, pit and bats are at the start of the game
wumpusRoom = randint(1,20)
pitRoom = randint(1,20)
if pitRoom == wumpusRoom:
  pitRoom = randint(1,20)
batRoom = randint(1,20)
wumpusDead = False
userDead = False

#takes in the random number, returning the room number and the adjacent rooms. Alerts user if near bats, etc.
def room(roomdata):
  roomNo = roomdata.split(",")
  print("You are in room " + roomNo[0])
  print("Room number " + str(roomNo[1]) + " is to your left")
  print("Room number " + str(roomNo[2]) + " is to your right")
  print("Room number " + str(roomNo[3]) + " is in front of you")
  for item in roomNo:
    if item == str(wumpusRoom):
      print("You smell something terrible nearby")
    elif item == str(pitRoom):
      print("You feel a cold wind blowing from a nearby cavern.")
    elif item == str(batRoom):
      print("You hear the rustle of bats")
  return roomNo[0], roomNo[1], roomNo[2], roomNo[3]

#basically returns the list index of the room number put in (1st item in group of 4)
def roomFind(numbertofind):
  for item in rooms:
    first = item.split(",")
    index = rooms.index(item)
    if first[0] == numbertofind:
      return index

#main bulk of code; generates random number and puts it into the room function    
randomRoom = randint(0, len(rooms))
current, left, right, center = room(rooms[randomRoom])
#menu, asks user what they want to do. Checks validity of any input
while wumpusDead == False or userDead == False:
  choice = input("What do you wish to do? 1. Move Rooms or 2. Fire Arrow?>>>")
  if choice == "1":
    where = input("Which room do you wish to move to?>>>")
    if where != left and where != right and where != center:
      print("Invalid room choice!")
    else:
      #uses roomFind function to find list index to put back into main room function
      index = roomFind(where)
      current, left, right, center = room(rooms[index])
      if current == str(wumpusRoom):
        #if in same room as wumpus, either runs away or kills you
        killOrNotKill=randint(1,2)
        if killOrNotKill == 1:
          print("The wumpus decided to eat you! You tasted nice!")
          print("Game Over!")
          exit()
        else:
          print("The wumpus runs away! You must find them again!")
          wumpusRoom = randint(1,20)
  elif choice == "2":
    #if the user chooses to fire arrow; checks validity of inputs and route to end game
    where = input("Which room do you wish to fire your arrow into?>>>")
    if where != left and where != right and where != center and where != current :
      print("That room is not adjacent! Your arrow instead bounces off the wall!")
    else:
      if str(where) == str(wumpusRoom):
        print("You have killed the wumpus! Congratulations!")
        wumpusDead = True
        exit()
      else:
        print("The wumpus was not in that room. You have wasted an arrow!")
