#!/usr/local/bin/python

import sys
import os
import logging
import sqlite3

basePath = "/wrk/xhdhdnobkup3/sanchayk/sanchay_work/my_git/projects/stock_analysis"
dataPath = basePath + "/database/data"
indexPath = basePath + "/database/index"

sqlite_path = basePath + "/src/pybase/sqlite/"

sys.path.append(sqlite_path)

import dataType
import DB
import DBMgr
#import absDB
#import abstractDB

logging.basicConfig(level=logging.DEBUG)

basePath = "/wrk/xhdhdnobkup3/sanchayk/sanchay_work/my_git/projects/stock_analysis"
dataPath = basePath + "/database/data"
indexPath = basePath + "/database/index"

commom_path = basePath + "src/pybase/common/"
db_path     = basePath + "src/pybase/abstractDB/"

sys.path.append(commom_path)
sys.path.append(db_path)

dataTypeDict = {
  "Symbol"                      : "VARCHAR(30)",
  "Series"                      : "VARCHAR(20)",
  "Date"                        : "DATE",
  "PrevClose"                   : "REAL",
  "OpenPrice"                   : "REAL",
  "HighPrice"                   : "REAL",
  "LowPrice"                    : "REAL",
  "LastPrice"                   : "REAL",
  "ClosePrice"                  : "REAL",
  "AveragePrice"                : "REAL",
  "TotalTradedQuantity"         : "REAL",
  "Turnover"                    : "REAL",
  "NumberOfTrades"              : "REAL",
  "DeliverableQty"              : "REAL",
  "PercentageDlyQtToTradedQty"  : "REAL"
}

#def createHeaderDict(header) :
#  

def parseAndCreateDB(dbMgr, dbName, dbType, tableName) :
  database = dbMgr.GetDB(dbName, dbType)
  # TODO: get all file for this company, check time stamp with database, if need to be created
  # if possible only add entries which are added new.

  message = "Creating table for " + tableName
  logging.info(message)

  company_path = dataPath + "/" + tableName
  for root, dirs, files in os.walk(company_path):
    for filename in files:
      file_path = company_path + "/" + filename
      p_file = open(file_path, "r")
      header = p_file.readline()
      headerDict = createHeaderDict(header)
      database.CreateTable(tableName, headerDict)
      rowData = "sanchay"
      bseEqDB.AddRow(tableName, headerDict, rowData)
      dbMgr.ExportDB(dbName, dbType, "STDOUT")
      for line in p_file :
        print line


# for each entry in index, create one data base. for each company.
def createDatabase(dbName, dbType) :
  logging.info("Creating " + dbName + " equity data base")
  #dbMgr = getDatabaseMgr()
  dbMgr = DBMgr.DBMgr()
  f_index = open(indexPath, "r")
  # TODO: trim extra spaces
  for company_name in f_index :
    parseAndCreateDB(dbMgr, dbName, dbType, company_name)
  logging.info("Successfully created " + dbName + " equity data base")

#def temp() :
#  logging.info("Creating BSE equity data base")
#  dbMgr = abstractDB.DBMgr()
#  bseEqDB = dbMgr.GetDB("BSE_EQ")
#  bseEqDB.SetDBType("sqlite3")
#  headerDict = {
#          "Symbol" : "VARCHAR(30)",
#          "Series" : "VARCHAR(20)",
#          "Date" : "DATE",
#          "PrevClose" : "REAL",
#          "OpenPrice" : "REAL",
#          "HighPrice" : "REAL",
#          "LowPrice" : "REAL",
#          "LastPrice" : "REAL",
#          "ClosePrice" : "REAL",
#          "AveragePrice" : "REAL",
#          "TotalTradedQuantity" : "REAL",
#          "Turnover" : "REAL",
#          "NumberOfTrades" : "REAL",
#          "DeliverableQty" : "REAL",
#          "PercentageDlyQtToTradedQty" : "REAL"}
#
#  bseEqDB.CreateTable("TATAMOTORS", headerDict)
#  rowData = "sanchay"
#  bseEqDB.AddRow("TATAMOTORS", headerDict, rowData)
#  dbMgr.ExportDB("BSE_EQ", "STDOUT")

def main() :
  logging.info("Creating BSE equity data base")
  dbName = "BSE"
  dbType = "sqlite3"
  createDatabase(dbName, dbType)

if ( __name__ == "__main__") :
  main()
