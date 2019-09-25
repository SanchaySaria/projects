#!/usr/local/bin/python

import sys
sys.path.append('/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/')

import mysql.connector
from mysql.connector import errocode
import logging
logging.basicConfig(level=logging.DEBUG)

print "Hi this is DBMgr class"


class DBMgr :
  def __init__ (self) :
    logging.info("Initialized data base manager")
    self.dbList_ = {} # Dict of all data base objects

  def GetDB(self, dbName) :
    if dbName in self.dbList_.keys() :
      return self.dbList_[dbName]
    oneDB = DB(dbName) # Create DB object
    self.dbList_[dbName] = oneDB
    return oneDB

  def ExportDB (self, dbName, exportTo) :
    if not dbName in self.dbList_.keys() :
      logging.error("Could not find data base %s", dbName)
      return
    logging.info("Exporting data base %s to %s",dbName, exportTo)
    if (exportTo == "STDOUT") :
      logging.info("Data base %s is of type %s", dbName, self.dbList_[dbName].GetDBType())
      conn = sqlite3.connect(dbName)
      tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
      for tab in tables :
        print(tab[0])
      rawCursor = conn.execute('select * from TATAMOTORS')
      header =  [description[0] for description in rawCursor.description]

      print "   ".join(header)
      conn.close()

