#!/usr/local/bin/python

import sqlite3
from sqlite3 import Error
import logging
logging.basicConfig(level=logging.DEBUG)

class DB :
  def __init__ (self, dbName) :
    self.dbName_ = dbName
    self.dbType_ = "Sqlite3"
    self.CreateDB()

  def SetDBType(self, dbType) :
    self.dbType_ = dbType

  def GetName(self) :
    return self.dbName_

  def GetDBType(self) :
    return self.dbType_

  def CreateDB (self) :
    logging.info("Creating data base %s", self.dbName_)
    conn = sqlite3.connect(self.dbName_)
    conn.close()

  def CreateTable (self, tableName, headerDict) :
    conn = sqlite3.connect(self.dbName_)
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for tab in tables :
      if(tab[0] == tableName) :
        logging.info("Table %s already exists in data base %s", tableName, self.dbName_)
        return
    logging.info("Creating table %s in data base %s", tableName, self.dbName_)
    createTableCmd = "CREATE TABLE " + tableName + "("
    createTableCmd += ','.join(['%s %s' % (key, val) for (key, val) in headerDict.items()])
    createTableCmd += ");"
    print createTableCmd
    conn = sqlite3.connect(self.dbName_)
    conn.execute(createTableCmd)

  def AddRow (self, tableName, headerDict, rowData) :
    conn = sqlite3.connect(self.dbName_)
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    isTableExist = "FALSE"
    for tab in tables :
      if(tab[0] == tableName) :
        isTableExist = "TRUE"
        break
    if () :
      logging.error("Table %s not found in data base %s", tableName, self.dbName_)
      return
    addRawCmd = "INSERT INTO " + tableName + "("
    addRawCmd += ','.join(['%s' % (key) for (key, val) in headerDict.items()])
    addRawCmd += ") VALUES()"
    print addRawCmd
    conn = sqlite3.connect(self.dbName_)
    #conn.execute(createTableCmd)
