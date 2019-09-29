#!/usr/local/bin/python

import re
import sqlite3
from sqlite3 import Error
import logging
from collections import OrderedDict
logging.basicConfig(level=logging.DEBUG)

print "Imported DB class"

class DB :
  def __init__ (self, dbName, dbType) :
    self.dbName_ = dbName
    self.dbType_ = dbType
    self.CreateDB()

  def SetDBType(self, dbType) :
    self.dbType_ = dbType

  def GetName(self) :
    return self.dbName_

  def GetDBType(self) :
    return self.dbType_

  def CreateDB (self) :
    logging.info("Creating data base %s of type %s", self.dbName_, self.dbType_)
    conn = sqlite3.connect(self.dbName_)
    conn.close()

  def CreateTable (self, tableName, headerDict) :
    #print "printing dict"
    #print(headerDict)
    conn = sqlite3.connect(self.dbName_)
    getTableCmd = "SELECT name FROM sqlite_master WHERE type='table';"
    print "sqlite cmd : " + getTableCmd
    tables = conn.execute(getTableCmd)
    for tab in tables :
      if(tab[0] == tableName) :
        logging.info("Table %s already exists in data base %s", tableName, self.dbName_)
        return
    logging.info("Creating table %s in data base %s", tableName, self.dbName_)
    createTableCmd = "CREATE TABLE " + tableName + "("
    createTableCmd += ','.join(['%s %s' % (key, val) for (key, val) in headerDict.items()])
    createTableCmd += ");"
    print "sqlite cmd : " + createTableCmd
    conn = sqlite3.connect(self.dbName_)
    conn.execute(createTableCmd)

  def AddRow (self, tableName, headerDict, rowData) :
    conn = sqlite3.connect(self.dbName_)
    getTableCmd = "SELECT name FROM sqlite_master WHERE type='table';"
    #print "sqlite cmd : " + getTableCmd
    tables = conn.execute(getTableCmd)
    isTableExist = "false"
    for tab in tables :
      if(tab[0] == tableName) :
        isTableExist = "true"
        break
    if (isTableExist == "false") :
      logging.error("Table %s not found in data base %s", tableName, self.dbName_)
      return
    #print rowData
    rowData = rowData.replace(' ', '')
    rowData = rowData.replace('\t', '')
    #print rowData
    addRawCmd = "INSERT INTO " + tableName + "("
    addRawCmd += ','.join(['%s' % (key) for (key, val) in headerDict.items()])
    addRawCmd += ") VALUES("
    addRawCmd += rowData
    #addRawCmd += ','.join(['%s' % (val) for val in rowData])
    addRawCmd += ")"
    #print "sqlite cmd : " + addRawCmd
    conn = sqlite3.connect(self.dbName_)
    conn.execute(addRawCmd)
    conn.commit()
    conn.close()

