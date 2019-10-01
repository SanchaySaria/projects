#!/usr/local/bin/python

import sys
sys.path.append('/Users/sanchaysaria/work/financial_analysis/src/pybase/pylib/')
sys.path.append('/Users/sanchaysaria/work/financial_analysis/src/pybase/abstractDB/')

import common
import logging
import sqlite3
import abstractDB

logging.basicConfig(level=logging.DEBUG)

def main() :
  print "Starting program"

if ( __name__ == "__main__") :
  main()

