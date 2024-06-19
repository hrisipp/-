my_dict = {'Slavik': 2000, 'Den': 1999}
print(my_dict)
print(my_dict.get('Slavik'))
print(my_dict.get('Max'))
my_dict.update({'Katya': 1996,
                'Elena': 1990})
my_dict.pop('Den')
print(my_dict.get('Den'))
print(my_dict)

my_set = {1, 2, 3, 5, 'hello', 1, 3, 2, 5, 'hello'}
print(my_set)
my_set.add('hay')
my_set.add(6)
my_set.discard(2)
print(my_set)