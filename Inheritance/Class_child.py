from Inheritance.Class_parent_1 import Parent1
from Inheritance.Class_parent_2 import Parent2
from Inheritance.Class_parent_3 import Parent3

class Child(Parent1, Parent2, Parent3):

    def reaper(self):
        self.output()


Child().reaper()

