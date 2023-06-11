#!/usr/bin/python

import sys
import module_post

i_min=30000        # min post_id
i_max=1563409    # max post_id


i=i_max
while i > i_min:
  module_post.post(  initial_post_id=i,
                         DB_Host="localhost",
                         DB_User="root",
                         DB_Password="rootpass",
                         DB_Name="db2",
                         DB_Port="3306" )

  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  from datetime import date
  today = date.today()
  sys.stdout.write("current post_id: %s,   time=%s, date=%s   \r" % (i,current_time,today) )
  sys.stdout.flush()
 

  i -=1
