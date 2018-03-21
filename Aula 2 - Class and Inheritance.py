# -*- coding: utf-8 -*-


class Animal:
    def __init__(self, size, sound):
        self.size = size
        self.sound = sound


class Cat(Animal):
    def __init__(self, size, sound, name):
        Animal.__init__(self, size, sound)
        self.name = name

    def purr(self):
        print("rrrrrr S2")


class Dog:
    def __init__(self, size, sound):
        Animal.__init__(self, size, sound)

    def bark(self):
        print("Woof! Woof!")


mickey = Cat("medium", "meoww", "Mickey")
print(mickey.size)
print(mickey.sound)
print(mickey.name)
mickey.purr()

print('I am a {} called {} and I say "{}".'
      .format("cat", mickey.name, mickey.sound))

rex = Dog("small", "au-au")
print(rex.size)
print(rex.sound)
rex.bark()
