class Parent(object):
2
3 def implicit(self):
4 print("PARENT implicit()")
5
6 class Child(Parent):
7 pass
8
9 dad = Parent()
10 son = Child()
11
12 dad.implicit()
13 son.implicit()
