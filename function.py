# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:09:47 2023

@author: Fancyui@Gobel
"""

import numpy as np
import math as math

#caculate hex value of field length

# str info = "C2 06 C5 5C"

def field_length(info):
    
    hex_data_array = bytearray.fromhex(info)
    
    hex_data_list = list(hex_data_array)
    
    lenid = len(hex_data_list)
    
    sum_lenid = math.floor(lenid/16/16) + math.floor(lenid/16) + np.mod(lenid,16)
    
    mod_lenid = np.mod(sum_lenid,16)
    
    lcksum = 255-mod_lenid+1-240
    
    lcksum_up = lcksum * pow(2,12)
    
    length = hex(lcksum_up + lenid)
    
    return length

    
    
