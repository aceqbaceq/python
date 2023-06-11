#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def price_list ( initial_price_list_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def price_list'  deletes  rows in `price_list` table using 'initial_price_list_id'
#  'initial_price_list_id' specifies (price_list_id)  row in `price_list` table we want to delete
#

  if (
          initial_price_list_id    is None
      or  DB_Host             is None
      or  DB_User             is None
      or  DB_Password         is None
      or  DB_Name             is None 
      or  DB_Port             is None

     ):
      print colored("file %s | ERROR: | one of function arguments  is not defined", 'red') % (__file__)
      sys.exit(1)

  else:
    mydb = mysql.connector.connect(
    host = DB_Host,
    user = DB_User,
    password = DB_Password,
    database = DB_Name,
    port = DB_Port
    )
         
    mycursor = mydb.cursor()
         



  #
  # step 1 |  price_list (price_list_id)
  #
  A_table = "price_list"
  query = ("SELECT SQL_NO_CACHE price_list_id   FROM `%s` WHERE price_list_id=%%s ORDER BY price_list_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_price_list_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "price_list_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'price_list_id' is not found, please specify another 'initial_price_list_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `price_list`, price_list_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current price_list_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | price_ (price_list_id)
  #
  A_table = "price"
  query = ("SELECT SQL_NO_CACHE price_list_id FROM `%s` WHERE  price_list_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where price_list_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()










  #
  #  step 7 | price_list (price_list_id)
  #
  #print "table `price_list` has price_list_id=",d
  #print "table `price_list` , trying to delete price_list_id =  (%s)" % (d)
  query = ("delete from  `price_list` where price_list_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `price_list`, price_list_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
  #print "\n"



  # print stats
  mydb.commit()
  # print current time
  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  #print "\n"
  #print "-----------------------------"
  #print "Current Time =", current_time
  #print "table `price_list`, (price_list_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


