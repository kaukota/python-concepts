#context_manager,py

import sqlite3

class DataConn:
    """"""
    def __init__(self, db_name):
        """Constructor"""
        self.db_name = db_name

    def __enter__(self):
        """Open db connection"""
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exec_type, exec_val, exec_tb):
        """Close db connection"""
        self.conn.close()
        if exec_val:
            raise


from contextlib import  contextmanager

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print('We have an error')
    finally:
        print ('Closing File')
        f_obj.close()



from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://google.com')) as webpage:
    for line in webpage:
        #process the line
        pass

from contextlib import suppress

with suppress(FileNotFoundError):
    with open('noFile.txt') as fobj:
        for line in fobj:
            print(line)


from contextlib import redirect_stdout
with open('text.txt', 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)

if __name__ == '__main__':
    with file_open('test.txt') as fobj:
        fobj.write('Testing context managers')