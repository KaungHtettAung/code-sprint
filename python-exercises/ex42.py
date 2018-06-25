## Animal is-a object (yes, sort of confusing) look at the extra credit
2 class Animal(object):
3 pass
4
5 ## ??
6 class Dog(Animal):
7
8 def __init__(self, name):
9 ## ??
10 self.name = name
11
12 ## ??
13 class Cat(Animal):
14
15 def __init__(self, name):
16 ## ??
17 self.name = name
18
19 ## ??
20 class Person(object):
21
22 def __init__(self, name):
23 ## ??
24 self.name = name
25
26 ## Person has-a pet of some kind
194 LEARN PYTHON THE HARD WAY
27 self.pet = None
28
29 ## ??
30 class Employee(Person):
31
32 def __init__(self, name, salary):
33 ## ?? hmm what is this strange magic?
34 super(Employee, self).__init__(name)
35 ## ??
36 self.salary = salary
37
38 ## ??
39 class Fish(object):
40 pass
41
42 ## ??
43 class Salmon(Fish):
44 pass
45
46 ## ??
47 class Halibut(Fish):
48 pass
49
50
51 ## rover is-a Dog
52 rover = Dog("Rover")
53
54 ## ??
55 satan = Cat("Satan")
56
57 ## ??
58 mary = Person("Mary")
59
60 ## ??
61 mary.pet = satan
62
63 ## ??
64 frank = Employee("Frank", 120000)
65
66 ## ??
67 frank.pet = rover
68
69 ## ??
70 flipper = Fish()
71
IS-A, HAS-A, OBJECTS, AND CLASSES 195
72 ## ??
73 crouse = Salmon()
74
75 ## ??
76 harry = Halibut()
