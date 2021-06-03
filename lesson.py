from lesson_package.tools import utils
from lesson_package.talk import human
from lesson_package.talk import animal
#from lesson_package.talk import *
from termcolor import colored

print(colored('color', 'red'))

r = utils.say_twice('hello')

print(r)
print(human.sing())
print(human.cry())

print(animal.sing())
print(animal.cry())
