`class Other(object):
2
3 def override(self):
4 print("OTHER override()")
5
6 def implicit(self):
7 print("OTHER implicit()")
8
9 def altered(self):
10 print("OTHER altered()")
11
12 class Child(object):
13
14 def __init__(self):
15 self.other = Other()
16
17 def implicit(self):
18 self.other.implicit()
19
20 def override(self):
21 print("CHILD override()")
22
23 def altered(self):
24 print("CHILD, BEFORE OTHER altered()")
25 self.other.altered()
26 print("CHILD, AFTER OTHER altered()")
27
28 son = Child()
29
INHERITANCE VERSUS COMPOSITION 221
30 son.implicit()
31 son.override()
32 son.altered()
