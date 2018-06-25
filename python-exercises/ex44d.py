class Parent(object):
2
3 def override(self):
4 print("PARENT override()")
5
6 def implicit(self):
7 print("PARENT implicit()")
8
9 def altered(self):
10 print("PARENT altered()")
11
12 class Child(Parent):
13
14 def override(self):
15 print("CHILD override()")
16
17 def altered(self):
18 print("CHILD, BEFORE PARENT altered()")
19 super(Child, self).altered()
20 print("CHILD, AFTER PARENT altered()")
21
22 dad = Parent()
23 son = Child()
24
25 dad.implicit()
26 son.implicit()
27
28 dad.override()
29 son.override()
30
31 dad.altered()
32 son.altered()
