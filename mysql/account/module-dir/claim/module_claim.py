#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def claim ( initial_claim_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def claim'  deletes  rows in `claim` table using 'initial_claim_id'
#  'initial_claim_id' specifies (claim_id)  row in `claim` table we want to delete
#

  if (
          initial_claim_id    is None
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
  # step 1 |  claim (claim_id)
  #
  A_table = "claim"
  query = ("SELECT SQL_NO_CACHE claim_id   FROM `%s` WHERE claim_id=%%s ORDER BY claim_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_claim_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "claim_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'claim_id' is not found, please specify another 'initial_claim_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `claim`, claim_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current claim_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | category_claim (claim_id)
  #
  A_table = "category_claim"
  query = ("SELECT SQL_NO_CACHE claim_id FROM `%s` WHERE  claim_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where claim_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 3 | claim_history (claim_id)
  #
  A_table = "claim_history"
  query = ("SELECT SQL_NO_CACHE claim_id FROM `%s` WHERE  claim_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where claim_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 4 | claim_order (claim_id)
  #
  A_table = "claim_order"
  query = ("SELECT SQL_NO_CACHE claim_id FROM `%s` WHERE  claim_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where claim_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 5 | claim_trip (claim_id)
  #
  A_table = "claim_trip"
  query = ("SELECT SQL_NO_CACHE claim_id FROM `%s` WHERE  claim_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where claim_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 6 | guilty (claim_id)
  #
  A_table = "guilty"
  query = ("SELECT SQL_NO_CACHE claim_id FROM `%s` WHERE  claim_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where claim_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()







  #
  #  step 7 | claim (claim_id)
  #
  #print "table `claim` has claim_id=",d
  #print "table `claim` , trying to delete claim_id =  (%s)" % (d)
  query = ("delete from  `claim` where claim_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `claim`, claim_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `claim`, (claim_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


