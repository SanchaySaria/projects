#!/usr/local/bin/python
import sys
sys.path.append('/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/')

import mysql.connector
from mysql.connector import errocode
import logging
logging.basicConfig(level=logging.DEBUG)

print "hi this is sanchay"

try
  cnx = mysql.connector.connect(user='root', password='76684678', host='127.0.0.1', database='mydb')
  print "cnx is established"
except mysql.connector.Error as err :
  print err
else
cnx.close()


#def create_connection():
#    """ create a database connection to a database that resides
#        in the memory
#    """
#    try:
#        conn = sqlite3.connect(':memory:')
#        print(sqlite3.version)
#    except Error as e:
#        print(e)
#    finally:
#        conn.close()
# 
#if __name__ == '__main__':
#    create_connection()
#
