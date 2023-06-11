#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def vacancy ( initial_vacancy_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def vacancy'  deletes  rows in `vacancy` table using 'initial_vacancy_id'
#  'initial_vacancy_id' specifies (vacancy_id)  row in `vacancy` table we want to delete
#

  if (
          initial_vacancy_id    is None
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
  # step 1 |  vacancy (vacancy_id)
  #
  A_table = "vacancy"
  query = ("SELECT SQL_NO_CACHE vacancy_id   FROM `%s` WHERE vacancy_id=%%s ORDER BY vacancy_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_vacancy_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "vacancy_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'vacancy_id' is not found, please specify another 'initial_vacancy_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `vacancy`, vacancy_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current vacancy_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | vacancy_contact (vacancy_id)
  #
  A_table = "vacancy_contact"
  query = ("SELECT SQL_NO_CACHE vacancy_id FROM `%s` WHERE  vacancy_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where vacancy_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 3 | vacancy_history (vacancy_id)
  #
  A_table = "vacancy_history"
  query = ("SELECT SQL_NO_CACHE vacancy_id FROM `%s` WHERE  vacancy_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where vacancy_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()










  #
  #  step 7 | vacancy (vacancy_id)
  #
  #print "table `vacancy` has vacancy_id=",d
  #print "table `vacancy` , trying to delete vacancy_id =  (%s)" % (d)
  query = ("delete from  `vacancy` where vacancy_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `vacancy`, vacancy_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `vacancy`, (vacancy_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


