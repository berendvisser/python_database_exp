import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="newuser",
  passwd="password",
  database="pythontest"
)

mycursor = mydb.cursor()

def add_column(name):
    mycursor.execute("ALTER TABLE `dmx` ADD `%s` TINYINT UNSIGNED NULL DEFAULT NULL"%(name))
    mydb.commit()
def remove_column(name):
    mycursor.execute("ALTER TABLE `dmx` DROP `%s`"%(name))
    mydb.commit()

def set_channel_static(channel, value):
    mycursor.execute("UPDATE `dmx` SET `%s` = '%d' WHERE `dmx`.`TIME` = 0;;"%(str(channel), value))
    mydb.commit()

def set_channels_dynamic(time, channel, value):
    sql = "INSERT INTO `dmx` (TIME, `%d`) VALUES (%s, %s)"%(channel,"%s","%s")
    val = (str(time), str(value))
    mycursor.execute(sql, val)
    mydb.commit()
    
mycursor.executemany