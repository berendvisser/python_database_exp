
import time

import requests

import db_wrapper







url = "http://frankpi.student.utwente.nl:9090/set_dmx"





def set_dmx():
 

    list = db_wrapper.get_channels_static()



    str_list = str(list[0])
    
    for i in range(1,len(list)):
        str_list += ","+(str(list[i]))
    
    data = {"u": 1, "d": str_list}

    requests.post(url, data).text