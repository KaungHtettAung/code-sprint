
from sys import exit
2
3 def gold_room():
4 print("This room is full of gold. How much do you take?")
5
6 choice = input("> ")
7 if "0" in choice or "1" in choice:
8 how_much = int(choice)
9 else:
10 dead("Man, learn to type a number.")
11
12 if how_much < 50:
13 print("Nice, you're not greedy, you win!")
14 exit(0)
15 else:
16 dead("You greedy bastard!")
17
18
19 def bear_room():
20 print("There is a bear here.")
21 print("The bear has a bunch of honey.")
22 print("The fat bear is in front of another door.")
23 print("How are you going to move the bear?")
24 bear_moved = False
25
26 while True:
27 choice = input("> ")
28
29 if choice == "take honey":
30 dead("The bear looks at you then slaps your face off.")
31 elif choice == "taunt bear" and not bear_moved:
32 print("The bear has moved from the door.")
33 print("You can go through it now.")
34 bear_moved = True
35 elif choice == "taunt bear" and bear_moved:
BRANCHES AND FUNCTIONS 157
36 dead("The bear gets pissed off and chews your leg off.")
37 elif choice == "open door" and bear_moved:
38 gold_room()
39 else:
40 print("I got no idea what that means.")
41
42
43 def cthulhu_room():
44 print("Here you see the great evil Cthulhu.")
45 print("He, it, whatever stares at you and you go insane.")
46 print("Do you flee for your life or eat your head?")
47
48 choice = input("> ")
49
50 if "flee" in choice:
51 start()
52 elif "head" in choice:
53 dead("Well that was tasty!")
54 else:
55 cthulhu_room()
56
57
58 def dead(why):
59 print(why, "Good job!")
60 exit(0)
61
62 def start():
63 print("You are in a dark room.")
64 print("There is a door to your right and left.")
65 print("Which one do you take?")
66
67 choice = input("> ")
68
69 if choice == "left":
70 bear_room()
71 elif choice == "right":
72 cthulhu_room()
73 else:
74 dead("You stumble around the room until you starve.")
75
76
77 start()
