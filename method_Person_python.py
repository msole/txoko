class Person:
  '''This class represents a person object'''
  
    def__init__ (self, first_name, surname, tel):
      self.first_name = fisrt_name
      self.surname = surname
      self.tel = tel
      
    def full_name(self):
      return self.first_name + " " + self.surname
      
class Employee(Person):
  
    def __init__ (self, first_name, surname, tel, salary):
      super(). init (first_name, surname, tel)
      self.salary = salary
    
    def give_raise(self, amount):
      self.salary = self.salary + amount
