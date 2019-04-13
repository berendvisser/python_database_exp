
import time
import db_wrapper
import mysql.connector
while(1):
    db_wrapper.set_channels_dynamic(int(time.time()*1000),255,100)
    


# for i in range(1,513):
#     db_wrapper.set_channel_static(i,0)

# for i in range(1,513):
#     db_wrapper.add_column("%s"%(str(i)))

