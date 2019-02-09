class Person:
	age = 45
	pro = 'Engineer'

person = Person()
print('Age ', getattr(person, 'age'))
print('Prof ', person.pro)