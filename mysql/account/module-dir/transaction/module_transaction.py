#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def transaction ( initial_transaction_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def transaction'  deletes  rows in `transaction` table using 'initial_transaction_id'
#  'initial_transaction_id' specifies (transaction_id)  row in `transaction` table we want to delete
#

  if (
          initial_transaction_id    is None
      or  DB_Host             is None
      or  DB_User             is None
      or  DB_Password         is None
      or  DB_Name             is None 
      or  DB_Port             is None

     ):
      print colored("file %s | ERROR: | one of function arguments  is not defined", 'red') % (__file__)
      sys.ext(1)

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
  # step 1 |  transaction (transaction_id)
  #
  A_table = "transaction"
  query = ("SELECT SQL_NO_CACHE transaction_id   FROM `%s` WHERE transaction_id=%%s ORDER BY transaction_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_transaction_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "transaction_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'transaction_id' is not found, please specify another 'initial_transaction_id'. \n ", 'red') % (__file__)
     return


  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `transaction`, transaction_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current transaction_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | acquiring_response (transaction_id)
  #
  A_table = "acquiring_response"
  query = ("SELECT SQL_NO_CACHE transaction_id FROM `%s` WHERE  transaction_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where transaction_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 2 | payment_gateway_registry (transaction_id)
  #
  A_table = "payment_gateway_registry"
  query = ("SELECT SQL_NO_CACHE transaction_id FROM `%s` WHERE  transaction_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where transaction_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()





  #
  # step 3 |  transaction (transaction_id, parent_id)
  #
  A_table = "transaction"
  A_transaction_id = d
  query = ("SELECT SQL_NO_CACHE parent_id FROM  `%s`  WHERE  parent_id = %%s;")  %(A_table,)
  mycursor.execute(query, (A_transaction_id,))
  A_result = mycursor.fetchall()

  if A_result:
         #print "---------------------------------------"
         for x in A_result:
                 # x[0] is parent_id
                 #print "table `%s` :  (transaction_id,parent_id) = (%s,%s)" % (A_table,  A_transaction_id, x[0])
                 query = ("DELETE FROM  %s  WHERE parent_id= %%s;") %(A_table,)
                 mycursor.execute(query, (x[0],))
                 mydb.commit()








  #
  #  step 4 | transaction (transaction_id)
  #
  #print "table `transaction` has transaction_id=",d
  #print "table `transaction` , trying to delete transaction_id =  (%s)" % (d)
  query = ("delete from  `transaction` where transaction_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `transaction`, transaction_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `transaction`, (transaction_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()



