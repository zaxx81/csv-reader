import csv

class Dog:
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  def __str__(self):
    return f'{self.name} is a {self.age} year old {self.breed}.'

class Cat:
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  def __str__(self):
    return f'{self.name} is a {self.age} year old {self.breed}.'

# Driver Import from CSV
dogs = []
try:
  with open('data/dogs.csv', newline='') as dogs_csvfile:
    spamreader = csv.reader(dogs_csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      dogs.append(Dog(row[0], row[1].strip(), row[2].strip()))
  dogs.pop(0)
except:
  print('An error occurred trying to open the dog CSV file')


cats = []
try:
  with open('data/cats.csv', newline='') as cats_csvfile:
    spamreader = csv.reader(cats_csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
      cats.append(Cat(row[0], row[1].strip(), row[2].strip()))
  cats.pop(0)
except:
  print('An error occurred trying to open the cat CSV file')


answer = input('Would you like a cat or a dog?')
if answer.lower() == 'dog':
  print('Here are the dogs we have:')
  for x in dogs:
    print(f'\t{x}')

if answer.lower() == 'cat':
  print('Here are the cats we have:')
  for x in cats:
    print(f'\t{x}')

else:
  print(f"Sorry, we don't have any {answer}s here")
