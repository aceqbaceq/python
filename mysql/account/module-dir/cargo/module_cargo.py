#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def cargo ( initial_cargo_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def cargo'  deletes  rows in `cargo` table using 'initial_cargo_id'
#  'initial_cargo_id' specifies (cargo_id)  row in `cargo` table we want to delete
#

  if (
          initial_cargo_id    is None
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
  # step 1 |  cargo (cargo_id)
  #
  A_table = "cargo"
  query = ("SELECT cargo_id   FROM `%s` WHERE cargo_id=%%s ORDER BY cargo_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_cargo_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "cargo_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'cargo_id' is not found, please specify another 'initial_cargo_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `cargo`, cargo_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current cargo_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""






  #
  # step 2 | cargo_service (cargo_id)
  #
  A_table = "cargo_service"
  query = ("SELECT cargo_id FROM `%s` WHERE  cargo_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where cargo_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 3 | storage (cargo_id)
  #
  A_table = "storage"
  query = ("SELECT cargo_id FROM `%s` WHERE  cargo_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where cargo_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 4 | storage_service (cargo_id)
  #
  A_table = "storage_service"
  query = ("SELECT cargo_id FROM `%s` WHERE  cargo_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where cargo_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()





  #
  # step 5 |  cargo (cargo_id, parent_cargo_id)
  #
  A_table = "cargo"
  A_transaction_id = d
  query = ("SELECT parent_cargo_id FROM  `%s`  WHERE  parent_cargo_id = %%s;")  %(A_table,)
  mycursor.execute(query, (A_transaction_id,))
  A_result = mycursor.fetchall()

  if A_result:
         #print "---------------------------------------"
         for x in A_result:
                 # x[0] is parent_id
                 #print "table `%s` :  (cargo_id,parent_cargo_id) = (%s,%s)" % (A_table,  A_transaction_id, x[0])
                 query = ("DELETE FROM  %s  WHERE parent_cargo_id= %%s;") %(A_table,)
                 mycursor.execute(query, (x[0],))
                 mydb.commit()







  # FINAL STEPS

  #
  #  step 7 | cargo (cargo_id)
  #
  #print "table `cargo` has cargo_id=",d
  #print "table `cargo` , trying to delete cargo_id =  (%s)" % (d)
  query = ("delete from  `cargo` where cargo_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `cargo`, cargo_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `claim`, (claim_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


