#!/usr/bin/python

import sys
import module_payment_gateway


module_payment_gateway.payment_gateway(  initial_payment_gateway_id=115,
                         DB_Host="localhost",
                         DB_User="root",
                         DB_Password="rootpass",
                         DB_Name="db2",
                         DB_Port="330" )






