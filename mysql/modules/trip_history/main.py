#!/usr/bin/python

import sys
import module_trip_history


module_trip_history.trip_history(  initial_revision_id=466,
                         DB_Host="localhost",
                         DB_User="root",
                         DB_Password="rootpass",
                         DB_Name="db",
                         DB_Port="3308" )






