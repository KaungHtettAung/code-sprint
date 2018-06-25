class Parent(object):
2
3 def override(self):
4 print("PARENT override()")
5
6 class Child(Parent):
7
8 def override(self):
9 print("CHILD override()")
10
11 dad = Parent()
12 son = Child()
13
14 dad.override()
15 son.override()
