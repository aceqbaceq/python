#!/usr/bin/python

import sys
import module_invoice


module_invoice.invoice(  initial_invoice_id=1762,
                         DB_Host="localhost",
                         DB_User="root",
                         DB_Password="rootpass",
                         DB_Name="db",
                         DB_Port="3308" )






