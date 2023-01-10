# Practice 01
# list version
animals = ['rabbit', 'cat', 'dog', 'aligator', 'tiger', 'Lion']
animals.extend(['elephant', 'crow', 'parrot'])
print(animals)
animals.sort(reverse=True)
print(animals)
even_animals = animals[1::2]
print(even_animals)

# Small Quiz
set_a = set('fastcampus')
set_b = set('shinhan')

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
print(set_a ^ set_b)

# Practice 02
# 1
_list = [
  {
    'Name': 'Johnny Silverhand',
    'Locale': 'Night City',
    'Age': 120,
    'Username': 'Johnny',
  },
  {
    'Name': 'John Doe',
    'Locale': 'CA, USA',
    'Age': 40,
    'Username': 'Doh',
  },
  {
    'Name': 'Jane Doe',
    'Locale': 'Seoul, Korea',
    'Age': 24,
    'Username': 'jane=doe',
  },
  {
    'Name': 'Foo Bar',
    'Locale': 'Busan, Korea',
    'Age': 31,
    'Username': 'foo-bar',
  },
]

print(_list)


# 2
for l in _list:
  if l['Name'] == 'Jane Doe':
    l['Locale'] = 'London, UK'

print(_list[2])

# 3
print(_list[0].keys(), _list[0].values())
print(_list[1].keys(), _list[1].values())
print(_list[2].keys(), _list[2].values())
print(_list[3].keys(), _list[3].values())

# 4
cities = [
    'Daejun', 'Ulsan', 'Seoul', 'Jeju',
    'Busan', 'Ulsan', 'Daegu', 'Daejeon',
    'Seoul', 'Seoul, Daejeon', 'Gwangju',
    'Ulsan', 'Jeju', 'Gwangju', 'Seoul'
]

cities = list(set(cities))
cities.sort()
print(cities)

