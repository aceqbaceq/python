#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def training ( initial_training_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def training'  deletes  rows in `training` table using 'initial_training_id'
#  'initial_training_id' specifies (training_id)  row in `training` table we want to delete
#

  if (
          initial_training_id    is None
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
  # step 1 |  training (training_id)
  #
  A_table = "training"
  query = ("SELECT SQL_NO_CACHE training_id   FROM `%s` WHERE training_id=%%s ORDER BY training_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_training_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "training_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'training_id' is not found, please specify another 'initial_training_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `training`, training_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current training_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""






  #
  # step 2 | training_employee (training_id)
  #
  A_table = "training_employee"
  query = ("SELECT SQL_NO_CACHE training_id FROM `%s` WHERE  training_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where training_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()









  # FINAL STEPS

  #
  #  step 7 | training (training_id)
  #
  #print "table `training` has training_id=",d
  #print "table `training` , trying to delete training_id =  (%s)" % (d)
  query = ("delete from  `training` where training_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `training`, training_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `training`, (training_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


