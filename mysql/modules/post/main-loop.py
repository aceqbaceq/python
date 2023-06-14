#!/usr/bin/python

import sys
import module_post
import datetime
import os.path
from termcolor import colored
from settings import *


#
# set inital variabes
#

module_name = "post"
i_min=100000             # min post_id
sql_step = 40000
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
# step 1 | launch loop
#

i=i_max

while i >= i_min:

  #
  # substep 1.1 |  post (post_id)
  #
  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  from datetime import date
  today = date.today()
  sys.stdout.write("current post_id: %s,   time=%s, date=%s   \r" % (i,current_time,today) )
  sys.stdout.flush()

  m = module_post.post(      initial_post_id=i,
                             sql_step = sql_step,
                             DB_Host=DB_Host,
                             DB_User=DB_User,
                             DB_Password=DB_Password,
                             DB_Name=DB_Name,
                             DB_Port=DB_Port )

  i -=sql_step
  # write new i_max to config file
  f = open('%s' % path, 'w')      # open config file
  f.write("i_max = %s" % i)       # write i  as i_max to config file
  f.close()                       # close config file





