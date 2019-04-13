
import time
import db_wrapper
import mysql.connector
import ola_wrapper


db_wrapper.set_channels_static([1,2,3,4,5,6],[0,0,255,0,0,0])

ola_wrapper.set_dmx()



# for i in range(1,513):
#     db_wrapper.set_channel_static(i,0)

# for i in range(1,513):
#     db_wrapper.add_column("%s"%(str(i)))

