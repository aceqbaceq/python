#!/usr/bin/python

import sys
import module_client
import datetime
import mysql.connector
import os.path
from termcolor import colored
from settings import *


#
# set inital variabes
#

i_min=50000             # min client_id
sql_step = 100000
DB_Host="localhost"
DB_User="root"
DB_Password="rootpass"
DB_Name="db2"
DB_Port="3306"
module_name = "main"
suffix = "/settings.py"   # config file name



#
# Step -1
#
current_dir = os.getcwd()
path = current_dir
path += suffix
print "settings file path = %s" % (path)





#
# Step 0 | set mysql connection
#

mydb = mysql.connector.connect(
                                host = DB_Host,
                                user = DB_User,
                                password = DB_Password,
                                database = DB_Name,
                                port = DB_Port
                              )


mycursor = mydb.cursor()



#
# step 1 |  client (client_id)
#
# 
myresult=[]
while not myresult:     # we cycle inside loop until find client_id in the table or reach i_min
  A_table = "client"
  t_min = i_max
  t_min -= sql_step
  t_max = i_max
  query = ("SELECT SQL_NO_CACHE client_id  FROM `%s` where client_id >=  %%s    and client_id <= %%s limit 1;")  %(A_table,)
  mycursor.execute(query,(t_min,i_max))  # i_max is read via config file
  myresult = mycursor.fetchall()

  if not myresult:      # if  client_id = i_max is not found in `client` table we print error message
     print colored("file %s | ERROR: | 'client_id' = %s  is not found,  i will try 'client_id=client_id - 1'   \n", 'red') % (__file__, i_max)    

  i_max -= sql_step # decrease i_max
  if i_max <= i_min:    # if i_max <= i_min we exit from module
     print colored("file %s | ERROR: | 'client_id' is less than i_min = %s, please specify another 'client_id'. \n", 'red') % (__file__, i_min)
     sys.exit(1)


print colored("file %s | SUCCESS: | 'client_id' = %s  is found,  continue to process   \n", 'green') % (__file__, i_max)










#
# step 2 | launch loop
#

i=i_max

# 1  <============================================================
while i >= i_min:

  #
  # substep 2.1 |  client (client_id)
  #
  A_table = "client"
  t_min=i
  t_min -= sql_step
  t_max = i
  query = ("SELECT SQL_NO_CACHE    client_id  FROM `%s` where   client_id >= %%s    AND   client_id <= %%s   ORDER BY  client_id DESC;")  %(A_table,)
  mycursor.execute(query,(t_min,t_max))
  myresult = mycursor.fetchall()

  # 2 <===============================
  if myresult:
    # 3 <=====================
    for x in myresult:
      from datetime import datetime
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      from datetime import date
      today = date.today()
      sys.stdout.write("current client_id: %s,   time=%s, date=%s   \r" % (x[0],current_time,today) )
      sys.stdout.flush()

      m = module_client.client(  initial_client_id=x[0],
                             DB_Host=DB_Host,
                             DB_User=DB_User,
                             DB_Password=DB_Password,
                             DB_Name=DB_Name,
                             DB_Port=DB_Port )
      if m == 10:
         print " module %s | submodule client returned error \"payment gateway detected\" | skip client_id = %s " % (module_name, x[0])
      # 3 <===================
  # 2 < ==============================

  i -=sql_step
  # write new i_max to config file
  f = open('%s' % path, 'w')      # open config file
  f.write("i_max = %s" % i)       # write i  as i_max to config file
  f.close()                       # close config file
  # 1 <======================================================================




print ""

