#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored
# module contract
sys.path.append('../contract')
import module_contract
# module trip
sys.path.append('../trip')
import module_trip



def driver ( initial_driver_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def driver'  deletes  rows in `driver` table using 'initial_driver_id'
#  'initial_driver_id' specifies (driver_id)  row in `driver` table we want to delete
#

  if (
          initial_driver_id    is None
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
  # step 1 |  driver (driver_id)
  #
  A_table = "driver"
  query = ("SELECT SQL_NO_CACHE driver_id   FROM `%s` WHERE driver_id=%%s ORDER BY driver_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_driver_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "driver_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'driver_id' is not found, please specify another 'initial_driver_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `driver`, driver_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current driver_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | category_driver (driver_id)
  #
  A_table = "category_driver"
  query = ("SELECT SQL_NO_CACHE driver_id FROM `%s` WHERE  driver_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where driver_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()







  #
  # step 3 |  contract (contract_id, driver_id) 
  #
  A_table = "contract"
  query = ("SELECT SQL_NO_CACHE contract_id  FROM `%s` WHERE  driver_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_contract.contract(  initial_contract_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )







  #
  # step 4 | driver_firm_history (driver_id)
  #
  A_table = "driver_firm_history"
  query = ("SELECT SQL_NO_CACHE driver_id FROM `%s` WHERE  driver_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where driver_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 5 | driver_history (driver_id)
  #
  A_table = "driver_history"
  query = ("SELECT SQL_NO_CACHE driver_id FROM `%s` WHERE  driver_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where driver_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 6 | driver_mailing (driver_id)
  #
  A_table = "driver_mailing"
  query = ("SELECT SQL_NO_CACHE driver_id FROM `%s` WHERE  driver_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where driver_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()






  #
  # step 7 |  trip (trip_id, driver_id) 
  #
  A_table = "trip"
  query = ("SELECT SQL_NO_CACHE trip_id  FROM `%s` WHERE  driver_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_trip.trip(  initial_trip_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )









  #
  #  step 7 | driver (driver_id)
  #
  #print "table `driver` has driver_id=",d
  #print "table `driver` , trying to delete driver_id =  (%s)" % (d)
  query = ("delete from  `driver` where driver_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `driver`, driver_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `driver`, (driver_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


