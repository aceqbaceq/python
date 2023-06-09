#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored
# module claim
sys.path.append('../claim')
import module_claim
# module driver
sys.path.append('../driver')
import module_driver
# module invoice
sys.path.append('../invoice')
import module_invoice
# module order
sys.path.append('../order')
import module_order
# module transaction
sys.path.append('../transaction')
import module_transaction





def account ( initial_account_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def account'  deletes  rows in `account_id` table using 'initial_account_id'
#  'initial_account_id' specifies (account_id)  row in `account` table we want to delete
#

  if (
          initial_account_id  is None
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
  # step 1 |  account (account_id)
  #
  A_table = "account"
  query = ("SELECT SQL_NO_CACHE account_id  FROM `%s` WHERE account_id=%%s ORDER BY account_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_account_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "account_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'account_id' is not found, please specify another 'initial_account_id'. \n or doc_date = NULL ", 'red') % (__file__)
     return

  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `account`, account_id=%s | START TRANSACTION |" % (d)
      #from datetime import datetime
      #now = datetime.now()
      #current_time = now.strftime("%H:%M:%S")
      #from datetime import date
      #today = date.today()
      #sys.stdout.write("current account_id: %s,   time=%s, date=%s   \r" % (d,current_time,today) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | account_access (account_id)
  #
  A_table = "account_access"
  query = ("SELECT SQL_NO_CACHE account_id FROM `%s` WHERE  account_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where account_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 3 |  bank_detail (identification_account_id) 
  #
  A_table = "bank_detail"
  query = ("SELECT SQL_NO_CACHE bank_detail_id FROM `%s` WHERE  identification_account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where bank_detail_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 4 |  claim (from_account_id) 
  #
  A_table = "claim"
  query = ("SELECT SQL_NO_CACHE claim_id  FROM `%s` WHERE  from_account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print "step 4 | claim (from_account_id) | claim_id = %s " % (myresult)

  if myresult:
     for x in myresult:
         module_claim.claim(  initial_claim_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )




  #
  # step 5 |  claim (to_account_id) 
  #
  A_table = "claim"
  query = ("SELECT SQL_NO_CACHE claim_id  FROM `%s` WHERE  to_account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print "step 5 | claim (to_account_id) | claim_id = %s " % (myresult)

  if myresult:
     for x in myresult:
         module_claim.claim(  initial_claim_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )



  #
  # step 6 |  client_uuid (account_id ) 
  #
  A_table = "client_uuid"
  query = ("SELECT SQL_NO_CACHE account_id  FROM `%s` WHERE  account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where account_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 7 |  contract_uuid (account_id)
  #
  A_table = "contract_uuid"
  query = ("SELECT SQL_NO_CACHE account_id  FROM `%s` WHERE  account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where account_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()








  #
  # step 8 |  driver (account_id, default_account_id) 
  #
  A_table = "driver"
  query = ("SELECT SQL_NO_CACHE driver_id  FROM `%s` WHERE  default_account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         module_driver.driver(  initial_driver_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )






  #
  # step 9 |  guilty (account_id)
  #
  A_table = "guilty"
  query = ("SELECT SQL_NO_CACHE account_id  FROM `%s` WHERE  account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where account_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 10 |  guilty_reduction (account_id)
  #
  A_table = "guilty_reduction"
  query = ("SELECT SQL_NO_CACHE account_id  FROM `%s` WHERE  account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where account_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()







  #
  # step 11 |  invoice (invoice_id, from_account_id) 
  #
  A_table = "invoice"
  query = ("SELECT SQL_NO_CACHE invoice_id  FROM `%s` WHERE  from_account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         module_invoice.invoice(  initial_invoice_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )




  #
  # step 12 |  invoice (invoice_id, to_account_id) 
  #
  A_table = "invoice"
  query = ("SELECT SQL_NO_CACHE invoice_id  FROM `%s` WHERE  to_account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         module_invoice.invoice(  initial_invoice_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )






  #
  # step 13 |  order (order_id, account_id) 
  #
  A_table = "order"
  query = ("SELECT SQL_NO_CACHE order_id  FROM `%s` WHERE  account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         module_order.order(  initial_order_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )





  #
  # step 14 |  order (order_id, main_account_id) 
  #
  A_table = "order"
  query = ("SELECT SQL_NO_CACHE order_id  FROM `%s` WHERE  main_account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         module_order.order(  initial_order_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )




  #
  # step 15 |  transaction (transaction_id, account_id) 
  #
  A_table = "transaction"
  query = ("SELECT SQL_NO_CACHE transaction_id  FROM `%s` WHERE  account_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         module_transaction.transaction(  initial_transaction_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )




















  #
  #  step 10 | account (account_id)
  #
  #print "account has account_id=",d
  #print "table `account` , trying to delete account_id =  (%s)" % (d)
  query = ("delete from  `account` where account_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `account`, account_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table account, (account_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"


#  print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


