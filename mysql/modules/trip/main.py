#!/usr/bin/python

import sys
import module_trip



i = 100
while i < 200:
   module_trip.trip(  initial_trip_id=i,
                         DB_Host="localhost",
                         DB_User="root",
                         DB_Password="rootpass",
                         DB_Name="db",
                         DB_Port="3308" )


   i += 1
