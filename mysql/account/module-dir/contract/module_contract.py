#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored
# module invoice
sys.path.append('../invoice')
import module_invoice



def contract ( initial_contract_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def contract'  deletes  rows in `contract` table using 'initial_contract_id'
#  'initial_contract_id' specifies (contract_id)  row in `contract` table we want to delete
#

  if (
          initial_contract_id    is None
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
  # step 1 |  contract (contract_id)
  #
  A_table = "contract"
  query = ("SELECT contract_id   FROM `%s` WHERE contract_id=%%s ORDER BY contract_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_contract_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "contract_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'contract_id' is not found, please specify another 'initial_contract_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `contract`, contract_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current contract_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""







  #
  # step 2 |  invoice (invoice_id, contract_id) 
  #
  A_table = "invoice"
  query = ("SELECT invoice_id  FROM `%s` WHERE  contract_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_invoice.invoice(  initial_invoice_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )









  #
  #  step 7 | contract (contract_id)
  #
  #print "table `contract` has contract_id=",d
  #print "table `contract` , trying to delete contract_id =  (%s)" % (d)
  query = ("delete from  `contract` where contract_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `contract`, contract_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `contract`, (contract_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


