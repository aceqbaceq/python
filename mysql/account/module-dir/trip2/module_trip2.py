#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored
# module property
sys.path.append('../property')
import module_property
# module trip_history
sys.path.append('../trip_history')
import module_trip_history
# module waybill
sys.path.append('../waybill')
import module_waybill




def trip2 ( initial_trip_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def trip'  deletes  rows in `trip` table using 'initial_trip_id'
#  'initial_trip' specifies (trip_id)  row in `trip` table we want to delete
#

  if (
          initial_trip_id     is None
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
  # step 1 |  trip (trip_id)
  #
  A_table = "trip"
  query = ("SELECT trip_id   FROM `%s` WHERE trip_id=%%s ORDER BY trip_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_trip_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "trip_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'trip_id' is not found, please specify another 'initial_trip_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `trip`, trip_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current trip_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | category_trip (trip_id)
  #
  A_table = "category_trip"
  query = ("SELECT trip_id FROM `%s` WHERE  trip_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where trip_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 3 | claim_trip (trip_id)
  #
  A_table = "claim_trip"
  query = ("SELECT trip_id FROM `%s` WHERE  trip_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where trip_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()





  #
  # step 4 | point (trip_id)
  #
  A_table = "point"
  query = ("SELECT trip_id FROM `%s` WHERE  trip_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where trip_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()






  #
  # step 5 |  property (trip_id, property_id) 
  #
  A_table = "property"
  query = ("SELECT property_id  FROM `%s` WHERE  trip_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_property.property(  initial_property_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )





  #
  # step 6 | route (trip_id)
  #
  A_table = "route"
  query = ("SELECT trip_id FROM `%s` WHERE  trip_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where trip_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 7 | shipping_firm_price  (trip_id)
  #
  A_table = "shipping_firm_price"
  query = ("SELECT trip_id FROM `%s` WHERE  trip_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where trip_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 8 | trip_contents  (trip_id)
  #
  A_table = "trip_contents"
  query = ("SELECT trip_id FROM `%s` WHERE  trip_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where trip_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()





  #
  # step 9 |  trip_history (trip_id, revision_id) 
  #
  A_table = "trip_history"
  query = ("SELECT revision_id  FROM `%s` WHERE  trip_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_trip_history.trip_history(  initial_revision_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )






  #
  # step 10 | trip_service  (trip_id)
  #
  A_table = "trip_service"
  query = ("SELECT trip_id FROM `%s` WHERE  trip_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where trip_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()






  #
  # step 11 |  waybill (trip_id, waybill_id) 
  #
  A_table = "waybill"
  query = ("SELECT waybill_id  FROM `%s` WHERE  trip_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()
  #print myresult;


  if myresult:
     for x in myresult:
         module_waybill.waybill(  initial_waybill_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )







  #
  # step 12 |  trip (trip_id, parent_id)
  #
  A_table = "trip"
  A_transaction_id = d
  query = ("SELECT parent_id FROM  `%s`  WHERE  parent_id = %%s;")  %(A_table,)
  mycursor.execute(query, (A_transaction_id,))
  A_result = mycursor.fetchall()

  if A_result:
         #print "---------------------------------------"
         for x in A_result:
                 # x[0] is parent_id
                 #print "table `%s` :  (trip_id,parent_id) = (%s,%s)" % (A_table,  A_transaction_id, x[0])
                 query = ("DELETE FROM  %s  WHERE parent_id= %%s;") %(A_table,)
                 mycursor.execute(query, (x[0],))
                 mydb.commit()















  #
  #  step 4 | transaction (transaction_id)
  #
  #print "table `transaction` has transaction_id=",d
  #print "table `transaction` , trying to delete transaction_id =  (%s)" % (d)
  query = ("delete from  `transaction` where transaction_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `transaction`, transaction_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `transaction`, (transaction_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."


  mydb.commit()
  mycursor.close()
  mydb.close()




