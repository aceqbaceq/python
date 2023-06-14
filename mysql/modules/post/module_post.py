#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def post ( initial_post_id=None, 
            sql_step = None,
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
          initial_post_id     is None
      or  sql_step            is None
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
  #  step 1 | post (post_id)
  #
  A_table = "post"
  #print "table `post` has post_id=",d
  #print "table `post` , trying to delete post_id =  (%s)" % (d)
  t_max = initial_post_id
  t_min = t_max
  t_min -= sql_step
  query = ("delete from  `%s` where post_id >=  %%s  and post_id <= %%s")  %(A_table,)
  mycursor.execute(query, (t_min,t_max))
  mydb.commit()
  #print "table `post`, post_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
  #print "\n"








  # FINAL STEPS



  # print stats
  #mydb.commit()
  # print current time
  #from datetime import datetime
  #now = datetime.now()
  #current_time = now.strftime("%H:%M:%S")
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


