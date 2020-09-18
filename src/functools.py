#functools.py

import urllib.error
import urllib.request

from functools import lru_cache

@lru_cache(maxsize=24)
def get_webpage(module):
    """
    Get specified web page
    :param module:
    :return:
    """
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read
    except urllib.error.HTTPError:
        return None
from functools import partial

def add(x, y):
    return  x + y


from functools import singledispatch


@singledispatch
def multiple(x, y):
    raise NotImplementedError('Unsupported Type')



@multiple.register(int)
def _(x, y):
    print("First argument is of type ", type(x))
    print(x + y)


@multiple.register(str)
def _(x, y):
    print("First argument is of type ", type(x))
    print(x + y)


@multiple.register(list)
def _(x, y):
    print("First argument is of type ", type(x))
    print(x + y)


if __name__ == '__main__':
    modules = ['functools', 'collections', 'os', 'sys']
    for module in modules:
        page = get_webpage(module)
        if page:
            print("{} module page found".format(module))

    p_add = partial(add, 2)
    print(p_add(4))
    multiple(1, 2)
    multiple('add', 'add2')
    multiple([1], [2])