#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored

# module company
sys.path.append('../company')
import module_company

def payment_gateway ( initial_gateway_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def payment_gateway'  deletes  rows in `payment_gateway` table using 'initial_gateway_id'
#  'initial_gateway_id' specifies (gateway_id)  row in `payment_gateway` table we want to delete
#

  if (
          initial_gateway_id    is None
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
  # step 1 |  payment_gateway (gateway_id)
  #
  A_table = "payment_gateway"
  query = ("SELECT SQL_NO_CACHE gateway_id   FROM `%s` WHERE gateway_id=%%s ORDER BY gateway_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_gateway_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "gateway_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'gateway_id' is not found, please specify another 'initial_gateway_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `payment_gateway`, gateway_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current gateway_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""







  #
  # step 2 |  company (company_id, acquiring_gateway_id) 
  #
  A_table = "company"
  query = ("SELECT SQL_NO_CACHE     company_id       FROM `%s` WHERE    acquiring_gateway_id =    %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_company.company(  initial_company_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)









  #
  #  step 7 | payment_gateway (gateway_id)
  #
  #print "table `payment_gateway` has gateway_id=",d
  #print "table `payment_gateway` , trying to delete gateway_id =  (%s)" % (d)
  query = ("delete from  `payment_gateway` where gateway_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `payment_gateway`, gateway_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `payment_gateway`, (gateway_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


