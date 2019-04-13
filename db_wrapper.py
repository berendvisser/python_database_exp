import mysql.connector
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  passwd="password",
  database="pythontest"
)
list_channels = "`1`"
for i in range(2,513):
    list_channels +=",`"+str(i)+"`" 

mycursor = mydb.cursor(buffered=True)

def add_column(name):

    mycursor.execute("ALTER TABLE `dmx` ADD `%s` TINYINT UNSIGNED NULL DEFAULT NULL"%(name))
    mydb.commit()

def remove_column(name):
    mycursor.execute("ALTER TABLE `dmx` DROP `%s`"%(name))
    mydb.commit()

def set_channels_static(channels, values):
    str_sql = "`"+str(channels[0])+"` = '"+str(values[0])+"'"
    
    if len(channels)>>1:
        for i in range(1, len(channels)):
            str_sql +=",`"+str(channels[i])+"` = '"+str(values[i])+"'"
         
    
    sql = "UPDATE `dmx` SET %s WHERE `dmx`.`TIME` = 0;"%(str_sql)
    
    mycursor.execute(sql)
    mydb.commit()

def set_channels_dynamic(time, channel, value):
    sql = "INSERT INTO `dmx` (TIME, `%d`) VALUES (%s, %s)"%(channel,"%s","%s")
    val = (str(time), str(value))
    mycursor.execute(sql, val)
    mydb.commit()

def get_channels_static():
    #sql = "SELECT * FROM `dmx` WHERE TIME=0"
    sql = "SELECT %s FROM `dmx` WHERE TIME=0"%(list_channels)
    start = time.time()
    mycursor.execute(sql)
    
    result = mycursor.fetchone()
    elapsed = time.time()
    
    
    print(elapsed-start)
    return(result)

    
