score = 0
import time

def startover():
    startover = input("Start over? y/n \n >> ")
    if startover == "y":
            run()
    else:
        print("Your score is " + str(score))
        quit

print("Input name:")
name = input(">> ")

def cave():
    global score
    print(name+" finds themself in a spider cave, entangled in a web hanging 7 feet off the ground. In their surroundings is a brittle stalactite that seems it may come off the ceiling, and a swiss army knife. What do they reach for?")
    print("OPTIONS: stalactite, swiss knife (input these)")
    option1 = input(">> ")
    
    if option1 == "stalactite":
        print("The stalactite breaks off, but it slips out of "+name+"'s hand and shatters on the ground, alerting the spiders. Their impending doom is fulfilled by the hungry arachnids. YOU DIED")
        startover()
    elif option1 == "swiss knife":
        print(name + " latches on to the swiss knife. It has a good grip and fits well in their hand. They flip it up and slice the web open. YOU ARE SAFE. \n")
        score = score + 1
        
def exit():
     global score
     print("As "+name+" gets up from the web, they begin to realize their surroundings a bit more. In their possession is a dilapidated compass that they can hardly make out, and a trusty swiss army knife. To their east is a path down the cave where they can make out a slight cry, to their north is a small cave pond, and to their south is a tiny crevice that they can just barely fit through. Which direction do they go?")
     print("OPTIONS: east, north, south")
     option2 = input(">> ")
     
     if option2 == "east":
          print(name+" travels down the path to see a small child tangled in a similar web they were in. When they approach the child, his eyes turn red and his teeth turn sharp. The figure was not a child, but a mere trap, and he decapitates you. YOU DIED")
          startover()
     elif option2 == "north":
          print(name+" walks through the cave to the pond. They shortly find that the pond isn't normal. The water is purple with granular bright pebbles akin to stars. Around the pond is a black, almost void-like room. When "+name+" tries to touch the substance, an unrelenting force pulls them downward into the pond and enshrouds them in the substance, which is slowly melting their flesh. YOU DIED")
          startover()
     elif option2 == "south":
          print(name+" travelled through the narrow crevice which was just wide enough to move through. When they proceeded to the other side of the wall, there was a large opening with the brightness of the sun proceeding through. They had found the exit, and the next step was to find home. YOU ARE SAFE. \n")
          score = score+1

def outside():
     global score
     print(name+" exits the cave to see a bustling, lush village. While trying to get a sense of where they are, a woman approaches them. In a scottish accent she asks, 'Young child! What were you thinking going into that cave?! Its dangerous in there!'. She offers to take you to her home. Do you accept? y/n")
     option3 = input()
     if option3 == "y":
          print("The woman takes "+name+" in and makes them some food. She asks them a few questions about where they live, and where their parents are, but they can't remember anything at all. The last "+name+" can remember is their name. YOU ARE SAFE. \n")
          score = score + 1
     elif option3 == "n":
          print("She leaves "+name+" to fend for themself and they walk about the place. Eventually, they discover a well. They climb up a set of steps to see inside and they trip over the last step and fall into the well. YEOUUCHH!!! YOU DIED.")
          startover()

def conflict():
     global score
     print("After chatting with the woman for a bit, you find that the woman is named Melissa. A nice conversation and a cup of tea later, "+name+" hears a distant, but vicious growl. Moments after the disturbing noise, A loud thud resounds in the door. Soon enough the door bursts open to reveal a rabid coyote. Melissa is petrified. They have an army knife and a compass. What do they do?")
     print("OPTIONS: run away, stand there, attack")
     option4 = input()
     if option4 == "run away":
          print(name+" bolts out the door. Unfortunately, the coyote is way faster than them. YOU DIED.")
          startover()
     elif option4 == "stand there":
          print(name+" just simply stood there in shock. Thankfully, the coyote is blind, and "+name+" was very quiet. Since the coyotes poor senses were not working, he promply exited the room, and "+name+" and Melissa both just sat down. YOU ARE SAFE. \n")
          score = score + 1
     elif option4 == "attack":
          print(name+" bravely charged the coyote. In a quick turn of events, they missed because their aim is TRASHHHHHHHH and tripped like an idiot. The coyote mauled them. YOU DIED.")
          startover()

def shankle():
     print("Melissa thanks "+name+" for shutting up and standing there even though they both would've died if it weren't up to luck. Still though, she thanks "+name+" and gives them a SHOTGUN (blunderbuss if you're a nerd) YEAHHHHHHHHHH!!!!! She does insist they must leave because she has an upcoming village party and she won't be at home ("+name+" isn't invited LOL) but it's okay because they have some home-finding to do. "+name+" lives in Britain so they try to take a carriage. They have to pay for the ride so they sell their stupid useless compass for some dabloons. Now they are on your way to London. Nering the end of their ride they are attacked by a random dude. What do they do?")
     print("OPTIONS: hit w gun, shoot w gun, stab w knife")
     option5 = input()
     if option5 == "stab w knife":
          print("You must have remembered this was London! You take out your swiss knife and start clashing shanks together. It was an epic duel, a brilliant one! You came out victorious and are now king of England because of your glorious shank fight. BE PROUD!!")
          score = 99999
          print("YOU WIN!! Your score is: "+str(score))
     else:
          print("Dude, this is London... he shanked you and you died. gg full piece 180 noscope clipped")
          startover()
     


def run():
    cave()
    time.sleep(5)
    exit()
    time.sleep(5)
    outside()
    time.sleep(5)
    conflict()
    time.sleep(5)
    shankle() 
run()

y = 0
while y != 99999999:
     y+1
     print(y)