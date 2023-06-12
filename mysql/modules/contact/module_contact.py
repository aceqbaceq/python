#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored

# module claim
sys.path.append('../claim')
import module_claim

# module client
sys.path.append('../client')
import module_client

# module company
sys.path.append('../company')
import module_company

# module driver
sys.path.append('../driver')
import module_driver

# module employee
sys.path.append('../employee')
import module_employee


# module order
sys.path.append('../order')
import module_order

# module person
sys.path.append('../person')
import module_person

# module property
sys.path.append('../property')
import module_property

# module training
sys.path.append('../training')
import module_training

# module vacancy
sys.path.append('../vacancy')
import module_vacancy

# module waybill
sys.path.append('../waybill')
import module_waybill








def contact ( initial_contact_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
           ):

#
#  function description:
#  function 'def contact'  deletes  rows in `contact_id` table using 'initial_contact_id'
#  'initial_contact_id' specifies (contact_id)  row in `contact` table we want to delete
#

  if (
          initial_contact_id  is None
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

    module_name = "contact"



  #
  # step 1 |  contact (contact_id)
  #
  A_table = "contact"
  query = ("SELECT SQL_NO_CACHE contact_id  FROM `%s` WHERE contact_id=%%s ORDER BY contact_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_contact_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "contact_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'contact_id' is not found, please specify another 'initial_contact_id'. \n or doc_date = NULL ", 'red') % (__file__)
     return

  else: 
      d=x[0]
      #d=12334    # for hardcode setting of contact_id uncomment this line
      #print "\n"
      #print "table `contact`, contact_id=%s | START TRANSACTION |" % (d)
      #from datetime import datetime
      #now = datetime.now()
      #current_time = now.strftime("%H:%M:%S")
      #from datetime import date
      #today = date.today()
      #sys.stdout.write("current contact_id: %s,   time=%s, date=%s   \r" % (d,current_time,today) )
      #sys.stdout.flush()
      #print ""





  #
  # step 2 |  claim  (claim_id, problem_contact_id) 
  #
  A_table = "claim"
  query = ("SELECT SQL_NO_CACHE   claim_id     FROM `%s` WHERE    problem_contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_claim.claim(  initial_claim_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)








  #
  # step 3 |  client  (client_id, contact_id) 
  #
  A_table = "client"
  query = ("SELECT SQL_NO_CACHE   client_id     FROM `%s` WHERE    contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_client.client(  initial_client_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)










  #
  # step 4 |  company  (company_id, contact_id) 
  #
  A_table = "company"
  query = ("SELECT SQL_NO_CACHE   company_id     FROM `%s` WHERE    contact_id   = %%s;")  %(A_table)
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
  # step 5 |  driver  (driver_id, default_storehouse_id) 
  #
  A_table = "driver"
  query = ("SELECT SQL_NO_CACHE   driver_id     FROM `%s` WHERE    default_storehouse_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_driver.driver(  initial_driver_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)








  #
  # step 6 |  employee  (employee_id, contact_id) 
  #
  A_table = "employee"
  query = ("SELECT SQL_NO_CACHE   employee_id     FROM `%s` WHERE    contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_employee.employee(  initial_employee_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)






  #
  # step 7 |  employee  (employee_id, office_contact_id) 
  #
  A_table = "employee"
  query = ("SELECT SQL_NO_CACHE   employee_id     FROM `%s` WHERE    office_contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_employee.employee(  initial_employee_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)







  #
  # step 8 |  employee  (employee_id, storehouse_contact_id) 
  #
  A_table = "employee"
  query = ("SELECT SQL_NO_CACHE   employee_id     FROM `%s` WHERE    storehouse_contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_employee.employee(  initial_employee_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)






  #
  # step 9 |  employee_default_group (contact_id)
  #
  A_table = "employee_default_group"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      contact_id      FROM `%s` WHERE      contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)





  #
  # step 10 |  order  (order_id, 'from_contact_id  OR  giveout_storehouse_id  OR  operation_storehouse_id  OR  to_contact_id ') 
  #
  A_table = "order"
  query = ("SELECT SQL_NO_CACHE   order_id     FROM `%s` WHERE   from_contact_id=%%s  OR  giveout_storehouse_id=%%s  OR  operation_storehouse_id=%%s  OR  to_contact_id=%%s ;")  %(A_table)
  mycursor.execute(query, (d,d,d,d))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_order.order(  initial_order_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)







  #
  # step 11 |  person  (person_id, contact_id) 
  #
  A_table = "person"
  query = ("SELECT SQL_NO_CACHE   person_id     FROM `%s` WHERE    contact_id   = %%s;")  %(A_table)
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
  # step 12 |  point (contact_id)
  #
  A_table = "point"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      contact_id      FROM `%s` WHERE      contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  where contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)







  #
  # step 13 |  property  (property_id, contact_id) 
  #
  A_table = "property"
  query = ("SELECT SQL_NO_CACHE   property_id     FROM `%s` WHERE    contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_property.property(  initial_property_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)








  #
  # step 14 |  route (from_contact_id)
  #
  A_table = "route"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      from_contact_id      FROM `%s` WHERE      from_contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  WHERE    from_contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)





  #
  # step 15 |  route (to_contact_id)
  #
  A_table = "route"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      to_contact_id      FROM `%s` WHERE      to_contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  WHERE    to_contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)








  #
  # step 16 |  self_finance_plan (office_id)
  #
  A_table = "self_finance_plan"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      office_id      FROM `%s` WHERE      office_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  WHERE    office_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)








  #
  # step 17 |  training  (training_id, contact_id) 
  #
  A_table = "training"
  query = ("SELECT SQL_NO_CACHE   training_id     FROM `%s` WHERE    contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_training.training(  initial_training_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)









  #
  # step 18 |  trip_contents (from_contact_id)
  #
  A_table = "trip_contents"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      from_contact_id      FROM `%s` WHERE      from_contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  WHERE    from_contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)







  #
  # step 18 |  trip_contents (plan_contact_id)
  #
  A_table = "trip_contents"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      plan_contact_id      FROM `%s` WHERE      plan_contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  WHERE    plan_contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)






  #
  # step 19 |  trip_contents (to_contact_id)
  #
  A_table = "trip_contents"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      to_contact_id      FROM `%s` WHERE      to_contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  WHERE    to_contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)







  #
  # step 20 |  trip_service (contact_id)
  #
  A_table = "trip_service"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      contact_id      FROM `%s` WHERE      contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  WHERE    contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)








  #
  # step 21 |  vacancy  (vacancy_id, contact_id) 
  #
  A_table = "vacancy"
  query = ("SELECT SQL_NO_CACHE   vacancy_id     FROM `%s` WHERE    contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_vacancy.vacancy(  initial_vacancy_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)






  #
  # step 22 |  vacancy_contact (contact_id)
  #
  A_table = "vacancy_contact"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE      contact_id      FROM `%s` WHERE      contact_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "i am going to delete from table `%s`" %(A_table)
     query = ("delete from  `%s`  WHERE    contact_id = %%s")  %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
     #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)






  #
  # step 23 |  waybill  (waybill_id, contact_id) 
  #
  A_table = "waybill"
  query = ("SELECT SQL_NO_CACHE   waybill_id     FROM `%s` WHERE    contact_id   = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_waybill.waybill(  initial_waybill_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)









  # FINAL STEPS
  #print " # FINAL STEPS"

  #
  #  step 22 |  (contact_id)
  #
  A_table = "contact"
  query = ("delete from  `%s`  WHERE    contact_id = %%s")  %(A_table)
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "delete from table `%s` is succeded" %(A_table)










  # print stats
  #mydb.commit()
  # print current time
  #from datetime import datetime
  #now = datetime.now()
  #current_time = now.strftime("%H:%M:%S")
  #print "\n"
  #print "-----------------------------"
  #print "Current Time =", current_time
  #print "table contact, (contact_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"


  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


