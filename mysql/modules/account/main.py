#!/usr/bin/python

import sys
import module_account
import datetime
import mysql.connector
import collections
import os.path
from settings import *


#
# set inital variabes
#

i_min=50000             # min account_id
module_name = "main"
DB_Host="localhost"
DB_User="root"
DB_Password="rootpass"
DB_Name="db2"
DB_Port="3306"
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
# step 1 |  account (account_id)
#
# 
A_table = "account"
d = i_max # i_max is read via config file
query = ("SELECT SQL_NO_CACHE account_id  FROM `%s` where account_id = %%s limit 1;")  %(A_table,)
mycursor.execute(query,(d,))
myresult = mycursor.fetchall()

if myresult:
   i_max = myresult [0][0]
else:
     print colored("file %s | ERROR: | 'account_id' is not found, please specify another 'account_id'. \n", 'red') % (__file__)
     sys.exit(1)







#
# step 2 | launch loop
#


i=i_max
while i >= i_min:

  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  from datetime import date
  today = date.today()
  sys.stdout.write("current account_id: %s,   time=%s, date=%s   \r" % (i,current_time,today) )
  sys.stdout.flush()



  m = module_account.account(  initial_account_id=i,
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
  if m == 10:
    print " module %s | module account returned error \"payment gateway detected\" | skip account_id = %s " % (module_name, i)
  i -=1
  # write new i_max to config file
  f = open('%s' % path, 'w')      # open config file
  f.write("i_max = %s" % i)       # write i  as i_max to config file
  f.close()                       # close config file



print ""
