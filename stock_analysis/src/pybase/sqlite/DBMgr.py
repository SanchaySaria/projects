#!/usr/local/bin/python

import sys
import os
import logging
import sqlite3
from sqlite3 import Error

logging.basicConfig(level=logging.DEBUG)

basePath = "/Users/sanchaysaria/my_git/projects/stock_analysis"
#basePath = "/wrk/xhdhdnobkup3/sanchayk/sanchay_work/my_git/projects/stock_analysis"
dataPath = basePath + "/database/data"
indexPath = basePath + "/database/index"

sqlite_path = basePath + "/src/pybase/sqlite/"

sys.path.append(sqlite_path)

import DB

print "Imported DBMgr class"

class DBMgr :
  def __init__ (self) :
    logging.info("Initialized data base manager")
    self.dbList_ = {} # Dict of all data base objects

  def GetDB(self, dbName, dbType) :
    if dbName in self.dbList_.keys() :
      return self.dbList_[dbName]
    oneDB = DB.DB(dbName, dbType) # Create DB object
    self.dbList_[dbName] = oneDB
    return oneDB

  def ExportDB (self, dbName, dbType, exportTo) :
    if not dbName in self.dbList_.keys() :
      logging.error("Could not find data base %s", dbName)
      return
    logging.info("Exporting data base %s to %s",dbName, exportTo)
    if (exportTo == "FILE") :
      f = open("database.txt",'w')
      logging.info("Data base %s is of type %s", dbName, self.dbList_[dbName].GetDBType())
      conn = sqlite3.connect(dbName)
      tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
      for tab in tables :
        f.write(tab[0])
        f.write("\n")
        #print(tab[0])
        #print(tab[0])
        selectTableCmd = "select * from " + tab[0]
        rawCursor = conn.execute(selectTableCmd)
        header =  [description[0] for description in rawCursor.description]
        headerStr = "   ".join(header)
        print "   ".join(header)
        f.write(headerStr)
        f.write("\n")
        #print "   ".join(header)
        for row in conn.execute( "select * from " + tab[0]):
          f.write(str(row))
          f.write("\n")
          #print(row)
          #print(row)
      conn.close()

