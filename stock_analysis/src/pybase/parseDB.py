#!/usr/local/bin/python

import sys
import common
import logging
import sqlite3
import abstractDB

logging.basicConfig(level=logging.DEBUG)

basePath = "/wrk/xhdhdnobkup3/sanchayk/sanchay_work/my_git/projects/stock_analysis"
dbPath = basePath + "/database/data"
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

def createHeaderDict(header) :
  

def parseAndCreateDB(dbMgr, dbName, dbType, tableName) :
  logging.info("Creating BSE equity data base")
  bseEqDB = dbMgr.GetDB(dbName, dbType)

  p_file = open(dbPath + "/" + tableName + "/" + "ITC_2016", "r")
  header = p_file.readline()
  headerDict = createHeaderDict(header)

  bseEqDB.CreateTable(tableName, headerDict)
  rowData = "sanchay"
  bseEqDB.AddRow(tableName, headerDict, rowData)
  dbMgr.ExportDB(dbName, dbType, "STDOUT")



  for line in p_file :
    print line


if ( __name__ == "__main__") :
  parseAndCreateDB()
