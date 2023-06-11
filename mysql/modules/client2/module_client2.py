#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored

# module company
sys.path.append('../company')
import module_company


# module contract
sys.path.append('../contract')
import module_contract

# module payment_gateway
sys.path.append('../payment_gateway')
import module_payment_gateway

# module driver
#sys.path.append('../driver')
#import module_driver


# module person
sys.path.append('../person')
import module_person

# module price_list
sys.path.append('../price_list')
import module_price_list






def client2 ( initial_client2_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
           ):

#
#  function description:
#  function 'def client2'  deletes  rows in `client_id` table using 'initial_client2_id'
#  'initial_client2_id' specifies (client_id)  row in `client` table we want to delete
#

  if (
          initial_client2_id  is None
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
  # step 1 |  client (client_id)
  #
  A_table = "client"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE client_id=%%s ORDER BY client_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_client2_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "client_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'client_id' is not found, please specify another 'initial_client2_id'. \n or doc_date = NULL ", 'red') % (__file__)
     return

  else: 
      d=x[0]
      #d=12334    # for hardcode setting of client_id uncomment this line
      #print "\n"
      #print "table `client`, client_id=%s | START TRANSACTION |" % (d)
      #from datetime import datetime
      #now = datetime.now()
      #current_time = now.strftime("%H:%M:%S")
      #from datetime import date
      #today = date.today()
      #sys.stdout.write("current client_id: %s,   time=%s, date=%s   \r" % (d,current_time,today) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 |  category_client (client_id)
  #
  A_table = "category_client"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)



  #
  # step 3 |  category_client_history (client_id)
  #
  A_table = "category_client_history"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)



  #
  # step 4 |  client_history (client_id)
  #
  A_table = "client_history"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)



  #
  # step 5 |  client_options (client_id)
  #
  A_table = "client_options"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)




  #
  # step 6 |  client_relation_history (child_client_id)
  #
  A_table = "client_relation_history"
  query = ("SELECT SQL_NO_CACHE child_client_id  FROM `%s` WHERE  child_client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where child_client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)




  #
  # step 7 |  client_relation_history (parent_client_id)
  #
  A_table = "client_relation_history"
  query = ("SELECT SQL_NO_CACHE parent_client_id  FROM `%s` WHERE  parent_client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where parent_client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)






  #
  # step 8 |  company (company_id, client_id) 
  #
  A_table = "company"
  #print "module client2 | enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE   company_id    FROM `%s` WHERE  client_id = %%s;")  %(A_table)
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
  #print "module client2 | exit step with %s table" %(A_table)







  #
  # step 9 |  contract (contract_id, client_id) 
  #
  A_table = "contract"
  query = ("SELECT SQL_NO_CACHE contract_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_contract.contract(  initial_contract_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)




  #
  # step 10 |  curator_history (client_id)
  #
  A_table = "curator_history"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)





  #
  # step 10.5 |  driver (driver_id, related_client_id) 
  #
  #A_table = "driver"
  #query = ("SELECT SQL_NO_CACHE    driver_id     FROM `%s` WHERE     related_client_id   = %%s;")  %(A_table)
  #mycursor.execute(query, (d,))
  #myresult = mycursor.fetchall()

  #if myresult:
     #for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         #module_driver.driver(  initial_driver_id=x[0],
                         #DB_Host=DB_Host,
                         #DB_User=DB_User,
                         #DB_Password=DB_Password,
                         #DB_Name=DB_Name,
                         #DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)




  #
  # step 11 |  forwarder (client_id)
  #
  A_table = "forwarder"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)




  #
  # step 12 |  invoice_options (client_id)
  #
  A_table = "invoice_options"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)




  #
  # step 13 |  main_client_relations (client_id)
  #
  A_table = "main_client_relations"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)




  #
  # step 14 |  main_client_relations (main_client_id)
  #
  A_table = "main_client_relations"
  query = ("SELECT SQL_NO_CACHE main_client_id  FROM `%s` WHERE  main_client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where main_client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)





  #
  # step 15 |  order_mark (client_id)
  #
  A_table = "order_mark"
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where client_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)






  #
  # step 16 |  payment_gateway (gateway_id, client_id) 
  #
  A_table = "payment_gateway"
  query = ("SELECT SQL_NO_CACHE   gateway_id      FROM `%s` WHERE    client_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_payment_gateway.payment_gateway(  initial_gateway_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)








  #
  # step 17 |  person (person_id, client_id) 
  #
  A_table = "person"
  query = ("SELECT SQL_NO_CACHE person_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_person.person(  initial_person_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)



  #
  # step 18 |  price_list (price_list_id, client_id) 
  #
  A_table = "price_list"
  query = ("SELECT SQL_NO_CACHE price_list_id  FROM `%s` WHERE  client_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_price_list.price_list(  initial_price_list_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)




  #
  # step 18 | contact (contact_id, client_id)
  #
  A_table = "contact"
  #print "module client2 | enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE contact_id FROM `%s` WHERE  client_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult_contact = mycursor.fetchall()
  #print " step 2 | print client_id = %s, myresult_contact = %s" %(d,myresult_contact)

  if myresult_contact:
     for x in myresult_contact:
        query = ("update `%s` set client_id=null  where contact_id = %%s") %(A_table)
        mycursor.execute(query, (x[0],))
        mydb.commit()
  #print "module client2 | exit step with %s table" %(A_table)








  # FINAL STEPS
  #print " # FINAL STEPS "

  #
  # step 19 | client (client_id)
  #
  A_table = "client"
  #print "module client2 | enter step with %s table"  %(A_table)

  query = ("delete FROM `%s` WHERE  client_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "module client2 | exit step with %s table" %(A_table)




  #
  # step 20 | contact (contact_id)
  #
  #A_table = "contact"
  #for x in myresult_contact:
     #query = ("delete FROM `%s` WHERE  contact_id = %%s;")  %(A_table,)
     #mycursor.execute(query, (x[0],))
     #mydb.commit()








  # print stats
  #mydb.commit()
  # print current time
  #from datetime import datetime
  #now = datetime.now()
  #current_time = now.strftime("%H:%M:%S")
  #print "\n"
  #print "-----------------------------"
  #print "Current Time =", current_time
  #print "table client, (client_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"


  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


