class Song(object):
2
3 def __init__(self, lyrics):
4 self.lyrics = lyrics
5
6 def sing_me_a_song(self):
7 for line in self.lyrics:
8 print(line)
9
10 happy_bday = Song(["Happy birthday to you",
11 "I don't want to get sued",
12 "So I'll stop right there"])
13
14 bulls_on_parade = Song(["They rally around tha family",
15 "With pockets full of shells"])
16
17 happy_bday.sing_me_a_song()
18
19 bulls_on_parade.sing_me_a_song()
