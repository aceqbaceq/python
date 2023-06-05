#!/usr/bin/python

import sys
import module_account

i_min=5000      # min account_id
i_max=106000    # max account_id


i=i_max
while i > i_min:
  module_account.account(  initial_account_id=i,
                         DB_Host="localhost",
                         DB_User="root",
                         DB_Password="rootpass",
                         DB_Name="db",
                         DB_Port="3308" )

  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  from datetime import date
  today = date.today()
  sys.stdout.write("current account_id: %s,   time=%s, date=%s   \r" % (i,current_time,today) )
  sys.stdout.flush()
 

  i -=1

