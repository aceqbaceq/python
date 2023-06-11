#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def post ( initial_post_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def post'  deletes  rows in `post` table using 'initial_post_id'
#  'initial_post_id' specifies (post_id)  row in `post` table we want to delete
#

  if (
          initial_post_id    is None
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
  # step 1 |  post (post_id)
  #
  A_table = "post"
  query = ("SELECT post_id   FROM `%s` WHERE post_id=%%s ORDER BY post_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_post_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "post_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'post_id' is not found, please specify another 'initial_post_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `post`, post_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current post_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""




  #
  # step 2 | category_post (post_id)
  #
  A_table = "category_post"
  query = ("SELECT post_id FROM `%s` WHERE  post_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where post_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 4 | driver_mailing (post_id)
  #
  A_table = "driver_mailing"
  query = ("SELECT post_id FROM `%s` WHERE  post_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where post_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 5 | invoice_post (post_id)
  #
  A_table = "invoice_post"
  query = ("SELECT post_id FROM `%s` WHERE  post_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where post_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 6 | payment (post_id)
  #
  A_table = "payment"
  query = ("SELECT post_id FROM `%s` WHERE  post_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where post_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 7 | person_mailing (post_id)
  #
  A_table = "person_mailing"
  query = ("SELECT post_id FROM `%s` WHERE  post_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where post_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 8 | post_access (post_id)
  #
  A_table = "post_access"
  query = ("SELECT post_id FROM `%s` WHERE  post_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where post_id = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()















  #
  #  step 7 | post (post_id)
  #
  #print "table `post` has post_id=",d
  #print "table `post` , trying to delete post_id =  (%s)" % (d)
  query = ("delete from  `post` where post_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `post`, post_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
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
  #print "table `post`, (post_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


