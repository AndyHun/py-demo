from Creature import Creature
from Person import Person
from Scholar import Scholar

animal = Creature()
print("This is an animal:", animal)

print("Person common intelligence level:", Person.basic_intelligence_level)
Person.intelli_level()
tom = Person("tom")
print("This is a person:", tom)
tom.say_hi();

scholar_tim = Scholar("tim")
print("Scholar common intelligence level:", Scholar.basic_intelligence_level)
scholar_tim.say_hi()
scholar_tim.intelli_level()
