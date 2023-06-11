#!/usr/bin/python

import sys
import module_client
import datetime
import mysql.connector


#
# set inital variabes
#

i_min=50000             # min client_id
DB_Host="localhost"
DB_User="root"
DB_Password="rootpass"
DB_Name="db2"
DB_Port="3306"






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
# find max(client_id)
A_table = "client"
query = ("SELECT SQL_NO_CACHE max(client_id)  FROM `%s`;")  %(A_table,)
mycursor.execute(query,)
myresult = mycursor.fetchall()

l = 0     
for x in myresult:
   l = len(myresult)
if l == 0:
   print colored("file %s | ERROR: | 'client_id' is not found, please specify another 'initial_client_id'. \n or doc_date = NULL ", 'red') % (__file__)
   sys.exit(1)

else: 
  i_max=x[0]




#
# step 2 | launch loop
#

i=i_max
while i >= i_min:
  #i=2154250;
  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  from datetime import date
  today = date.today()
  sys.stdout.write("current client_id: %s,   time=%s, date=%s   \r" % (i,current_time,today) )
  sys.stdout.flush()


  module_client.client(  initial_client_id=i,
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
 
  i -=1


print ""
