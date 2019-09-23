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


#class DBMgr :
#  def __init__ (self) :
#    logging.info("Created data base manager")
#    self.dbList_ = {} # Dict of all data base objects
#
#  def ExportDB (self, dbName, exportTo) :
#    if not dbName in self.dbList_.keys() :
#      logging.error("Could not find data base %s", dbName)
#      return
#    logging.info("Exporting data base %s to %s",dbName, exportTo)
#    if (exportTo == "STDOUT") :
#      logging.info("Data base %s is of type %s", dbName, self.dbList_[dbName].GetDBType())
#      conn = sqlite3.connect(dbName)
#      tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
#      for tab in tables :
#        print(tab[0])
#      rawCursor = conn.execute('select * from TATAMOTORS')
#      header =  [description[0] for description in rawCursor.description]
#
#      print "   ".join(header)
#      conn.close()
#
#  def GetDB(self, dbName) :
#    if dbName in self.dbList_.keys() :
#      return self.dbList_[dbName]
#    oneDB = DB(dbName)
#    self.dbList_[dbName] = oneDB
#    return oneDB
#
#class DB :
#  def __init__ (self, dbName) :
#    self.dbName_ = dbName
#    self.dbType_ = "Sqlite3"
#    self.CreateDB()
#
#  def SetDBType(self, dbType) :
#    self.dbType_ = dbType
#
#  def GetName(self) :
#    return self.dbName_
#
#  def GetDBType(self) :
#    return self.dbType_
#
#  def CreateDB (self) :
#    logging.info("Creating data base %s", self.dbName_)
#    conn = sqlite3.connect(self.dbName_)
#    conn.close()
#
#  def CreateTable (self, tableName, headerDict) :
#    conn = sqlite3.connect(self.dbName_)
#    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
#    for tab in tables :
#      if(tab[0] == tableName) :
#        logging.info("Table %s already exists in data base %s", tableName, self.dbName_)
#        return
#    logging.info("Creating table %s in data base %s", tableName, self.dbName_)
#    createTableCmd = "CREATE TABLE " + tableName + "("
#    createTableCmd += ','.join(['%s %s' % (key, val) for (key, val) in headerDict.items()])
#    createTableCmd += ");"
#    print createTableCmd
#    conn = sqlite3.connect(self.dbName_)
#    conn.execute(createTableCmd)
#
#  def AddRow (self, tableName, headerDict, rowData) :
#    conn = sqlite3.connect(self.dbName_)
#    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
#    isTableExist = "FALSE"
#    for tab in tables :
#      if(tab[0] == tableName) :
#        isTableExist = "TRUE"
#        break
#    if () :
#      logging.error("Table %s not found in data base %s", tableName, self.dbName_)
#      return
#    addRawCmd = "INSERT INTO " + tableName + "("
#    addRawCmd += ','.join(['%s' % (key) for (key, val) in headerDict.items()])
#    addRawCmd += ") VALUES()"
#    print addRawCmd
#    conn = sqlite3.connect(self.dbName_)
#    #conn.execute(createTableCmd)
#
#
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
