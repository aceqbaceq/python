#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored
# module claim
sys.path.append('../claim')
import module_claim
# module order
sys.path.append('../order')
import module_order
# module transaction
sys.path.append('../transaction')
import module_transaction
# module trip
sys.path.append('../trip')
import module_trip
# module waybill
sys.path.append('../waybill')
import module_waybill





def invoice ( initial_invoice_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def invoice'  deletes  rows in `invoice` table using 'initial_invoice_id'
#  'initial_invoice_id' specifies (invoice_id)  row in `invoice` table we want to delete
#

  if (
          initial_invoice_id    is None
      or  DB_Host             is None
      or  DB_User             is None
      or  DB_Password         is None
      or  DB_Name             is None 
      or  DB_Port             is None

     ):
      print colored("file %s | ERROR: | one of function arguments  is not defined", 'red') % (__file__)
      return

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
  # step 1 |  invoice (invoice_id)
  #
  A_table = "invoice"
  query = ("SELECT SQL_NO_CACHE invoice_id   FROM `%s` WHERE invoice_id=%%s ORDER BY invoice_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_invoice_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "invoice_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'invoice_id' is not found, please specify another 'initial_invoice_id'. \n ", 'red') % (__file__)
     return

  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `invoice`, invoice_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current invoice_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""





  #
  # step 2 | category_invoice (invoice_id)
  #
  A_table = "category_invoice"
  query = ("SELECT SQL_NO_CACHE invoice_id FROM `%s` WHERE  invoice_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where invoice_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()





  #
  # step 3 |  claim (invoice_id, claim_id) 
  #
  A_table = "claim"
  query = ("SELECT SQL_NO_CACHE claim_id  FROM `%s` WHERE  invoice_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_claim.claim(  initial_claim_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )




  #
  # step 4 | guilty (invoice_id)
  #
  A_table = "guilty"
  query = ("SELECT SQL_NO_CACHE invoice_id FROM `%s` WHERE  invoice_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where invoice_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 5 | invoice_bank_detail (invoice_id)
  #
  A_table = "invoice_bank_detail"
  query = ("SELECT SQL_NO_CACHE invoice_id FROM `%s` WHERE  invoice_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where invoice_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 6 | invoice_confirmation (invoice_id)
  #
  A_table = "invoice_confirmation"
  query = ("SELECT SQL_NO_CACHE invoice_id FROM `%s` WHERE  invoice_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where invoice_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 7 | invoice_edm_event (invoice_id)
  #
  A_table = "invoice_edm_event"
  query = ("SELECT SQL_NO_CACHE invoice_id FROM `%s` WHERE  invoice_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where invoice_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 8 | invoice_post (invoice_id)
  #
  A_table = "invoice_post"
  query = ("SELECT SQL_NO_CACHE invoice_id FROM `%s` WHERE  invoice_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where invoice_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 9 |  order (invoice_id, cash_on_delivery_prepay_invoice_id) 
  #
  A_table = "order"
  query = ("SELECT SQL_NO_CACHE order_id  FROM `%s` WHERE  cash_on_delivery_prepay_invoice_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_order.order(  initial_order_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )




  #
  # step 10 |  order (invoice_id, invoice_id) 
  #
  A_table = "order"
  query = ("SELECT SQL_NO_CACHE order_id  FROM `%s` WHERE  invoice_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_order.order(  initial_order_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )





  #
  # step 11 |  transaction (invoice_id, transaction_id) 
  #
  A_table = "transaction"
  query = ("SELECT SQL_NO_CACHE transaction_id  FROM `%s` WHERE  invoice_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         #print x
         module_transaction.transaction(  initial_transaction_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )







  #
  # step 12 |  trip  (invoice_id, trip_id) 
  #
  A_table = "trip"
  query = ("SELECT SQL_NO_CACHE trip_id  FROM `%s` WHERE  invoice_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         #print x
         module_trip.trip(  initial_trip_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )




  #
  # step 13 |  trip  (trip_id, prepay_invoice_id) 
  #
  A_table = "trip"
  query = ("SELECT SQL_NO_CACHE trip_id  FROM `%s` WHERE  prepay_invoice_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         #print x
         module_trip.trip(  initial_trip_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )







  #
  # step 14 | trip_service (invoice_id)
  #
  A_table = "trip_service"
  query = ("SELECT SQL_NO_CACHE invoice_id FROM `%s` WHERE  invoice_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where invoice_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()






  #
  # step 15 |  waybill  (waybill_id, invoice_id) 
  #
  A_table = "waybill"
  query = ("SELECT SQL_NO_CACHE waybill_id  FROM `%s` WHERE  invoice_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         #print x
         module_waybill.waybill(  initial_waybill_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )














  #
  #  step 7 | invoice (invoice_id)
  #
  #print "table `invoice` has invoice_id=",d
  #print "table `invoice` , trying to delete invoice_id =  (%s)" % (d)
  query = ("delete from  `invoice` where invoice_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `invoice`, invoice_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `invoice`, (invoice_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()



