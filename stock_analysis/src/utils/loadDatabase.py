#!/usr/local/bin/python

import sys
sys.path.append('/Users/sanchaysaria/work/financial_analysis/src/pybase/pylib/')
sys.path.append('/Users/sanchaysaria/work/financial_analysis/src/pybase/abstractDB/')

import common
import logging
import sqlite3
import abstractDB

logging.basicConfig(level=logging.DEBUG)


# for each entry in index, create one data base. for each company.



def main() :
  logging.info("Creating BSE equity data base")
  dbMgr = abstractDB.DBMgr()
  bseEqDB = dbMgr.GetDB("BSE_EQ")
  bseEqDB.SetDBType("sqlite3")
  headerDict = {
          "Symbol" : "VARCHAR(30)",
          "Series" : "VARCHAR(20)",
          "Date" : "DATE",
          "PrevClose" : "REAL",
          "OpenPrice" : "REAL",
          "HighPrice" : "REAL",
          "LowPrice" : "REAL",
          "LastPrice" : "REAL",
          "ClosePrice" : "REAL",
          "AveragePrice" : "REAL",
          "TotalTradedQuantity" : "REAL",
          "Turnover" : "REAL",
          "NumberOfTrades" : "REAL",
          "DeliverableQty" : "REAL",
          "PercentageDlyQtToTradedQty" : "REAL"}

  bseEqDB.CreateTable("TATAMOTORS", headerDict)
  rowData = "sanchay"
  bseEqDB.AddRow("TATAMOTORS", headerDict, rowData)
  dbMgr.ExportDB("BSE_EQ", "STDOUT")

if ( __name__ == "__main__") :
  main()
