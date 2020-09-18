#collections.py

from collections import ChainMap

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print (car_pricing['A/C'])
#1000


from collections import Counter

counter = Counter('superflous')
print(counter.elements())
#<itertools.chain object at 0x10989f490>

print(list(counter.elements()))
# ['s', 's', 'u', 'u', 'p', 'e', 'r', 'f', 'l', 'o']


from collections import defaultdict

animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print(animal['Nick'])
#Monkey

print(animal)
#defaultdict(<function <lambda> at 0x10e834280>, {'Sam': 'Tiger', 'Nick': 'Monkey'})


from collections import deque
import string
d = deque(string.ascii_lowercase)
for letter in d:
    print(letter)
d.append('right')
print(d)
# deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'bork'])

d.appendleft('left')
print(d)
# deque(['left', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'bork'])

d.rotate(1)
print(d)
# deque(['bork', 'left', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


from collections import namedtuple
Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ferrari', cost=123, amount=10)
print(auto_parts.desc)
#Ferrari


from collections import OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
new_ordered_dict = OrderedDict(sorted(d.items()))
print(new_ordered_dict)