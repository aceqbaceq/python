#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def waybill ( initial_waybill_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def waybill'  deletes  rows in `waybill` table using 'initial_waybill_id'
#  'initial_waybill_id' specifies (waybill_id)  row in `waybill` table we want to delete
#

  if (
          initial_waybill_id    is None
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
  # step 1 |  waybill (waybill_id)
  #
  A_table = "waybill"
  query = ("SELECT waybill_id   FROM `%s` WHERE waybill_id=%%s ORDER BY waybill_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_waybill_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "waybill_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'waybill_id' is not found, please specify another 'initial_waybill_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `waybill`, waybill_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current waybill_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | category_waybill (waybill_id)
  #
  A_table = "category_waybill"
  query = ("SELECT waybill_id FROM `%s` WHERE  waybill_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where waybill_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 3 | order_profit (waybill_id)
  #
  A_table = "order_profit"
  query = ("SELECT waybill_id FROM `%s` WHERE  waybill_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where waybill_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 4 | storage_service (draw_waybill_id)
  #
  A_table = "storage_service"
  query = ("SELECT draw_waybill_id FROM `%s` WHERE  draw_waybill_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where draw_waybill_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 5 | storage_service (waybill_id) (one more column)
  #
  A_table = "storage_service"
  query = ("SELECT waybill_id FROM `%s` WHERE  waybill_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where waybill_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 5 | trip_contents (waybill_id) (one more column)
  #
  A_table = "trip_contents"
  query = ("SELECT waybill_id FROM `%s` WHERE  waybill_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where waybill_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()






  #
  # step 6 |  waybill (waybill_id, parent_waybill_id)
  #
  A_table = "waybill"
  A_transaction_id = d
  query = ("SELECT parent_waybill_id FROM  `%s`  WHERE  parent_waybill_id = %%s;")  %(A_table,)
  mycursor.execute(query, (A_transaction_id,))
  A_result = mycursor.fetchall()

  if A_result:
         #print "---------------------------------------"
         for x in A_result:
                 # x[0] is parent_id
                 #print "table `%s` :  (waybill_id,parent_waybill_id) = (%s,%s)" % (A_table,  A_transaction_id, x[0])
                 query = ("DELETE FROM  %s  WHERE parent_waybill_id= %%s;") %(A_table,)
                 mycursor.execute(query, (x[0],))
                 mydb.commit()
















  #
  #  step 7 | waybill (waybill_id)
  #
  #print "table `waybill` has waybill_id=",d
  #print "table `waybill` , trying to delete waybill_id =  (%s)" % (d)
  query = ("delete from  `waybill` where waybill_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `waybill`, waybill_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `waybill`, (waybill_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."


  mydb.commit()
  mycursor.close()
  mydb.close()


