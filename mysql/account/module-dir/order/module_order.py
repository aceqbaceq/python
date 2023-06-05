#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored



def order ( initial_order_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def order'  deletes  rows in `order` table using 'initial_order_id'
#  'initial_order_id' specifies (order_id)  row in `order` table we want to delete
#

  if (
          initial_order_id is None
      or  DB_Host          is None
      or  DB_User          is None
      or  DB_Password      is None
      or  DB_Name          is None 
      or  DB_Port          is None

     ):
      print colored("file %s | ERROR: | one of function arguments  is not defined", 'red') % (__file__)
      sys.exit(1)

  else:
    mydb = mysql.connector.connect(
    host = DB_Host,
    user = DB_User,
    password = DB_Password,
    database = DB_Name,
    port = DB_Port
    )
         
    mycursor = mydb.cursor()
         


    #
    # step 0 | order_id 
    #
    query = ("SELECT order_id  FROM `order` WHERE order_id=%s limit 1")

    mycursor.execute(query, (initial_order_id, ))
    myresult2 = mycursor.fetchall()

    l = 0     
    for x in myresult2:
           l = len(myresult2)
           #print "order_id=",x[0]
           #print "\n"
    if l == 0:
       #print colored("file %s | ERROR: | 'order_id' is not found, please specify another 'initial_order_id'.", 'red') % (__file__)
       return





    #
    # step 1 |  order (order_id)
    #
    query = ("SELECT order_id, date FROM `order` WHERE order_id=%s ORDER BY date ASC LIMIT 1")
    mycursor.execute(query, (initial_order_id, ))
    myresult = mycursor.fetchall()


    for x in myresult:
        d=x[0]
        order_data=x[1]
    #d=12334    # for hardcode setting of order_id uncomment this line
    #print "\n"
    #print "table `order`, order_id=%s | START TRANSACTION |" % (d)
    #sys.stdout.write("current order_id: %s, order data = %s   \r" % (d, order_data) )
    #sys.stdout.flush()



    #
    # step 2 | category_order (order_id)
    #
    query = ("SELECT order_id FROM `category_order` WHERE  order_id = %s limit 1;")
    mycursor.execute(query, (d,))
    myresult = mycursor.fetchall()

    if myresult:
       query = ("delete from  category_order where order_id = %s")
       mycursor.execute(query, (d,))
       mydb.commit()



    #
    # step 3 |  claim_order (order_id)
    #
    query = ("SELECT order_id FROM `claim_order` WHERE  order_id = %s limit 1;")
    mycursor.execute(query, (d,))
    myresult = mycursor.fetchall()

    if myresult:
       query = ("delete from  claim_order  where order_id = %s")
       mycursor.execute(query, (d,))
       mydb.commit()



    #
    # step 4 |  order_profit (order_id)
    #
    query = ("SELECT order_id FROM `order_profit` WHERE  order_id = %s limit 1;")
    mycursor.execute(query, (d,))
    myresult = mycursor.fetchall()

    if myresult:
       query = ("delete from  order_profit  where order_id = %s")
       mycursor.execute(query, (d,))
       mydb.commit()



    #
    # step 5 |  order_profit_options (order_id)
    #
    query = ("SELECT order_id FROM `order_profit_options` WHERE  order_id = %s limit 1;")
    mycursor.execute(query, (d,))
    myresult = mycursor.fetchall()

    if myresult:
       query = ("delete from `order_profit_options`  where order_id = %s")
       mycursor.execute(query, (d,))
       mydb.commit()



    #
    # step 6 | self_finance_status_history (order_id)
    #
    query = ("SELECT order_id FROM `self_finance_status_history` WHERE  order_id = %s limit 1;")
    mycursor.execute(query, (d,))
    myresult = mycursor.fetchall()

    if myresult:
       query = ("delete from `self_finance_status_history`  where order_id = %s")
       mycursor.execute(query, (d,))
       mydb.commit()




    #
    # step 7 | order_mark  (order_id,order_mark_id)
    #

    #
    #  A_table  (order_id,order_mark_id)
    # 
    A_table = "order_mark"                # set help table name
    B_table = "category_order_mark"       # set help table name
    A_order_id = d                        # set order_id  for search

    query = ("SELECT order_id,order_mark_id FROM  `%s`  WHERE  order_id = %%s;")  %(A_table,)
    mycursor.execute(query, (A_order_id,))
    A_result = mycursor.fetchall()

    if A_result:
           # clear B_table and other help tables for order_id and order_mark_id
           #print "---------------------------------------"
           for x in A_result:
                   # x[0] is order_id | x[1] is order_mark_id
                   #print "table %s  (order_id,order_mark_id) = (%s,%s)" % (A_table,x[0],x[1])
                   B_order_mark_id=x[1]

                   #
                   #   B_table  (order_mark_id)
                   #
                   query = ("SELECT order_mark_id FROM %s  WHERE  order_mark_id = %%s limit 1;") %(B_table,)
                   mycursor.execute(query, (B_order_mark_id,))
                   B_result = mycursor.fetchall()

                   if B_result:
                       for y in B_result:
                          #print "y[0]=%s" % (y[0])
                          #print "table %s (order_mark_id) = %s" % (B_table,y[0])
                          query = ("delete from  %s  where order_mark_id = %%s;") %(B_table,)
                          mycursor.execute(query, (y[0],))
                          mydb.commit()

           # clear A_table for order_id 
           query = ("delete from  %s  where order_id = %%s;")  %(A_table,)
           A_order_id=x[0]
           mycursor.execute(query, (A_order_id,))
           mydb.commit()
           #print "---------------------------------------"
      





    #
    # step 8 | waybill  (order_id,waybill_id)
    #

    #
    #  A_table  (order_id,waybill_id)
    # 
    A_table = "waybill"                   # set help table name
    B_table = "category_waybill"          # set help table name
    C_table = "order_profit"              # set help table name
    D_table = "storage_service"           # set help table name
    E_table = "trip_contents"             # set help table name

    A_order_id = d                        # set order_id  for search

    query = ("SELECT order_id,waybill_id FROM  `%s`  WHERE  order_id = %%s;")  %(A_table,)
    mycursor.execute(query, (A_order_id,))
    A_result = mycursor.fetchall()

    if A_result:
           # clear B_table and other help tables for order_id and waybill_id
           #print "---------------------------------------"
           for x in A_result:
                   # x[0] is order_id | x[1] is waybill_id
                   #print "table %s  (order_id,waybill_id) = (%s,%s)" % (A_table,x[0],x[1])

                   #
                   #   B_table  (waybill_id)
                   #
                   B_colum=x[1]
                   query = ("SELECT waybill_id FROM %s  WHERE  waybill_id = %%s limit 1;") %(B_table,)
                   mycursor.execute(query, (B_colum,))
                   B_result = mycursor.fetchall()

                   if B_result:
                       for y in B_result:
                          #print "y[0]=%s" % (y[0])
                          #print "table %s (waybill_id) = %s" % (B_table,y[0])
                          query = ("delete from  %s  where waybill_id = %%s;") %(B_table,)
                          mycursor.execute(query, (y[0],))
                          mydb.commit()

                   #
                   #   C_table  (waybill_id)
                   #
                   C_colum=x[1]
                   query = ("SELECT waybill_id FROM %s  WHERE  waybill_id = %%s limit 1;") %(C_table,)
                   mycursor.execute(query, (C_colum,))
                   C_result = mycursor.fetchall()

                   if C_result:
                       for y in C_result:
                          #print "y[0]=%s" % (y[0])
                          #print "table %s (waybill_id) = %s" % (C_table,y[0])
                          query = ("delete from  %s  where waybill_id = %%s;") %(C_table,)
                          mycursor.execute(query, (y[0],))
                          mydb.commit()


                   #
                   #   D_table  (waybill_id)
                   #
                   D_colum=x[1]
                   query = ("SELECT waybill_id FROM %s  WHERE  waybill_id = %%s limit 1;") %(D_table,)
                   mycursor.execute(query, (D_colum,))
                   D_result = mycursor.fetchall()

                   if D_result:
                       for y in D_result:
                          #print "y[0]=%s" % (y[0])
                          #print "table %s (waybill_id) = %s" % (D_table,y[0])
                          query = ("delete from  %s  where waybill_id = %%s;") %(D_table,)
                          mycursor.execute(query, (y[0],))
                          mydb.commit()

                   #
                   #   E_table  (waybill_id)
                   #
                   E_colum=x[1]
                   query = ("SELECT waybill_id FROM %s  WHERE  waybill_id = %%s limit 1;") %(E_table,)
                   mycursor.execute(query, (E_colum,))
                   E_result = mycursor.fetchall()

                   if E_result:
                       for y in E_result:
                          #print "y[0]=%s" % (y[0])
                          #print "table %s (waybill_id) = %s" % (E_table,y[0])
                          query = ("delete from  %s  where waybill_id = %%s;") %(E_table,)
                          mycursor.execute(query, (y[0],))
                          mydb.commit()


           # clear A_table for order_id 
           query = ("delete from  %s  where order_id = %%s;")  %(A_table,)
           A_order_id=x[0]
           mycursor.execute(query, (A_order_id,))
           mydb.commit()
           #print "---------------------------------------"
      

    #
    # step 8 | 
    # END SECTION
    #





    #
    # step 9 | property  (order_id,property_id)
    #

    #
    #  A_table  (order_id,property_id)
    # 
    A_table = "property"                  # set help table name
    B_table = "category_property"         # set help table name
    C_table = "property_employee"         # set help table name
    D_table = "cargo"                     # set help table name
    E_table = "cargo_service"             # additional help table name
    F_table = "storage"                   # additional help table name
    G_table = "storage_service"           # additional help table name


    A_order_id = d                        # set order_id  for search

    query = ("SELECT order_id,property_id FROM  `%s`  WHERE  order_id = %%s;")  %(A_table,)
    mycursor.execute(query, (A_order_id,))
    A_result = mycursor.fetchall()
    #print "table property(order_id,property_id)=(%s,%s)" % (A_order_id,A_result)

    if A_result:
           # clear B_table and other help tables for order_id and property_id
           #print "---------------------------------------"
           for x in A_result:
                   # x[0] is order_id | x[1] is property_id
                   #print "table %s  (order_id,property_id) = (%s,%s)" % (A_table,x[0],x[1])

                   #
                   #   B_table  (property_id)
                   #
                   B_colum=x[1]
                   query = ("SELECT property_id FROM %s  WHERE  property_id = %%s limit 1;") %(B_table,)
                   mycursor.execute(query, (B_colum,))
                   B_result = mycursor.fetchall()

                   if B_result:
                       for y in B_result:
                          #print "y[0]=%s" % (y[0])
                          #print "table %s (property_id) = %s" % (B_table,y[0])
                          query = ("delete from  %s  where property_id = %%s;") %(B_table,)
                          mycursor.execute(query, (y[0],))
                          mydb.commit()

                   #
                   #   C_table  (property_id)
                   #
                   C_colum=x[1]
                   query = ("SELECT property_id FROM %s  WHERE  property_id = %%s limit 1;") %(C_table,)
                   mycursor.execute(query, (C_colum,))
                   C_result = mycursor.fetchall()

                   if C_result:
                       for y in C_result:
                          #print "y[0]=%s" % (y[0])
                          #print "table %s (property_id) = %s" % (C_table,y[0])
                          query = ("delete from  %s  where property_id = %%s;") %(C_table,)
                          mycursor.execute(query, (y[0],))
                          mydb.commit()


                   #
                   #   D_table  (property_id)
                   #
                   D_colum=x[1]
                   query = ("SELECT property_id, cargo_id FROM %s  WHERE  property_id = %%s;") %(D_table,)
                   mycursor.execute(query, (D_colum,))
                   D_result = mycursor.fetchall()

                   if D_result:
                       for y in D_result:
                           #print  y[0] is property_id | y[1] is cargo_id
                           #print "table %s  (property_id,cargo_id) = (%s,%s)" % (D_table,y[0],y[1])

                           #
                           #   E_table  (cargo_id)
                           #
                           E_colum=y[1]
                           query = ("SELECT cargo_id FROM %s  WHERE  cargo_id = %%s limit 1;") %(E_table,)
                           mycursor.execute(query, (E_colum,))
                           E_result = mycursor.fetchall()

                           if E_result:
                               for z in E_result:
                                  #print "z[0]=%s" % (z[0])
                                  #print "table %s (cargo_id) = %s" % (E_table,z[0])
                                  query = ("delete from  %s  where cargo_id = %%s;") %(E_table,)
                                  mycursor.execute(query, (z[0],))
                                  mydb.commit()
                           #
                           #   F_table  (cargo_id)
                           #
                           F_colum=y[1]
                           query = ("SELECT cargo_id FROM %s  WHERE  cargo_id = %%s limit 1;") %(F_table,)
                           mycursor.execute(query, (F_colum,))
                           F_result = mycursor.fetchall()

                           if F_result:
                               for z in F_result:
                                  #print "z[0]=%s" % (z[0])
                                  #print "table %s (cargo_id) = %s" % (F_table,z[0])
                                  query = ("delete from  %s  where cargo_id = %%s;") %(F_table,)
                                  mycursor.execute(query, (z[0],))
                                  mydb.commit()
                           #
                           #   G_table  (cargo_id)
                           #
                           G_colum=y[1]
                           query = ("SELECT cargo_id FROM %s  WHERE  cargo_id = %%s limit 1;") %(G_table,)
                           mycursor.execute(query, (G_colum,))
                           G_result = mycursor.fetchall()

                           if G_result:
                               for z in G_result:
                                  #print "z[0]=%s" % (z[0])
                                  #print "table %s (cargo_id) = %s" % (G_table,z[0])
                                  query = ("delete from  %s  where cargo_id = %%s;") %(G_table,)
                                  mycursor.execute(query, (z[0],))
                                  mydb.commit()

                       

                       # delete rows in D_table for parent_cargo_id
                       #print "cargo_id=%s, parent_cargo_id=%s" % (y[1],y[1])
                       query = ("delete from  %s  where parent_cargo_id = %%s;") %(D_table,)
                       mycursor.execute(query, (y[1],))
                       mydb.commit()
                   
                       # delete rows in D_table for property_id
                       query = ("delete from  %s  where property_id = %%s;") %(D_table,)
                       mycursor.execute(query, (y[0],))
                       mydb.commit()


           # clear A_table for order_id 
           query = ("delete from  %s  where order_id = %%s;")  %(A_table,)
           A_order_id=x[0]
           mycursor.execute(query, (A_order_id,))
           mydb.commit()
           #print "---------------------------------------"
      

    #
    # step 9 | 
    # END SECTION
    #




    #
    # step 9.5 |  cargo (order_id,cargo_id,parent_cargo_id)
    #
    A_table = "cargo"
    A_order_id = d
    B_table = "cargo"
    query = ("SELECT order_id, cargo_id FROM  `%s`  WHERE  order_id = %%s;")  %(A_table,)
    mycursor.execute(query, (A_order_id,))
    A_result = mycursor.fetchall()
    #print "table cargo, current order_id= %s, rows with this order_id are : (order_id,cargo_id)=(%s)" % (A_order_id,A_result)

    if A_result:
           # clear B_table and other help tables for  cargo_id and parent_cargo_id
           #print "---------------------------------------"
           for x in A_result:
                   # x[0] is order_id | x[1] is cargo_id
                   #print "table %s  (order_id,cargo_id) = (%s,%s)" % (A_table,x[0],x[1])

                   #
                   #   B_table  (property_id)
                   #
                   B_colum=x[1]
                   query = ("SELECT cargo_id,parent_cargo_id FROM %s  WHERE  parent_cargo_id = %%s;") %(B_table,)
                   mycursor.execute(query, (B_colum,))
                   B_result = mycursor.fetchall()

                   if B_result:
                       for y in B_result:
                          #print "y[0]=%s" % (y[0])
                          #print "table %s , row with (cargo_id,parent_cargo_id) = (%s,%s) is going to be deleted" % (B_table,y[0],y[1])
                          query = ("DELETE FROM  %s  WHERE cargo_id= %%s AND parent_cargo_id = %%s;") %(B_table,)
                          mycursor.execute(query, (y[0],y[1]))
                          mydb.commit()


    query = ("delete from `cargo`  where order_id = %s")
    mycursor.execute(query, (d,))
    mydb.commit()




    #
    #  step 10 | order (order_id)
    #
    #print "order has order_id=",d
    #print "table `order` , trying to delete order_id =  (%s)" % (d)
    query = ("delete from  `order` where order_id = %s")
    mycursor.execute(query, (d,))
    mydb.commit()
    #print "table `order`, order_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
    #print "\n"



    # print stats
    mydb.commit()
    # print current time
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #print "\n"
    #print "-----------------------------"
    #print "Current Time =", current_time
    #print "table order, (order_id)=%s" %(d)
    #print " 1 row has been deleted\n"
    #print "-----------------------------"
    #print "\n"




    #print "the program has finished successsfully."
         

    mydb.commit()
    mycursor.close()
    mydb.close()

