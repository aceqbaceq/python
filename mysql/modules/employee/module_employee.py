#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored

# module order
sys.path.append('../order')
import module_order

# module property
sys.path.append('../property')
import module_property

# module vacancy
sys.path.append('../vacancy')
import module_vacancy

# module driver
sys.path.append('../driver')
import module_driver



#   recursion level. check if we are inside recursion
invcount = 0



def employee ( initial_employee_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def employee'  deletes  rows in `employee` table using 'initial_employee_id'
#  'initial_employee_id' specifies (employee_id)  row in `employee` table we want to delete
#

  # recursion staff
  global invcount

  if (
          initial_employee_id    is None
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
  #print "enter into module employee"

  #
  # step 1 |  employee (employee_id)
  #
  A_table = "employee"
  query = ("SELECT SQL_NO_CACHE employee_id   FROM `%s` WHERE employee_id=%%s ORDER BY employee_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_employee_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "employee_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'employee_id' is not found, please specify another 'initial_employee_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `employee`, employee_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current employee_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 1.5 |  driver (driver_id, size_check_employee_id) 
  #
  A_table = "driver"
  query = ("SELECT SQL_NO_CACHE      driver_id       FROM `%s` WHERE     size_check_employee_id    = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "\n i am going to delete from table `%s`, driver_id=%s \n" %(A_table,x[0])
         module_driver.driver(  initial_driver_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)







  #
  # step 2 | driver_history (size_check_employee_id) 
  #
  A_table = "driver_history"
  query = ("SELECT SQL_NO_CACHE size_check_employee_id FROM `%s` WHERE  size_check_employee_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where size_check_employee_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 3| invoice_confirmation (employee_id)
  #
  A_table = "invoice_confirmation"
  query = ("SELECT SQL_NO_CACHE   employee_id  FROM `%s` WHERE  employee_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where employee_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()





  #
  # step 4 |  order (order_id, from_employee_id) 
  #
  A_table = "order"
  #print "module employee | enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE order_id  FROM `%s` WHERE  from_employee_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     verbose_lines = 100
     len_myresult=len(myresult)
     order_left=len_myresult
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_order.order(  initial_order_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)
         if len_myresult > verbose_lines:
           # calculate how many rows left to delete
           if order_left==len_myresult:
              print ""
           order_left -= 1
           from datetime import datetime
           now = datetime.now()
           current_time = now.strftime("%H:%M:%S")
           from datetime import date
           today = date.today()
           sys.stdout.write("current employee_id: %s,   time=%s, date=%s   ,order to delete: %s \r" % (d,current_time,today,order_left) )
           sys.stdout.flush()
     if len_myresult > verbose_lines:
        print ""
  #print "module employee | exit step with %s table" %(A_table)




  #
  # step 5 |  order (order_id, to_employee_id) 
  #
  A_table = "order"
  #print "module employee | enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE order_id  FROM `%s` WHERE  to_employee_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     verbose_lines = 100
     len_myresult=len(myresult)
     order_left=len_myresult
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_order.order(  initial_order_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)
         if len_myresult > verbose_lines:
           # calculate how many rows left to delete
           if order_left==len_myresult:
              print ""
           order_left -= 1
           from datetime import datetime
           now = datetime.now()
           current_time = now.strftime("%H:%M:%S")
           from datetime import date
           today = date.today()
           sys.stdout.write("current employee_id: %s,   time=%s, date=%s   ,order to delete: %s \r" % (d,current_time,today,order_left) )
           sys.stdout.flush()
     if len_myresult > verbose_lines:
        print ""
  #print "module employee | exit step with %s table" %(A_table)





  #
  # step 6 | post_access (employee_id)
  #
  A_table = "post_access"
  query = ("SELECT SQL_NO_CACHE   employee_id  FROM `%s` WHERE  employee_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where employee_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()







  #
  # step 7 |  property (property_id, employee_id) 
  #
  A_table = "property"
  query = ("SELECT SQL_NO_CACHE   property_id  FROM `%s` WHERE  employee_id = %%s;")  %(A_table)
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
  # step 8 |  vacancy (vacancy_id, executor_id)
  #
  A_table = "vacancy"
  query = ("SELECT SQL_NO_CACHE   vacancy_id  FROM `%s` WHERE  executor_id = %%s;")  %(A_table)
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
  # step 9 |  employee (employee_id, claim_confirm_employee_id)  | warning recursion launch
  #
  A_table = "employee"
  #print "module employee | enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE   employee_id  FROM `%s` WHERE      claim_confirm_employee_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     print "invcount = %s" %(invcount)
     invcount += 1         # set flag that we are going to dive into recusrsion loop
     if invcount == 2:     # condition when we exit from recursion loop
        invcount = 1
        return              
     for x in myresult:
         employee(  initial_employee_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
     invcount = 0
  #print "module employee | exit step with %s table" %(A_table)






  #
  # step 9.5 |  employee (employee_id, external_invoice_confirm_employee_id)   | warning recursion launch
  #
  A_table = "employee"
  #print "module employee | enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE   employee_id  FROM `%s` WHERE      external_invoice_confirm_employee_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     print "invcount = %s" %(invcount)
     invcount += 1         # set flag that we are going to dive into recusrsion loop
     if invcount == 2:     # condition when we exit from recursion loop
        invcount = 1
        return              
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         employee(  initial_employee_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)
     invcount = 0
  #print "module employee | exit step with %s table" %(A_table)






  #
  # step 10 |  employee (employee_id, main_curator_employee_id)     | warning recursion launch
  #
  A_table = "employee"
  query = ("SELECT SQL_NO_CACHE   employee_id  FROM `%s` WHERE      main_curator_employee_id  = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     print "invcount = %s" %(invcount)
     invcount += 1         # set flag that we are going to dive into recusrsion loop
     if invcount == 2:     # condition when we exit from recursion loop
        invcount = 1
        return              
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         employee(  initial_employee_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
     invcount = 0
         #print "delete from table `%s` is succeded" %(A_table)











  #
  #  step 11 | employee (employee_id)
  #
  #print "table `employee` has employee_id=",d
  #print "table `employee` , trying to delete employee_id =  (%s)" % (d)
  query = ("delete from  `employee` where employee_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `employee`, employee_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `employee`, (employee_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()

  #print "exit from module employee"
