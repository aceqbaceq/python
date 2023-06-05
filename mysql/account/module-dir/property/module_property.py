#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored
# module cargo
sys.path.append('../cargo')
import module_cargo


def property ( initial_property_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def property'  deletes  rows in `property` table using 'initial_property_id'
#  'initial_property_id' specifies (property_id)  row in `property` table we want to delete
#

  if (
          initial_property_id is None
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
  # step 1 |  property (property_id)
  #
  A_table = "property"
  query = ("SELECT property_id   FROM `%s` WHERE property_id=%%s ORDER BY property_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_property_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "property_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'property_id' is not found, please specify another 'initial_property_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `property`, property_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current property_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""






  #
  # step 2 |  cargo (property_id, cargo_id) 
  #
  A_table = "cargo"
  query = ("SELECT cargo_id  FROM `%s` WHERE  property_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         module_cargo.cargo(  initial_cargo_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )






  #
  # step 3 | category_property (property_id)
  #
  A_table = "category_property"
  query = ("SELECT property_id FROM `%s` WHERE  property_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where property_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()





  #
  # step 4 | property_employee (property_id)
  #
  A_table = "property_employee"
  query = ("SELECT property_id FROM `%s` WHERE  property_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where property_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
















  # FINAL STEPS

  #  step 7 | property (property_id)
  #
  #print "table `property` has property_id=",d
  #print "table `property` , trying to delete property_id =  (%s)" % (d)
  query = ("delete from  `property` where property_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `property`, property_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `property`, (property_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


