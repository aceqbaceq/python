#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def trip_history ( initial_revision_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def trip_history'  deletes  rows in `trip_history` table using 'initial_revision_id'
#  'initial_revision_id' specifies (revision_id)  row in `trip_history` table we want to delete
#

  if (
          initial_revision_id    is None
      or  DB_Host                is None
      or  DB_User                is None
      or  DB_Password            is None
      or  DB_Name                is None 
      or  DB_Port                is None

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
  # step 1 |  trip_history (revision_id)
  #
  A_table = "trip_history"
  query = ("SELECT SQL_NO_CACHE revision_id   FROM `%s` WHERE revision_id=%%s ORDER BY revision_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_revision_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "revision_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'revision_id' is not found, please specify another 'initial_revision_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `trip_history`, revision_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current revision_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | point_history (revision_id)
  #
  A_table = "point_history"
  query = ("SELECT SQL_NO_CACHE revision_id FROM `%s` WHERE  revision_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where revision_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 3 | route_history (revision_id)
  #
  A_table = "route_history"
  query = ("SELECT SQL_NO_CACHE revision_id FROM `%s` WHERE  revision_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where revision_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()












  #
  #  step 7 | trip_history (revision_id)
  #
  #print "table `trip_history` has revision_id=",d
  #print "table `trip_history` , trying to delete revision_id =  (%s)" % (d)
  query = ("delete from  `trip_history` where revision_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `trip_history`, revision_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `trip_history`, (revision_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."



  mydb.commit()
  mycursor.close()
  mydb.close()


