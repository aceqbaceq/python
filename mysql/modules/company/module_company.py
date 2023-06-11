#!/usr/bin/python
import sys
import datetime
import mysql.connector
from termcolor import colored

# module account
sys.path.append('../account')
import module_account

# module contract
sys.path.append('../contract')
import module_contract

# module employee
sys.path.append('../employee')
import module_employee

# module price_list
sys.path.append('../price_list')
import module_price_list






def company ( initial_company_id=None, 
            DB_Host=None, 
            DB_User=None, 
            DB_Password=None, 
            DB_Name=None, 
            DB_Port=None
          ):

#
#  function description:
#  function 'def company'  deletes  rows in `company` table using 'initial_company_id'
#  'initial_company_id' specifies (company_id)  row in `company` table we want to delete
#

  if (
          initial_company_id    is None
      or  DB_Host             is None
      or  DB_User             is None
      or  DB_Password         is None
      or  DB_Name             is None 
      or  DB_Port             is None

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
         
    module_name = "company"


  #
  # step 1 |  company (company_id)
  #
  A_table = "company"
  query = ("SELECT SQL_NO_CACHE company_id   FROM `%s` WHERE company_id=%%s ORDER BY company_id ASC LIMIT 1")  %(A_table,)
  mycursor.execute(query, (initial_company_id, ))
  myresult = mycursor.fetchall()

  l = 0     
  for x in myresult:
         l = len(myresult)
         #print "company_id=",x[0]
         #print "\n"
  if l == 0:
     #print colored("file %s | ERROR: | 'company_id' is not found, please specify another 'initial_company_id'. \n ", 'red') % (__file__)
     return
  else: 
      d=x[0]
      #d=12334    # for hardcode setting of account_id uncomment this line
      #print "\n"
      #print "table `company`, company_id=%s | START TRANSACTION |" % (d)
      #sys.stdout.write("current company_id: %s   \r" % (d) )
      #sys.stdout.flush()
      #print ""





  #
  # step 2 |  account (account_id, company_id) 
  #
  A_table = "account"
  query = ("SELECT SQL_NO_CACHE account_id  FROM `%s` WHERE  company_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         m = module_account.account(  initial_account_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )

         if m == 10:
            print " module %s | submodule account returned error \"payment gateway detected\" | skip company_id = %s " % (module_name, d)
            return(10)
         #print "delete from table `%s` is succeded" %(A_table)






  #
  # step 3 | contact (company_id)
  #
  A_table = "contact"
  query = ("SELECT SQL_NO_CACHE     company_id     FROM `%s` WHERE  company_id = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult_contact = mycursor.fetchall()

  if myresult_contact:
     for x in myresult_contact:
        query = ("update `%s` set company_id=null  where company_id = %%s") %(A_table)
        mycursor.execute(query, (x[0],))
        mydb.commit()






  #
  # step 4 |  contract (contract_id, company_id) 
  #
  A_table = "contract"
  query = ("SELECT SQL_NO_CACHE   contract_id     FROM `%s` WHERE  company_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_contract.contract(  initial_contract_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)





  #
  # step 5 |  employee (employee_id, company_id) 
  #
  A_table = "employee"
  query = ("SELECT SQL_NO_CACHE   employee_id     FROM `%s` WHERE  company_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_employee.employee(  initial_employee_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)





  #
  # step 6 | netting_partner_city (company_id)
  #
  A_table = "netting_partner_city"
  query = ("SELECT SQL_NO_CACHE    company_id     FROM `%s` WHERE    company_id   = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where company_id   = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 7 | netting_partner_scheme (company_id)
  #
  A_table = "netting_partner_scheme"
  query = ("SELECT SQL_NO_CACHE    company_id     FROM `%s` WHERE    company_id   = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where company_id   = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()



  #
  # step 7.1 | order_profit (credit_company_id)
  #
  A_table = "order_profit"
  query = ("SELECT SQL_NO_CACHE    credit_company_id     FROM `%s` WHERE    credit_company_id   = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where    credit_company_id   = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()




  #
  # step 7.2 | order_profit (debit_company_id)
  #
  A_table = "order_profit"
  query = ("SELECT SQL_NO_CACHE    debit_company_id     FROM `%s` WHERE    debit_company_id   = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where    debit_company_id   = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()







  #
  # step 8 | order_profit_options (curator_company_id)
  #
  A_table = "order_profit_options"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE    curator_company_id     FROM `%s` WHERE    curator_company_id   = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where    curator_company_id   = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
  #print "exit step with %s table" %(A_table)



  #
  # step 9 | order_profit_options (from_company_id)
  #
  A_table = "order_profit_options"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE    from_company_id     FROM `%s` WHERE    from_company_id   = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where    from_company_id   = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
  #print "exit step with %s table" %(A_table)




  #
  # step 10 | order_profit_options (to_company_id)
  #
  A_table = "order_profit_options"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE    to_company_id     FROM `%s` WHERE    to_company_id   = %%s;")  %(A_table,)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     query = ("delete from  `%s`  where    to_company_id   = %%s") %(A_table)
     mycursor.execute(query, (d,))
     mydb.commit()
  #print "exit step with %s table" %(A_table)




  #
  # step 11 |  price_list (price_list_id, company_id) 
  #
  A_table = "price_list"
  #print "enter step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE   price_list_id     FROM `%s` WHERE  company_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         module_price_list.price_list(  initial_price_list_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)



  #
  # step 12 |  company (company_id, parent_id)  | warning recursive lauch
  #
  A_table = "company"
  # print "module company | recursive launch | enter module company step with %s table"  %(A_table)
  query = ("SELECT SQL_NO_CACHE   company_id     FROM `%s` WHERE  parent_id = %%s;")  %(A_table)
  mycursor.execute(query, (d,))
  myresult = mycursor.fetchall()

  if myresult:
     #print "module company | recursive launch | enter module company step with %s table | parent_id= %s, its company_id= %s"  %(A_table, d, myresult[0])
     for x in myresult:
         #print "i am going to delete from table `%s`" %(A_table)
         company(  initial_company_id=x[0],
                         DB_Host=DB_Host,
                         DB_User=DB_User,
                         DB_Password=DB_Password,
                         DB_Name=DB_Name,
                         DB_Port=DB_Port )
         #print "delete from table `%s` is succeded" %(A_table)
  #print "exit step with %s table" %(A_table)











  #
  #  step 13 | company (company_id)
  #
  A_table = "company"
  #print "table `company` has company_id=",d
  #print "table `company` , trying to delete company_id =  (%s)" % (d)
  #print "enter step with %s table"  %(A_table)
  query = ("delete from  `company` where company_id = %s")
  mycursor.execute(query, (d,))
  mydb.commit()
  #print "table `company`, company_id =  (%s) is deleted  | STATUS SUCCESS |" % (d)
  #print "\n"
  #print "exit step with %s table" %(A_table)



  # print stats
  mydb.commit()
  # print current time
  from datetime import datetime
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  #print "\n"
  #print "-----------------------------"
  #print "Current Time =", current_time
  #print "table `company`, (company_id)=%s" %(d)
  #print " 1 row has been deleted\n"
  #print "-----------------------------"
  #print "\n"



  #print "the program has finished successsfully."

  mydb.commit()
  mycursor.close()
  mydb.close()


