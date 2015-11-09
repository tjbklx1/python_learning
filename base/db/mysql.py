import MySQLdb

db=MySQLdb.connect(user='root',db='mysql',passwd='mysql',host='localhost')
cursor=db.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print "Database version : %s" % data
db.close()

#Database version : 5.6.21-log


###########Create Table#######################
import MySQLdb

db=MySQLdb.connect(user='root',db='test',passwd='mysql',host='localhost')
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)"""
cursor.execute(sql)
print "Create table employee done..." 
db.close()




###########Insert#######################
import MySQLdb

db=MySQLdb.connect(user='root',db='test',passwd='mysql',host='localhost')
cursor=db.cursor()
sql= """insert into employee (first_name,last_name,age,sex,income) values('John','Smith',20,'M',2000) """
try:
    cursor.execute(sql)
    db.commit()
    print "insert and commit ...."
except:
    db.rollback()
    print "rollback ...."
    
db.close()



import MySQLdb

db=MySQLdb.connect(user='root',db='test',passwd='mysql',host='localhost')
cursor=db.cursor()
sql= "insert into employee (first_name,last_name,age,sex,income) values('%s','%s','%d','%c','%d') " % ('John','Smith',20,'M',3000)
try:
    cursor.execute(sql)
    db.commit()
    print "insert and commit ...."
except:
    db.rollback()
    print "rollback ...."
    
db.close()


###########Select#######################
import MySQLdb

db=MySQLdb.connect(user='root',db='test',passwd='mysql',host='localhost')
cursor=db.cursor()
sql= "select * from employee where income >%d " % (1000)
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        first_name=row[0]
        last_name=row[1]
        age=row[2]
        sex=row[3]
        income=row[4]
        print "(first_name=%s,last_name=%s,age=%d,sex=%s,income=%d) " %(first_name,last_name,age,sex,income) 
except Exception, e: 
    print str(e) 
    print "Error: Unable to fetch data"
    
db.close()



###########Update#######################
import MySQLdb

db=MySQLdb.connect(user='root',db='test',passwd='mysql',host='localhost')
cursor=db.cursor()
sql= "update employee set age =age+1 where sex ='%c' " % ('M')
try:
    cursor.execute(sql)
    db.commit()
except Exception, e: 
    print str(e) 
    db.rollback()
    
db.close()    