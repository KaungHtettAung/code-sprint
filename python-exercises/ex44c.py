class Parent(object):
2
3 def altered(self):
4 print("PARENT altered()")
5
6 class Child(Parent):
7
8 def altered(self):
9 print("CHILD, BEFORE PARENT altered()")
10 super(Child, self).altered()
11 print("CHILD, AFTER PARENT altered()")
12
13 dad = Parent()
14 son = Child()
15
16 dad.altered()
17 son.altered()
