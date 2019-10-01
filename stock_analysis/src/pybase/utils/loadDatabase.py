#!/usr/local/bin/python

import sys
import os
import logging
import sqlite3
from collections import OrderedDict

logging.basicConfig(level=logging.DEBUG)

#basePath = "/Users/sanchaysaria/my_git/projects/stock_analysis"
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
  "No.ofTrades"              : "REAL",
  "DeliverableQty"              : "REAL",
  "%DlyQttoTradedQty"              : "REAL",
  "PercentageDlyQtToTradedQty"  : "REAL"
}

def createHeaderDict(header) :
  header = header.replace('\t', '')
  header = header.replace(' ', '')
  logging.info("Creating header dict for %s", header)
  headerDict = OrderedDict()
  for key in header.split(',') :
    key = key.replace('\"', '')
    key = key.replace('\n', '')
    #key = key.replace('\"', '')
    val =  dataTypeDict[key]
    if (key == "No.ofTrades") :
      key = "NumberOfTrades"
    if (key == "%DlyQttoTradedQty") :
      key = "PercentageDlyQtToTradedQty"
    #print key + " : " + dataTypeDict[key]
    headerDict[key] = dataTypeDict[key]
  return headerDict

def parseAndCreateDB(dbMgr, dbName, dbType, tableName) :
  dbName = dbName.strip("\n")
  dbType = dbType.strip("\n")
  tableName = tableName.strip("\n")
  bseEqDB = dbMgr.GetDB(dbName, dbType)
  # TODO: get all file for this company, check time stamp with database, if need to be created
  # if possible only add entries which are added new.

  logging.info("Creating table for %s", tableName)

  company_path = dataPath + "/" + tableName
  logging.info("Company path %s", company_path)

  #for r, d, f in os.walk("/Users/sanchaysaria/my_git/projects/stock_analysis/database/data/TATAMOTORS") :
  #  logging.info(r)
  #  for dname in f :
  #    logging.info(dname)


  #for root, dirs, files in os.walk("/Users/sanchaysaria/my_git/projects/stock_analysis/database/data/TATAMOTORS") :
  for root, dirs, files in os.walk(company_path) :
    for filename in files :
      logging.info("sanchay %s", filename)
      file_path = company_path + "/" + filename
      p_file = open(file_path, "r")
      header = p_file.readline()
      headerDict = createHeaderDict(header)
      #dataTypeDict = createHeaderDict(header)

      #bseEqDB .CreateTable(tableName, dataTypeDict)
      bseEqDB .CreateTable(tableName, headerDict)
      for rowData in p_file :
        #print "Adding row : \n" + rowData
        #bseEqDB.AddRow(tableName, dataTypeDict, rowData)
        bseEqDB.AddRow(tableName, headerDict, rowData)
  #dbMgr.ExportDB(dbName, dbType, "STDOUT")
  dbMgr.ExportDB(dbName, dbType, "FILE")


# for each entry in index, create one data base. for each company.
def createDatabase(dbName, dbType) :
  logging.info("Creating " + dbName + " equity data base")
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
#  dataTypeDict = {
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
#  bseEqDB.CreateTable("TATAMOTORS", dataTypeDict)
#  rowData = "sanchay"
#  bseEqDB.AddRow("TATAMOTORS", dataTypeDict, rowData)
#  dbMgr.ExportDB("BSE_EQ", "STDOUT")

def main() :
  logging.info("Creating BSE equity data base")
  dbName = "BSE"
  dbType = "sqlite3"
  createDatabase(dbName, dbType)

if ( __name__ == "__main__") :
  main()
